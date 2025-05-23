"""
Скрипт для загрузки статей и их ресурсов из архива Readwise Reader.

- Загружает статьи из файла articles.json, формирует очередь ссылок для обработки
и запускает асинхронные задачи для загрузки страниц и их ресурсов.

- После загрузки страницы, извлекает ссылки на изображения, JS и CSS, загружает их и
сохраняет в файлы в поддиректории в указанной директории.

- Затем изменяет в HTML ссылки на сохранённые файлы на локальные и сохраняет изменённый
HTML в файл index.html.

Использует асинхронные задачи для параллельной загрузки страниц и их ресурсов.

Пример использования (из корневой директории проекта):
    uv run ./app/scrape.py
"""

import asyncio
import json
import logging
import os
from asyncio import Lock, Queue, Semaphore
from pathlib import Path
from time import perf_counter
from urllib.parse import urljoin, urlparse
from uuid import uuid4

import aiofiles
import httpx
from bs4 import BeautifulSoup
from logger import setup_logging
from schemas.readwise import EnrichedReadwiseDocument

# Для просты хардкодим параметры, не выделяя их в аргументы или конфиг.
# Они не будут меняться, а если будут, то не критично.
ARCHIVE_DIR = "./scratch/archive"
MAX_CACHE_SIZE = 1000 * 1024 * 1024  # 1000MB
MAX_SCRAPE_WORKERS = 8  # По количеству ядер в M1
MAX_DOWNLOAD_WORKERS = 16  # x2 от количества ядер
HTTPX_TIMEOUT = 10  # секунд
STOP_TOKEN = object()  # Уникальный объект как сигнал остановки рабочим

logger = logging.getLogger(__name__)
request_semaphore = Semaphore(20)  # Ограничиваем количество одновременных запросов
file_semaphore = Semaphore(8)  # Ограничиваем кол-во одновременных файловых операций
download_cache: dict[str, bytes] = {}  # URL -> content
current_cache_size = 0
cache_size_lock = Lock()


async def main():
    # Загрузим список ссылок из файла "./web/src/assets/articles.json"
    articles = load_articles_from_file(
        filepath=Path("./web/src/assets/articles.json"),
    )
    print(f"Загружено {len(articles)} постов")

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
        and not os.path.exists(Path(ARCHIVE_DIR) / doc.id / "index.html")
    ]
    print(f"В очереди {scrape_queue.qsize()} ссылок для обработки")

    # Используем единый HTTP клиент для всех запросов
    scrapers = []
    try:
        async with httpx.AsyncClient(
            timeout=HTTPX_TIMEOUT,
            follow_redirects=True,
        ) as client:
            scrapers = [
                asyncio.create_task(
                    scrape_worker(
                        worker_id=worker_id,
                        scrape_queue=scrape_queue,
                        output_dir=ARCHIVE_DIR,
                        client=client,
                    )
                )
                for worker_id in range(MAX_SCRAPE_WORKERS)
            ]

            # Добавляем STOP_TOKEN для каждого воркера для исключения
            # блокировок при завершении
            for _ in range(MAX_SCRAPE_WORKERS):
                scrape_queue.put_nowait(STOP_TOKEN)

            start = perf_counter()
            await scrape_queue.join()
            elapsed_time = perf_counter() - start
            print(f"🎉 Загрузка завершена за {elapsed_time:.2f} сек.")
    except KeyboardInterrupt:
        print("\n⚠️ Прерывание работы по Ctrl+C")
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
    finally:
        # Убедимся, что все задачи отменены корректно
        for task in scrapers:
            if not task.done():
                task.cancel()

        if scrapers:
            # Собираем возможные исключения из отмененных задач
            await asyncio.gather(*scrapers, return_exceptions=True)


