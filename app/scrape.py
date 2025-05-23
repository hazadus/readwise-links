import asyncio
import json
import logging
import os
from asyncio import Lock, Queue
from pathlib import Path
from time import perf_counter
from urllib.parse import urljoin, urlparse
from uuid import uuid4

import aiofiles
import httpx
from bs4 import BeautifulSoup
from logger import setup_logging
from schemas.readwise import EnrichedReadwiseDocument

logger = logging.getLogger(__name__)

ARCHIVE_DIR = "./scratch/archive"
MAX_DOWNLOAD_WORKERS = 5
MAX_SCRAPE_WORKERS = 5
HTTPX_TIMEOUT = 10  # секунд


async def main():
    # Загрузим список ссылок из файла "./web/src/assets/articles.json"
    articles = load_articles_from_file(
        filepath=Path("./web/src/assets/articles.json"),
    )
    print(f"Загружено {len(articles)} постов")

    # Сформируем список ссылок для обработки

    # Наполняем очередь ссылками для обработки и загрузки
    # проверяем, что страница не была загружена ранее - по имени директории
    # и имеет id - иначе не сможем потом понять, что это за страница
    scrape_queue = Queue()
    [
        scrape_queue.put_nowait(doc)
        for doc in articles
        if doc.source_url is not None
        and doc.category == "article"
        and doc.id is not None
        and not os.path.exists(Path(ARCHIVE_DIR) / doc.id)
    ]
    print(f"В очереди {scrape_queue.qsize()} ссылок для обработки")

    # Использовать asyncio.gather для параллельной загрузки
    scrapers = [
        asyncio.create_task(
            scrape_worker(
                worker_id=worker_id,
                scrape_queue=scrape_queue,
                output_dir=ARCHIVE_DIR,
            )
        )
        for worker_id in range(MAX_SCRAPE_WORKERS)
    ]

    start = perf_counter()
    await asyncio.gather(
        scrape_queue.join(),
        *scrapers,
    )
    end = start - perf_counter()
    print(f"🎉 Загрузка завершена за {end:.2f} сек.")


async def scrape_worker(
    *,
    worker_id: int,
    scrape_queue: Queue,
    output_dir: str,
):
    while not scrape_queue.empty():
        # Загружаем страницу
        doc: EnrichedReadwiseDocument = scrape_queue.get_nowait()
        url = doc.source_url

        logger.info(f"Worker S-{worker_id} | Скачиваю {url}")
        data = await download_url(url=url)
        if data is None:
            logger.error(f"Worker S-{worker_id} | ❌ Не смог скачать {url}")
            # Отметить задачу как выполненную
            scrape_queue.task_done()
            continue

        html = data.decode(encoding="utf-8")

        # Вытащить из страницы ссылки на изображения, JS, CSS
        links_map = get_all_links_from_html(
            url=url,
            html=html,
        )

        # Загрузить изображения, JS, CSS по ссылкам и сохранить в файлы в поддиректорию в
        # указанной директории
        doc_output_dir = Path(output_dir) / doc.id
        all_links = list(links_map.values())
        names = await download_links(
            links=all_links,
            output_dir=doc_output_dir,
        )

        # Заменить ссылки в HTML на локальные
        for link in links_map.keys():
            # Получаем имя файла, cначала получая абсолютную ссылку через исходную (из HTML)
            absolute_link = links_map[link]
            filename = names.get(absolute_link)
            # Заменяем исходные ссылки в HTML на локальные имена файлов
            html = html.replace(link, filename)

        # Cохранить изменённый HTML в файл
        filepath = Path(doc_output_dir) / "index.html"
        await save_to_file(
            filepath=filepath,
            content=html.encode(encoding="utf-8"),
        )
        logger.info(f"Worker S-{worker_id} | 📥 Сохранён {filepath}")

        # Отметить задачу как выполненную
        scrape_queue.task_done()


def get_all_links_from_html(
    *,
    url: str,
    html: str,
) -> dict[str, str]:
    css_links = get_rel_links_from_html(
        html=html,
        rel_type="stylesheet",
    )

    img_links = get_img_links_from_html(
        html=html,
    )

    js_links = get_js_links_from_html(
        html=html,
    )

    # Формируем абсолютные ссылки
    # Ссылка из файла : полная ссылка
    links_map = {}
    for link in css_links + img_links + js_links:
        links_map[link] = urljoin(url, link) if not link.startswith("http") else link
    return links_map


