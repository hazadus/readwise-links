from pathlib import Path

from formatters.json import create_json_dump
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
        "later",
        "new",
        "archive",
        "shortlist",
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
            # Добавляем summary только для 'later' - материалов,
            # отобранных к прочтению
            add_summary=True if location == "later" else False,
        )

        filename = f"{location}.md"
        filepath = Path(dir) / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w") as f:
            f.write(report)
        print(f"✅ Отчет '{location}' сохранен в '{filepath}'")

    # Создаем отчеты для тегов
    all_tags = get_tags(documents=all_documents)
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


def create_dumps(
    *,
    token: str,
    dir: str,
):
    """
    Создает дампы в формате JSON для категорий note, highlight документа.
    Сохраняет дампы в указанной директории в файлы с именами,
    соответствующими category документа.

    :param token: API ключ для авторизации в Readwise
    :param dir: Директория для сохранения дампов
    :return: None
    """
    categories = [
        "note",
        "highlight",
    ]

    for cat in categories:
        print(f"🚀 Создаю JSON-дамп для '{cat}'...")
        highlights = fetch_reader_document_list_api(
            token=token,
            category=cat,
        )
        filepath = Path(dir) / f"{cat}.json"
        save_as_json(
            documents=highlights,
            filepath=filepath,
        )
        print(f"✅ JSON для '{cat}' сохранен в '{filepath}'")


def get_tags(
    *,
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
    *,
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


def save_as_json(
    *,
    documents: list[ReadwiseDocument],
    filepath: Path,
):
    """
    Конвертирует документы в формат JSON и сохраняет в файл по указанному
    пути.

    :param documents: Список документов Readwise
    :param filepath: Путь к файлу для сохранения JSON
    """
    result = create_json_dump(documents=documents)
    with open(filepath, "w") as f:
        f.write(result)
