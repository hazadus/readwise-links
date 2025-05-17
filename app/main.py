"""
Скрипт для архивации ссылок из Readwise.

Получает список документов из API Readwise и создает:

- отчеты в формате Markdown. Отчёты создаются для каждой локации (new, later,
shortlist, archive) и для каждого тега (в поддиректории "tags" заданной для
отчетов директории).
- дампы заметок и highlights в JSON-файлах.

Пример использования:
    uv run ./app/main.py --api-key your_api_key --dir ./reports
"""

import argparse

from reports import create_dumps, create_reports


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
