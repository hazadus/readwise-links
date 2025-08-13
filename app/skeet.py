"""
Скрипт для публикации документов из Readwise в виде skeet'ов в Bluesky.

- Получает список документов из JSON файла
- Фильтрует их по тегу "toot"
- Проверяет, были ли они уже опубликованы
- Публикует новые документы в Bluesky
- Сохраняет информацию о skeet'ах в JSON файл

Для работы требуется передать идентификатор пользователя Bluesky и пароль как аргументы командной строки.

Пример использования:
    uv run ./app/skeet.py your-username.bsky.social your-password
"""

import argparse
import json
import os
from urllib.parse import urlparse, urlunparse

from integrations.bluesky import publish_message
from pydantic import BaseModel
from schemas.readwise import ReadwiseDocument

ARTICLES_JSON_FILE_PATH = "./web/src/assets/articles.json"
SKEETS_JSON_FILE_PATH = "./data/skeets.json"


class Skeet(BaseModel):
    document_id: str
    document_title: str | None = None
    source_url: str
    skeet_url: str


class SkeetData(BaseModel):
    skeeted_doc_ids: list[str]
    skeets: list[Skeet]


def main():
    parser = argparse.ArgumentParser(description="Публикация документов в Bluesky")
    parser.add_argument(
        "identifier",
        help="Идентификатор пользователя Bluesky (например: username.bsky.social)",
    )
    parser.add_argument("password", help="Пароль пользователя Bluesky")

    args = parser.parse_args()

    documents = load_documents(file_path=ARTICLES_JSON_FILE_PATH)
    print(f"Загружено {len(documents)} документов из {ARTICLES_JSON_FILE_PATH}")

    docs_for_skeets = get_documents_with_tag(
        documents=documents,
        tag="toot",
    )
    print(f"Найдено {len(docs_for_skeets)} документов с тегом 'toot'")

    skeet_data = load_skeets(file_path=SKEETS_JSON_FILE_PATH)
    print(f"Загружено {len(skeet_data.skeeted_doc_ids)} уже опубликованных документов")

    new_ids, new_skeets = skeet_new_docs(
        skeet_data=skeet_data,
        docs_for_skeets=docs_for_skeets,
        identifier=args.identifier,
        password=args.password,
    )

    skeet_data.skeeted_doc_ids.extend(new_ids)
    skeet_data.skeets.extend(new_skeets)

    print(f"Добавлено {len(new_ids)} новых skeet'ов")

    save_skeets(skeet_data=skeet_data, file_path=SKEETS_JSON_FILE_PATH)


def load_documents(
    *,
    file_path: str,
) -> list[ReadwiseDocument]:
    """
    Загружает документы из JSON файла.

    Args:
        file_path (str): Путь к файлу с документами.

    Returns:
        list[ReadwiseDocument]: Список документов.
    """
    with open(file_path, "r") as f:
        data = json.load(f)
    return [ReadwiseDocument(**doc) for doc in data]


def get_documents_with_tag(
    *,
    documents: list[ReadwiseDocument],
    tag: str,
) -> list[ReadwiseDocument]:
    """
    Фильтрует документы по тегу.

    Args:
        documents (list[ReadwiseDocument]): Список документов.
        tag (str): Тег для фильтрации.

    Returns:
        list[ReadwiseDocument]: Список документов, содержащих указанный тег.
    """
    return [doc for doc in documents if doc.tags and tag in doc.tags.keys()]


def compose_message(
    *,
    doc: ReadwiseDocument,
) -> str:
    """
    Формирует сообщение для skeet'а на основе документа.

    Args:
        doc (ReadwiseDocument): Документ для skeet'а.

    Returns:
        str: Сформированное сообщение.
    """

    # Фильтруем теги, исключая служебные и добавляя # для хештегов
    # Очищаем теги от специальных символов, которые могут помешать распознаванию
    def clean_tag(tag: str) -> str:
        # Убираем специальные символы, оставляем только буквы, цифры и подчеркивания
        import re

        cleaned = re.sub(r"[^\wа-яё]", "", tag.lower())
        return cleaned

    tags = [
        f"#{clean_tag(tag)}"
        for tag in doc.tags.keys()
        if tag not in ["skeet", "toot"] and clean_tag(tag)
    ]

    # Убираем query-часть из URL для чистоты
    parsed_url = urlparse(doc.source_url)
    clean_url = urlunparse(
        (
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            parsed_url.params,
            "",  # query - убираем
            parsed_url.fragment,
        )
    )

    # Формируем сообщение с правильным форматированием
    # Bluesky автоматически распознает URL и хештеги
    message_parts = []

    if doc.notes and doc.notes.strip():
        message_parts.append(doc.notes.strip())

    if clean_url:
        message_parts.append(clean_url)

    if tags:
        message_parts.append(" ".join(tags))

    return "\n\n".join(message_parts)


def load_skeets(
    *,
    file_path: str,
) -> SkeetData:
    """
    Загружает данные о skeet'ах из файла.

    Args:
        file_path (str): Путь к файлу с данными о skeet'ах.

    Returns:
        SkeetData: Данные о skeet'ах.
    """
    if not os.path.exists(file_path):
        return SkeetData(skeeted_doc_ids=[], skeets=[])

    with open(file_path, "r") as f:
        data = json.load(f)
    return SkeetData(**data)


def save_skeets(
    *,
    skeet_data: SkeetData,
    file_path: str,
):
    """
    Сохраняет данные о skeet'ах в файл.

    Args:
        skeet_data (SkeetData): Данные о skeet'ах.
        file_path (str): Путь к файлу для сохранения.
    """
    res = json.dumps(
        skeet_data.model_dump(),
        ensure_ascii=False,
        indent=4,
    )
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write(res)


def skeet_new_docs(
    *,
    skeet_data: SkeetData,
    docs_for_skeets: list[ReadwiseDocument],
    identifier: str,
    password: str,
) -> tuple[list[str], list[Skeet]]:
    """
    Публикует новые документы в виде skeet'ов.
    Возвращает список новых ID и список новых skeet'ов.

    Args:
        skeet_data (SkeetData): Данные о skeet'ах.
        docs_for_skeets (list[ReadwiseDocument]): Документы для skeet'ов.
        identifier (str): Идентификатор пользователя Bluesky.
        password (str): Пароль пользователя Bluesky.

    Returns:
        tuple: Список новых ID и список новых skeet'ов.
    """
    new_skeets: list[Skeet] = []
    new_ids: list[str] = []

    for doc in docs_for_skeets:
        if doc.id in skeet_data.skeeted_doc_ids:
            continue

        message = compose_message(doc=doc)
        print(f"Отправляем сообщение в Bluesky:")
        print(f"Длина: {len(message)} символов")
        print(f"Содержимое:\n{repr(message)}")
        print("-" * 50)

        skeet_url = publish_message(
            message=message,
            identifier=identifier,
            password=password,
        )
        if not skeet_url:
            continue

        new_ids.append(doc.id)
        new_skeets.append(
            Skeet(
                document_id=doc.id,
                document_title=doc.title,
                source_url=doc.source_url,
                skeet_url=skeet_url,
            )
        )

    return new_ids, new_skeets


if __name__ == "__main__":
    main()
