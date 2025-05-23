"""
Схемы данных для работы с API Readwise.
Документация API: https://readwise.io/reader_api
"""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, field_validator


class ReadwiseDocument(BaseModel):
    """Схема данных для документа Readwise."""

    id: str
    url: str
    source_url: str | None = None
    title: str | None = None
    author: str | None = None
    source: str | None = None
    # One of: article, email, rss, highlight, note, pdf, epub, tweet, video:
    category: str
    location: str | None = None  # One of: new, later, shortlist, archive, feed
    tags: dict | None = None
    site_name: str | None = None
    word_count: int | None
    notes: str | None = ""
    summary: str | None = None
    image_url: str | None = None
    parent_id: str | None = None
    reading_progress: float = 0.0
    content: str | None = None  # для заметок, highlights
    html_content: str | None = None
    published_date: str | None = None
    created_at: datetime
    updated_at: datetime
    saved_at: datetime
    first_opened_at: datetime | None = None
    last_opened_at: datetime | None = None
    last_moved_at: datetime | None = None

    @field_validator("published_date", mode="before")
    @classmethod
    def validate_published_date(cls, v: Any) -> str | None:
        """Convert integer timestamp to string format if needed"""
        if v is None:
            return None
        if isinstance(v, int):
            return datetime.fromtimestamp(v / 1000).strftime("%Y-%m-%d")
        return v


class ReadwiseDocumentList(BaseModel):
    """Схема данных для списка документов Readwise."""

    count: int
    nextPageCursor: str | None = None
    results: list[ReadwiseDocument]


class EnrichedReadwiseDocument(ReadwiseDocument):
    """
    Схема данных для обогащенного документа Readwise.
    В таком виде мы сохраняем в articles.json для фронта и скрапера.
    """

    highlights: list["EnrichedReadwiseDocument"] | None = None
    notes_attached: list["EnrichedReadwiseDocument"] | None = None
