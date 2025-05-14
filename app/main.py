"""
Скрипт для архивации ссылок из Readwise.

Получает список документов из API Readwise и создает отчеты в формате Markdown.
Отчёты создаются для каждой локации (new, later, shortlist, archive) и для каждого
тега (в поддиректории "tags" заданной для отчетов директории).

Пример использования:
    uv run ./app/main.py --api-key your_api_key --dir ./reports
"""

import argparse
from pathlib import Path

from formatters.markdown import create_markdown_report
from schemas.readwise import ReadwiseDocument
from services.readwise import fetch_reader_document_list_api


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
    all_documents: list[ReadwiseDocument] = []

    # Создаем отчеты для каждого location
    for location in locations:
        print(f"🚀 Создаю отчет для '{location}'...")
        documents: list[ReadwiseDocument] = fetch_reader_document_list_api(
            token=token,
            location=location,
        )
        all_documents.extend(documents)

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

    # Создаем отчеты для тегов
    all_tags = get_tags(all_documents)
    for tag in all_tags:
        print(f"📌 Тег: {tag}")
        tagged_documents = get_documents_by_tag(
            documents=all_documents,
            tag=tag,
        )
        report = create_markdown_report(
            documents=tagged_documents,
            location=tag,
            add_summary=True,
        )
        filename = f"{tag}.md"
        filepath = Path(dir + "/tags") / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w") as f:
            f.write(report)
        print(f"✅ Отчет для тега '{tag}' сохранен в '{filepath}'")


def get_tags(
    documents: list[ReadwiseDocument],
) -> set[str]:
    """
    Извлекает уникальные теги из списка документов.

    :param documents: Список документов Readwise
    :return: Множество уникальных тегов
    """
    tags = set()
    for doc in documents:
        if doc.tags:
            tags.update(doc.tags.keys())
    return tags


def get_documents_by_tag(
    documents: list[ReadwiseDocument],
    tag: str,
) -> list[ReadwiseDocument]:
    """
    Фильтрует документы по указанному тегу.

    :param documents: Список документов Readwise
    :param tag: Тег для фильтрации
    :return: Список документов, содержащих указанный тег
    """
    return [doc for doc in documents if doc.tags and tag in doc.tags]


if __name__ == "__main__":
    main()
