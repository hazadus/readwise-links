"""Создание отчетов и дампов документов Readwise в формате JSON и Markdown."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from formatters.json import create_json_dump
from formatters.markdown import create_markdown_report
from schemas.readwise import ReadwiseDocument


def create_reports(
    *,
    all_docs: list[ReadwiseDocument],
    dir: str,
):
    """
    Создает отчеты в формате Markdown для каждого location документа.
    Сохраняет отчеты в указанной директории в файлы с именами,
    соответствующими location документа.

    :param all_docs: Список всех документов Readwise
    :param dir: Директория для сохранения отчетов
    :return: None
    """
    locations = [
        "later",
        "new",
        "archive",
        "shortlist",
    ]
    # Создаем отчеты для каждого location
    for location in locations:
        print(f"🚀 Создаю отчет для '{location}'...")
        documents: list[ReadwiseDocument] = [
            doc for doc in all_docs if doc.location == location
        ]

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
    all_tags = get_tags(documents=all_docs)
    for tag in all_tags:
        print(f"📌 Тег: {tag}")
        tagged_documents = get_documents_by_tag(
            documents=all_docs,
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


def dump_docs_to_json(
    *,
    all_docs: list[ReadwiseDocument],
    dir: str,
):
    """
    Создает дамп документов в формате JSON в указанной директории
    в файл articles.json.

    :param all_docs: Список всех документов Readwise
    :param dir: Директория для сохранения дампа
    :return: None
    """
    print("🚀 Делаю мапу...")
    hashmap = {}
    for doc in all_docs:
        hashmap[doc.id] = doc.model_dump()

    print("🚀 Добавляем заметки и highlights к документам...")
    # Сначала добавим заметки к highlight'ам
    for doc in all_docs:
        if doc.category == "note":
            if doc.parent_id not in hashmap.keys():
                print(f"    Нет дока с id={doc.parent_id}")
                print(f"        Заметка: {doc.id=} {doc.content}")
                continue

            if not hashmap[doc.parent_id].get("notes_attached", None):
                hashmap[doc.parent_id]["notes_attached"] = [doc.model_dump()]
            else:
                hashmap[doc.parent_id]["notes_attached"].append(doc.model_dump())
            print(
                f"        ✅ Заметка: '{doc.content}' к '{hashmap[doc.parent_id]["content"]}'"
            )
    # Теперь добавим highlights к документам: берем их из хашмапы, потому что там
    # highlights уже должны быть с заметками к ним
    for doc_id in hashmap.keys():
        doc = hashmap[doc_id]
        if doc["category"] == "highlight":
            if doc["parent_id"] not in hashmap.keys():
                print(f"    Нет дока с id={doc["parent_id"]}")
                print(f"        Highlight: {doc["id"]=} {doc["content"]}")
                continue

            if not hashmap[doc["parent_id"]].get("highlights", None):
                hashmap[doc["parent_id"]]["highlights"] = [doc]
            else:
                hashmap[doc["parent_id"]]["highlights"].append(doc)

    # Оставляем только документы, у которых нет родителя
    root_docs = []
    for doc_id in hashmap.keys():
        doc = hashmap[doc_id]
        has_no_parent = doc["parent_id"] is None
        if has_no_parent:
            root_docs.append(doc)

    # Делаем дамп полученных доков в файл JSON
    def datetime_serializer(obj: Any) -> str:
        """Преобразует datetime объекты в ISO формат."""
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Тип {type(obj)} не сериализуем")

    res = json.dumps(
        root_docs,
        ensure_ascii=False,
        indent=4,
        default=datetime_serializer,
    )

    filepath = Path(dir) / "articles.json"
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w") as f:
        f.write(res)

    print(f"✅ Сохранено {len(root_docs)} док. в '{filepath}'")


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
