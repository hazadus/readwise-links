from schemas.readwise import ReadwiseDocument


def create_markdown_report(
    *,
    documents: list[ReadwiseDocument],
) -> str:
    """
    Создает отчет в формате Markdown из списка документов.
    """
    report = "# Архивные ссылки\n\n"

    for doc in documents:
        author = f" 👤 {doc.author}" if doc.author else ""
        report += f"- [{doc.title}]({doc.source_url}){author}\n"

    return report
