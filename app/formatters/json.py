import json
from datetime import datetime
from typing import Any

from schemas.readwise import ReadwiseDocument


def create_json_dump(
    *,
    documents: list[ReadwiseDocument],
) -> str:
    """
    Преобразует список документов Readwise в строку в формате JSON.
    """

    def datetime_serializer(obj: Any) -> str:
        """Преобразует datetime объекты в ISO формат."""
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Тип {type(obj)} не сериализуем")

    dicts = [doc.model_dump() for doc in documents]
    return json.dumps(
        dicts,
        ensure_ascii=False,
        indent=4,
        default=datetime_serializer,
    )
