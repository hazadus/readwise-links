import asyncio
import logging
from pathlib import Path

import aiofiles
import httpx
from logger import setup_logging

logger = logging.getLogger(__name__)

ARCHIVE_DIR = "./scratch/archive"


async def main():
    print("Scraping data...")
    url = "https://simonwillison.net/2025/May/21/chatgpt-new-memory/#atom-everything"
    page_id = "willison_post"

    await scrape_page(
        url=url,
        dir=Path(ARCHIVE_DIR) / page_id,
    )


async def scrape_page(
    *,
    url: str,
    dir: str,
):
    # Загружаем страницу
    logger.info(f"Downloading {url}")
    data = await download_url(url=url)
    if data is None:
        logger.error(f"Failed to download {url}")
        return

    # TODO: вытащить из страницы ссылки на изображения, JS, CSS

    # TODO: загрузить изображения, JS, CSS по ссылкам и сохранить в файлы в указанную директорию

    # TODO: заменить ссылки в HTML на локальные

    # TODO: сохранить изменённый HTML в файл

    # Сохраняем страницу в файл
    filepath = Path(dir) / "index.html"
    await save_to_file(filepath=filepath, content=data)
    logger.info(f"Saved {filepath}")


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