async def scrape_worker(
    *,
    worker_id: int,
    scrape_queue: Queue,
    output_dir: str,
    client: httpx.AsyncClient,
):
    """
    Рабочий для загрузки страниц. После загрузки страницы, извлекает ссылки на
    изображения, JS и CSS, загружает их и сохраняет в файлы в поддиректории
    в указанной директории. Затем сохраняет изменённый HTML в файл.

    :param worker_id: ID рабочего
    :param scrape_queue: Очередь ссылок для загрузки
    :param output_dir: Директория для сохранения поддиректорий с загруженными файлами
    :param client: HTTP клиент для загрузки страниц
    """
    while True:
        doc = await scrape_queue.get()
        try:
            if doc is STOP_TOKEN:
                break

            url = doc.source_url

            logger.info(
                f"Worker S-{worker_id} | Осталось: {scrape_queue.qsize()} | 🚀 Скачиваю {url}"
            )
            data = await download_url_cached(
                url=url,
                client=client,
            )
            if data is None:
                logger.error(f"Worker S-{worker_id} | ❌ Не смог скачать {url}")
                continue

            # Пробуем декодировать контент с помощью нескольких кодировок
            # Если не получится, то просто пропускаем страницу
            html = None
            encodings_to_try = ["utf-8", "latin-1", "windows-1252", "iso-8859-1"]

            for encoding in encodings_to_try:
                try:
                    html = data.decode(encoding=encoding)
                    logger.debug(
                        f"Worker S-{worker_id} | Успешно декодировал {url} как {encoding}"
                    )
                    break
                except UnicodeDecodeError:
                    continue

            if html is None:
                logger.error(
                    f"Worker S-{worker_id} | ❌ Не смог декодировать {url} с помощью "
                    f"{', '.join(encodings_to_try)}"
                )
                continue

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
                client=client,
            )

            # Заменить ссылки в HTML на локальные
            for link in links_map.keys():
                # Получаем имя файла, cначала получая абсолютную ссылку через исходную (из HTML)
                absolute_link = links_map[link]
                filename = names.get(absolute_link)
                # Заменяем исходные ссылки в HTML на локальные имена файлов, если файл скачан
                if filename is not None:
                    html = html.replace(link, filename)
                else:
                    # Если файл не скачан, то оставляем оригинальную ссылку в абсолютном виде
                    html = html.replace(link, absolute_link)

            # Cохранить изменённый HTML в файл
            filepath = Path(doc_output_dir) / "index.html"
            await save_to_file(
                filepath=filepath,
                content=html.encode(encoding="utf-8"),
            )
            logger.info(f"Worker S-{worker_id} | 📥 Сохранён {filepath}")
        except Exception as e:
            logger.error(
                f"Worker S-{worker_id} | ❌ Ошибка при обработке {doc.source_url}: {e}"
            )
        finally:
            # Всегда отмечаем задачу как выполненную, даже при ошибке
            scrape_queue.task_done()


async def download_links(
    *,
    links: list[str],
    output_dir: str,
    client: httpx.AsyncClient,
) -> dict[str, str]:
    """
    Загружает файлы по указанным ссылкам и сохраняет их в указанной директории.

    :param links: Список ссылок для загрузки
    :param output_dir: Директория для сохранения файлов
    :param client: HTTP клиент для загрузки файлов
    :return: Словарь с соответствием между ссылками и именами локальных файлов
    """
    # Заполняем очередь ссылками для загрузки
    download_queue = Queue()
    [download_queue.put_nowait(link) for link in links]

    # Добавляем STOP_TOKEN для каждого воркера для исключения
    # блокировок при завершении
    for _ in range(MAX_DOWNLOAD_WORKERS):
        download_queue.put_nowait(STOP_TOKEN)

    # Словарь для хранения соответствия между ссылками и именами локальных файлов
    links_to_filenames = {}
    download_lock = Lock()

    # Использовать asyncio.gather для параллельной загрузки
    try:
        downloaders = [
            asyncio.create_task(
                download_worker(
                    worker_id=worker_id,
                    download_queue=download_queue,
                    download_lock=download_lock,
                    output_dir=output_dir,
                    links_to_filenames=links_to_filenames,
                    client=client,
                )
            )
            for worker_id in range(MAX_DOWNLOAD_WORKERS)
        ]

        # Обрабатываем всю очередь воркерами
        await download_queue.join()
        for task in downloaders:
            task.cancel()
        await asyncio.gather(*downloaders, return_exceptions=True)
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        for task in downloaders:
            if not task.done():
                task.cancel()

    return links_to_filenames


async def download_worker(
    *,
    worker_id: int,
    download_queue: Queue,
    download_lock: Lock,
    output_dir: str,
    links_to_filenames: dict[str, str],
    client: httpx.AsyncClient,
) -> None:
    """
    Рабочий для загрузки файлов. После загрузки файла, сохраняет его в указанной
    директории и обновляет словарь links_to_filenames с соответствием между
    ссылкой и именем файла.

    :param worker_id: ID рабочего
    :param download_queue: Очередь ссылок для загрузки
    :param download_lock: Блокировка для синхронизации доступа к словарю
    :param output_dir: Директория для сохранения файлов
    :param links_to_filenames: Словарь для хранения соответствия между ссылками и именами файлов
    :param client: HTTP клиент для загрузки файлов
    """
    while True:
        link = await download_queue.get()
        try:
            if link is STOP_TOKEN:
                break

            filename = create_filename(url=link)
            filepath = Path(output_dir) / filename

            logger.info(f"Worker D-{worker_id} | Скачиваю {link} to {filepath}")
            data = await download_url_cached(
                url=link,
                client=client,
            )
            if data is None:
                logger.error(f"Worker D-{worker_id} | Не смог скачать {link}")
                # В случае ошибки, оставляем оригинальную ссылку
                async with download_lock:
                    links_to_filenames[link] = link
                continue

            await save_to_file(
                filepath=filepath,
                content=data,
            )
            logger.debug(f"Worker D-{worker_id} | 💾 Сохранён {filepath}")

            # Сохраняем соответствие между ссылкой и именем файла
            async with download_lock:
                links_to_filenames[link] = filename

        except Exception as e:
            logger.error(f"Worker D-{worker_id} | ❌ Ошибка при обработке {link}: {e}")
            # В случае исключения, тоже оставляем оригинальную ссылку
            try:
                async with download_lock:
                    links_to_filenames[link] = link
            except Exception:
                pass
        finally:
            # Всегда отмечаем задачу как выполненную, даже при ошибке
            download_queue.task_done()


