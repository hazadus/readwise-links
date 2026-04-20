"""
Клиент для анализа статей через OpenRouter API.
"""

import json

import requests

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openai/gpt-oss-120b:free"

SYSTEM_PROMPT = """Ты — ассистент для анализа статей. Отвечай строго в формате JSON без каких-либо пояснений.

Проанализируй статью и верни JSON с полями:
- is_tutorial (bool): true если статья — руководство/туториал, требующее следовать инструкциям за компьютером
- is_foundational (bool): true если статья охватывает фундаментальные концепции, теорию, основы — а не хайп, новости или тренды
- is_evergreen (bool): true если содержание не устаревает со временем (в отличие от новостей, анонсов, обзоров актуальных событий)
- interest_score (int): от 1 до 10, насколько статья соответствует списку интересов пользователя

Отвечай только JSON, никакого дополнительного текста."""


def analyze_article(
    *,
    title: str,
    text: str,
    word_count: int | None,
    summary: str | None,
    interests: str,
    openrouter_key: str,
) -> dict | None:
    """
    Анализирует статью через LLM и возвращает метаданные для триажа.

    :param title: Заголовок статьи
    :param text: Очищенный текст статьи (до 25 000 символов)
    :param word_count: Количество слов в статье
    :param summary: Краткое содержание от Readwise (опционально)
    :param interests: Содержимое interests.md
    :param openrouter_key: API-ключ OpenRouter
    :return: dict с полями is_tutorial, is_foundational, is_evergreen, interest_score или None при ошибке
    """
    user_prompt = f"""Интересы пользователя:
{interests}

---

Статья для анализа:
Заголовок: {title}
Количество слов: {word_count or "неизвестно"}
Краткое содержание: {summary or "отсутствует"}

Текст:
{text}"""

    try:
        response = requests.post(
            url=OPENROUTER_API_URL,
            headers={
                "Authorization": f"Bearer {openrouter_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
            },
            timeout=60,
        )
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"    ❌ Ошибка запроса к OpenRouter: {e}")
        return None

    try:
        content = response.json()["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as e:
        print(
            f"    ❌ Неожиданная структура ответа OpenRouter: {e}. Ответ: {response.text[:300]}"
        )
        return None

    # Модель может обернуть JSON в markdown-блок ```json ... ```
    clean = content.strip()
    if clean.startswith("```"):
        lines = clean.splitlines()
        clean = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])

    try:
        result = json.loads(clean)
    except json.JSONDecodeError as e:
        print(f"    ❌ Невалидный JSON от LLM: {e}. Контент: {content[:300]}")
        return None

    required_fields = {
        "is_tutorial",
        "is_foundational",
        "is_evergreen",
        "interest_score",
    }
    if not required_fields.issubset(result.keys()):
        missing = required_fields - result.keys()
        print(f"    ❌ LLM вернул неполный JSON, отсутствуют поля: {missing}")
        return None

    return {
        "is_tutorial": bool(result["is_tutorial"]),
        "is_foundational": bool(result["is_foundational"]),
        "is_evergreen": bool(result["is_evergreen"]),
        "interest_score": int(result["interest_score"]),
    }
