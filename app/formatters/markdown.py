"""
Содержит функции для создания отчетов в формате Markdown.
"""

from schemas.readwise import ReadwiseDocument


def create_markdown_report(
    *,
    documents: list[ReadwiseDocument],
    location: str | None = None,
) -> str:
    """
    Создает отчет в формате Markdown из списка документов.

    :param documents: Список документов
    :param location: Локация документа (new, later, shortlist, archive)
    :return: Отчет в формате Markdown
    """
    titles = {
        "new": "Новые ссылки",
        "later": "Отложенные ссылки",
        "shortlist": "Шортлист ссылок",
        "archive": "Архивные ссылки",
    }
    title = titles.get(location, "Ссылки")

    total = len(documents)
    report = f"# {title}\n\n- Всего ссылок: {total}\n\n"

    if total > 0:
        report += "## Ссылки\n\n"

    for doc in documents:
        author = f" 👤 {doc.author}" if doc.author else ""

        tags_text = ""
        if doc.tags:
            tags = [f"#{tag}" for tag in doc.tags]
            tags_text = " 🔖 " + ", ".join(tags)

        report += f"- [{doc.title}]({doc.source_url}){author}{tags_text}\n"

    return report