def get_all_links_from_html(
    *,
    url: str,
    html: str,
) -> dict[str, str]:
    """
    Извлекает все ссылки на изображения, JS и CSS из HTML-кода страницы.

    :param url: URL страницы
    :param html: HTML-код страницы
    :return: Словарь с соответствием между ссылками и их абсолютными URL
    """
    soup = BeautifulSoup(html, "html.parser")

    # Извлекаем все типы ссылок, используя один экземпляр BeautifulSoup
    css_links = [
        link.get("href")
        for link in soup.find_all(name="link", attrs={"rel": "stylesheet"})
        if link.get("href")
    ]

    img_links = [
        img.get("src")
        for img in soup.find_all(name="img")
        if img.get("src") and not img.get("src").startswith("data:")
    ]

    js_links = [
        script.get("src")
        for script in soup.find_all(name="script")
        if script.get("src")
    ]

    # Формируем абсолютные ссылки в формате
    # ключ - ссылка из HTML, значение - абсолютная ссылка для скачивания
    links_map = {}
    for link in css_links + img_links + js_links:
        links_map[link] = (
            urljoin(url, link)
            if not (link.startswith("http") or link.startswith("//"))
            else link
        )
    return links_map


def create_filename(
    *,
    url: str,
) -> str:
    """
    Создаёт уникальное имя файла на основе URL. Исходное имя файла нас
    не интересует, поэтому новое имя будет сгенерировано случайно.

    :param url: URL для создания имени файла
    :return: Имя файла
    """
    path = urlparse(url).path
    if "." in path:
        extension = path.split(".")[-1]
        return f"{uuid4()}.{extension}"
    return f"{uuid4()}"


async def download_url_cached(
    *,
    url: str,
    client: httpx.AsyncClient,
) -> bytes | None:
    """
    Загружает контент по указанному URL с использованием кеша.
    Кэширование важно, так как в архива много страниц с одних и тех же сайтов,
    использующих одинаковые ресурсы.

    :param url: URL для загрузки
    :param client: HTTP клиент для загрузки
    :return: Контент в байтах или None в случае ошибки
    """
    global current_cache_size

    if url in download_cache.keys():
        logger.info(
            f"🔄 Используем кеш для {url} (размер кэша: {current_cache_size} байт)"
        )
        return download_cache[url]

    result = await download_url(
        url=url,
        client=client,
    )

    # Проверяем, переполнится ли кеш при добавлении нового элемента
    async with cache_size_lock:
        size = len(result) if result is not None else 0
        if current_cache_size + size <= MAX_CACHE_SIZE:
            logger.debug(f"🔄 Сохраняем кеш для {url}")
            download_cache[url] = result
            current_cache_size += size
        else:
            logger.debug("❌ Кеш переполнен, больше не сохраняем")

    return result


async def download_url(
    *,
    url: str,
    client: httpx.AsyncClient,
) -> bytes | None:
    """
    Загружает контент по указанному URL.

    :param url: URL для загрузки
    :param client: HTTP клиент для загрузки
    :return: Контент в байтах или None в случае ошибки
    """
    async with request_semaphore:
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
    """
    Сохраняет контент в файл.

    :param filepath: Путь к файлу
    :param content: Контент для сохранения
    """
    filepath.parent.mkdir(parents=True, exist_ok=True)
    async with file_semaphore:
        async with aiofiles.open(filepath, "wb") as f:
            await f.write(content)


def load_articles_from_file(
    *,
    filepath: Path,
) -> list[EnrichedReadwiseDocument]:
    """
    Загружает статьи из файла articles.json.

    :param filepath: Путь к файлу articles.json
    :return: Список статей
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
