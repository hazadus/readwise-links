"""
Содержит функции для работы с API Readwise.
"""

from time import sleep

import requests
import urllib3
from schemas.readwise import ReadwiseDocument, ReadwiseDocumentList


def fetch_reader_document_list_api(
    *,
    token: str,
    updated_after=None,
    location=None,
) -> list[ReadwiseDocument]:
    """
    Получает список документов из API Readwise.

    :param token: API ключ для авторизации в Readwise
    :param updated_after: Дата обновления документа в формате YYYY-MM-DD
    :param location: Локация документа (new, later, shortlist, archive)
    :return: Список документов
    """
    full_data: list[ReadwiseDocument] = []
    next_page_cursor = None

    urllib3.disable_warnings()

    while True:
        params = {}
        if next_page_cursor:
            params["pageCursor"] = next_page_cursor
        if updated_after:
            params["updatedAfter"] = updated_after
        if location:
            params["location"] = location

        print("Делаю запрос к API с параметрами " + str(params) + "...")

        response = requests.get(
            url="https://readwise.io/api/v3/list/",
            params=params,
            headers={"Authorization": f"Token {token}"},
            verify=False,
        )

        try:
            res = ReadwiseDocumentList(**response.json())
            full_data.extend(res.results)
            got = len(full_data)
            total = response.json().get("count")
            print(f"Получено ссылок: {got} шт., осталось: {total} шт.")
        except KeyError:
            print("Error: " + str(response.json()))
            break

        next_page_cursor = response.json().get("nextPageCursor")
        sleep(3)  # Rate limiting

        if not next_page_cursor:
            break
    return full_data
