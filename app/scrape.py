import asyncio
import logging
from pathlib import Path
from urllib.parse import urljoin
from uuid import uuid4

import aiofiles
import httpx
from bs4 import BeautifulSoup
from logger import setup_logging

logger = logging.getLogger(__name__)

ARCHIVE_DIR = "./scratch/archive"


async def main():
    print("Scraping data...")
    url = "https://simonwillison.net/2025/May/21/chatgpt-new-memory/#atom-everything"
    page_id = "willison_post"

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
    html = data.decode()

    # Вытащить из страницы ссылки на изображения, JS, CSS
    all_links = get_all_links_from_html(
        url=url,
        html=html,
    )

    # Загрузить изображения, JS, CSS по ссылкам и сохранить в файлы в указанную директорию
    names = await download_links(
        links=all_links,
        output_dir=output_dir,
    )

    # TODO: заменить ссылки в HTML на локальные

    # TODO: сохранить изменённый HTML в файл

    # Сохраняем страницу в файл
    filepath = Path(output_dir) / "index.html"
    await save_to_file(filepath=filepath, content=data)
    logger.info(f"Saved {filepath}")


def get_all_links_from_html(
    *,
    url: str,
    html: str,
) -> list[str]:
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
    all_links = [
        urljoin(url, link) if not link.startswith("http") else link
        for link in css_links + img_links + js_links
    ]
    return all_links


async def download_links(
    *,
    links: list[str],
    output_dir: str,
) -> dict[str, str]:
    links_to_names = {}
    # TODO: использовать asyncio.gather для параллельной загрузки
    for link in links:
        filename = create_filename(url=link)
        filepath = Path(output_dir) / filename
        logger.info(f"Downloading {link} to {filepath}")
        data = await download_url(url=link)
        if data is None:
            logger.error(f"Failed to download {link}")
            # В случае ошибки, оставляем оригинальную ссылку
            links_to_names[link] = link
            continue
        await save_to_file(
            filepath=filepath,
            content=data,
        )
        # Сохраняем имя файла в словаре для замены в HTML
        links_to_names[link] = filename
        logger.info(f"Saved {filepath}")
    return links_to_names


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
