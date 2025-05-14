"""
Скрипт для архивации ссылок из Readwise.

Получает список документов из API Readwise и создает отчеты в формате Markdown
для каждого location документа.

Пример использования:
    uv run ./app/main.py --api-key your_api_key --dir ./reports
"""

import argparse
from pathlib import Path

from formatters.markdown import create_markdown_report
from schemas.readwise import ReadwiseDocument
from services.readwise import fetch_reader_document_list_api


def create_reports(
    *,
    token: str,
    dir: str,
):
    """
    Создает отчеты в формате Markdown для каждого location документа.
    Сохраняет отчеты в указанной директории в файлы с именами,
    соответствующими location документа.

    :param token: API ключ для авторизации в Readwise
    :param dir: Директория для сохранения отчетов
    :return: None
    """
    locations = [
        "new",
        "later",
        "shortlist",
        "archive",
    ]

    for location in locations:
        print(f"🚀 Создаю отчет для '{location}'...")
        documents: list[ReadwiseDocument] = fetch_reader_document_list_api(
            token=token,
            location=location,
        )

        report = create_markdown_report(
            documents=documents,
            location=location,
            # Добавляем summary только для 'later' - материалов, отобранных к прочтению
            add_summary=True if location == "later" else False,
        )

        filename = f"{location}.md"
        filepath = Path(dir) / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w") as f:
            f.write(report)
        print(f"✅ Отчет '{location}' сохранен в '{filepath}'")


def main():
    parser = argparse.ArgumentParser(
        description="Скрипт для архивации ссылок из Readwise",
    )
    parser.add_argument(
        "--api-key",
        required=True,
        help="API ключ для авторизации",
    )
    parser.add_argument(
        "--dir",
        required=False,
        default="links",
        help="Директория для сохранения отчетов",
    )
    args = parser.parse_args()

    create_reports(
        token=args.api_key,
        dir=args.dir,
    )


if __name__ == "__main__":
    main()
