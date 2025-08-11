"""
Скрипт для публикации документов из Readwise в виде туитов.

- Получает список документов из JSON файла
- Фильтрует их по тегу "toot"
- Проверяет, были ли они уже туитнуты
- Публикует новые документы в Mastodon
- Сохраняет информацию о туитах в JSON файл

Для работы требуется файл "toot_usercred.secret" в корне проекта с токеном доступа к Mastodon.

Пример использования:
    uv run ./app/toot.py
"""

import json
import os
from urllib.parse import urlparse, urlunparse

from integrations.mastodon import publish_message
from pydantic import BaseModel
from schemas.readwise import ReadwiseDocument

ARTICLES_JSON_FILE_PATH = "./web/src/assets/articles.json"
TOOTS_JSON_FILE_PATH = "./data/toots.json"


class Toot(BaseModel):
    document_id: str
    document_title: str | None = None
    source_url: str
    toot_url: str


class TootData(BaseModel):
    tooted_doc_ids: list[str]
    toots: list[Toot]


def main():
    documents = load_documents(file_path=ARTICLES_JSON_FILE_PATH)
    print(f"Загружено {len(documents)} документов из {ARTICLES_JSON_FILE_PATH}")

    docs_for_toots = get_documents_with_tag(
        documents=documents,
        tag="toot",
    )
    print(f"Найдено {len(docs_for_toots)} документов с тегом 'Toot'")

    toot_data = load_toots(file_path=TOOTS_JSON_FILE_PATH)
    print(f"Загружено {len(toot_data.tooted_doc_ids)} уже туитнутых документов")

    new_ids, new_toots = toot_new_docs(
        toot_data=toot_data,
        docs_for_toots=docs_for_toots,
    )

    toot_data.tooted_doc_ids.extend(new_ids)
    toot_data.toots.extend(new_toots)

    print(f"Добавлено {len(new_ids)} новых туитов")

    save_toots(toot_data=toot_data, file_path=TOOTS_JSON_FILE_PATH)


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
    Формирует сообщение для туита на основе документа.

    Args:
        doc (ReadwiseDocument): Документ для туита.

    Returns:
        str: Сформированное сообщение.
    """
    tags = [f"#{tag}" for tag in doc.tags.keys() if tag != "toot"]

    # Убираем query-часть из URL
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

    return f"{doc.notes}\n\n{clean_url}\n\n{', '.join(tags)}"


def load_toots(
    *,
    file_path: str,
) -> TootData:
    """
    Загружает данные о туитах из файла.

    Args:
        file_path (str): Путь к файлу с данными о туитах.

    Returns:
        TootData: Данные о туитах.
    """
    if not os.path.exists(file_path):
        return TootData(tooted_doc_ids=[], toots=[])

    with open(file_path, "r") as f:
        data = json.load(f)
    return TootData(**data)


def save_toots(
    *,
    toot_data: TootData,
    file_path: str,
):
    """
    Сохраняет данные о туитах в файл.

    Args:
        toot_data (TootData): Данные о туитах.
        file_path (str): Путь к файлу для сохранения.
    """
    res = json.dumps(
        toot_data.model_dump(),
        ensure_ascii=False,
        indent=4,
    )
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write(res)


def toot_new_docs(
    *,
    toot_data: TootData,
    docs_for_toots: list[ReadwiseDocument],
) -> tuple[list[str], list[Toot]]:
    """
    Публикует новые документы в виде туитов.
    Возвращает список новых ID и список новых туитов.

    Args:
        toot_data (TootData): Данные о туитах.
        docs_for_toots (list[ReadwiseDocument]): Документы для туитов.

    Returns:
        tuple: Список новых ID и список новых туитов.
    """
    new_toots: list[Toot] = []
    new_ids: list[str] = []

    for doc in docs_for_toots:
        if doc.id in toot_data.tooted_doc_ids:
            continue

        message = compose_message(doc=doc)
        toot_url = publish_message(message=message)
        if not toot_url:
            continue

        new_ids.append(doc.id)
        new_toots.append(
            Toot(
                document_id=doc.id,
                document_title=doc.title,
                source_url=doc.source_url,
                toot_url=toot_url,
            )
        )

    return new_ids, new_toots


if __name__ == "__main__":
    main()
