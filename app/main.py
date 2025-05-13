import argparse

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
    args = parser.parse_args()

    archived_links: list[ReadwiseDocument] = fetch_reader_document_list_api(
        token=args.api_key,
        location="archive",
    )

    report = create_markdown_report(documents=archived_links)
    with open("archive.md", "w") as f:
        f.write(report)


if __name__ == "__main__":
    main()
