import asyncio
import logging
from asyncio import Lock, Queue
from pathlib import Path
from urllib.parse import urljoin
from uuid import uuid4

import aiofiles
import httpx
from bs4 import BeautifulSoup
from logger import setup_logging

logger = logging.getLogger(__name__)

ARCHIVE_DIR = "./scratch/archive"
MAX_DOWNLOAD_WORKERS = 5


async def main():
    print("Scraping data...")

    # TODO: загрузить список ссылок из файла "../web/src/assets/articles.json"

    url = "https://simonwillison.net/2025/May/21/chatgpt-new-memory/#atom-everything"
    page_id = "willison_post"

    # TODO: проверять, что страница не была загружена ранее - по имени директории
    # TODO: использовать asyncio.gather для параллельной загрузки

    await scrape_page(
        url=url,
        output_dir=Path(ARCHIVE_DIR) / page_id,
    )


async def scrape_page(
    *,
    url: str,
    output_dir: str,
):
    # Загружаем страницу
    logger.info(f"Downloading {url}")
    data = await download_url(url=url)
    if data is None:
        logger.error(f"Failed to download {url}")
        return
    html = data.decode(encoding="utf-8")

    # Вытащить из страницы ссылки на изображения, JS, CSS
    links_map = get_all_links_from_html(
        url=url,
        html=html,
    )

    # Загрузить изображения, JS, CSS по ссылкам и сохранить в файлы в указанную директорию
    all_links = list(links_map.values())
    names = await download_links(
        links=all_links,
        output_dir=output_dir,
    )

    # Заменить ссылки в HTML на локальные
    for link in links_map.keys():
        # Получаем имя файла, cначала получая абсолютную ссылку через исходную (из HTML)
        absolute_link = links_map[link]
        filename = names.get(absolute_link)
        # Заменяем исходные ссылки в HTML на локальные имена файлов
        html = html.replace(link, filename)

    # Cохранить изменённый HTML в файл
    filepath = Path(output_dir) / "index.html"
    await save_to_file(
        filepath=filepath,
        content=html.encode(encoding="utf-8"),
    )
    logger.info(f"Saved {filepath}")


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

    # Словар для хранения соответствия между ссылками и именами локальных файлов
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

        logger.info(f"Worker {worker_id} | Downloading {link} to {filepath}")
        data = await download_url(url=link)
        if data is None:
            logger.error(f"Worker {worker_id} | Failed to download {link}")
            # В случае ошибки, оставляем оригинальную ссылку
            async with download_lock:
                links_to_filenames[link] = link
            continue

        await save_to_file(
            filepath=filepath,
            content=data,
        )

        # Сохраняем соответствие между ссылкой и именем файла
        async with download_lock:
            links_to_filenames[link] = filename
        logger.info(f"Worker {worker_id} | Saved {filepath}")

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
    # Извлекаем расширение файла из URL
    extension = url.split(".")[-1]
    if not extension:
        extension = ""
    return f"{uuid4()}.{extension}"


async def download_url(
    *,
    url: str,
) -> bytes | None:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.content
        else:
            logger.warning(f"Failed to download {url}: {response.status_code}")
            return None


async def save_to_file(
    *,
    filepath: Path,
    content: bytes,
) -> None:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    async with aiofiles.open(filepath, "wb") as f:
        await f.write(content)


if __name__ == "__main__":
    setup_logging()
    asyncio.run(main())
