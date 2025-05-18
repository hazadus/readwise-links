"""
Скрипт для архивации ссылок из Readwise.

Получает список документов из API Readwise и создает:

- отчеты в формате Markdown. Отчёты создаются для каждой локации (new, later,
shortlist, archive) и для каждого тега (в поддиректории "tags" заданной для
отчетов директории).
- дампы всех заметок и выделений в формате JSON, сохраняется в отдельных файлах
в указанной директории.
- дамп статей у которых есть заметки и выделения в формате JSON, сохраняется в
"./web/src/assets/articles.json" для использования во фронтовом приложении.

Пример использования:
    uv run ./app/main.py --api-key your_api_key --dir ./reports
"""

import argparse

from reports import create_dumps, create_reports, dump_docs_with_notes_and_highlights


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

    dump_docs_with_notes_and_highlights(
        token=args.api_key,
        dir="./web/src/assets",
    )
    create_dumps(
        token=args.api_key,
        dir=args.dir,
    )
    create_reports(
        token=args.api_key,
        dir=args.dir,
    )


if __name__ == "__main__":
    main()
