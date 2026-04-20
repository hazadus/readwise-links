"""
Содержит функции для создания отчетов в формате Markdown.
"""

from schemas.readwise import ReadwiseDocument


def create_markdown_report(
    *,
    documents: list[ReadwiseDocument],
    location: str | None = None,
    add_summary: bool = False,
) -> str:
    """
    Создает отчет в формате Markdown из списка документов.

    :param documents: Список документов
    :param location: Локация документа (new, later, shortlist, archive)
    :param add_summary: Добавлять ли summary в отчет
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
        source_url = doc.source_url or doc.url
        reader_link = f" [📖]({doc.url})" if doc.url != source_url else ""
        author = f" 👤 {doc.author}" if doc.author else ""

        tags_text = ""
        if doc.tags:
            tags = [f"#{tag}" for tag in doc.tags]
            tags_text = " 🔖 " + ", ".join(tags)

        word_count = ""
        if doc.word_count:
            word_count = f" 💬 {doc.word_count}"

        notes = ""
        if doc.notes:
            notes = f"    > **Заметка:** {doc.notes}\n"

        summary = ""
        if add_summary and doc.summary:
            summary = f"    > **Резюме:** {doc.summary}\n"

        saved_at = doc.saved_at.strftime(" 🗓️ %Y-%m-%d")

        report += (
            f"- [{doc.title}]({source_url}){reader_link}{author}{word_count}{tags_text}{saved_at}\n"
            f"{notes}"
            f"{summary}"
        )

    return report