async def download_links(
    *,
    links: list[str],
    output_dir: str,
) -> dict[str, str]:
    # Заполняем очередь ссылками для загрузки
    download_queue = Queue()
    [download_queue.put_nowait(link) for link in links]

    # Словарь для хранения соответствия между ссылками и именами локальных файлов
    links_to_filenames = {}
    download_lock = Lock()

    # Использовать asyncio.gather для параллельной загрузки
    downloaders = [
        asyncio.create_task(
            download_worker(
                worker_id=worker_id,
                download_queue=download_queue,
                download_lock=download_lock,
                output_dir=output_dir,
                links_to_filenames=links_to_filenames,
            )
        )
        for worker_id in range(MAX_DOWNLOAD_WORKERS)
    ]

    # Обрабатываем всю очередь воркерами
    await asyncio.gather(
        download_queue.join(),
        *downloaders,
    )

    return links_to_filenames


async def download_worker(
    *,
    worker_id: int,
    download_queue: Queue,
    download_lock: Lock,
    output_dir: str,
    links_to_filenames: dict[str, str],
) -> None:
    while not download_queue.empty():
        link = download_queue.get_nowait()
        filename = create_filename(url=link)
        filepath = Path(output_dir) / filename

        logger.info(f"Worker D-{worker_id} | Скачиваю {link} to {filepath}")
        data = await download_url(url=link)
        if data is None:
            logger.error(f"Worker D-{worker_id} | Не смог скачать {link}")
            # В случае ошибки, оставляем оригинальную ссылку
            async with download_lock:
                links_to_filenames[link] = link
            # Отметить задачу как выполненную
            download_queue.task_done()
            continue

        await save_to_file(
            filepath=filepath,
            content=data,
        )

        # Сохраняем соответствие между ссылкой и именем файла
        async with download_lock:
            links_to_filenames[link] = filename
        logger.info(f"Worker D-{worker_id} | Сохранён {filepath}")

        # Отметить задачу как выполненную
        download_queue.task_done()


def get_rel_links_from_html(
    *,
    html: str,
    rel_type: str = "stylesheet",
) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for link in soup.find_all(name="link", attrs={"rel": rel_type}):
        href = link.get("href")
        if href:
            links.append(href)
    return links


def get_img_links_from_html(
    *,
    html: str,
) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for img in soup.find_all(name="img"):
        src = img.get("src")
        if src:
            links.append(src)
    return links


def get_js_links_from_html(
    *,
    html: str,
) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for script in soup.find_all(name="script"):
        src = script.get("src")
        if src:
            links.append(src)
    return links


def create_filename(
    *,
    url: str,
) -> str:
    # Извлекаем имя файла из URL (убираем параметры запроса и якоря)
    path = urlparse(url).path
    # Извлекаем расширение файла из path
    if not "." in path:
        # Если в URL нет точки, то не можем определить расширение
        extension = ""
    else:
        extension = path.split(".")[-1]

    if not extension:
        extension = ""
    return f"{uuid4()}.{extension}" if extension != "" else f"{uuid4()}"


async def download_url(
    *,
    url: str,
) -> bytes | None:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                url=url,
                timeout=HTTPX_TIMEOUT,
                # Обязательно следуем за редиректами
                follow_redirects=True,
            )
        except httpx.ConnectTimeout as e:
            logger.error(f"❌ Таймаут соединения с {url}: {e}")
            return None
        except httpx.RequestError as e:
            logger.error(f"❌ Ошибка запроса к {url}: {e}")
            return None

        if response.status_code == 200:
            return response.content
        else:
            logger.warning(f"❌ Не смог скачать {url}: {response.status_code}")
            return None


async def save_to_file(
    *,
    filepath: Path,
    content: bytes,
) -> None:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    async with aiofiles.open(filepath, "wb") as f:
        await f.write(content)


def load_articles_from_file(
    *,
    filepath: Path,
) -> list[EnrichedReadwiseDocument]:
    """
    Загружает статьи из файла articles.json.
    """
    if not filepath.exists():
        logger.error(f"❌ Файл {filepath} не существует")
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        data = f.read()

    parsed_data = json.loads(data)
    articles = [EnrichedReadwiseDocument.model_validate(doc) for doc in parsed_data]
    return articles


if __name__ == "__main__":
    setup_logging()
    asyncio.run(main())
