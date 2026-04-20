"""
Скрипт триажа списка "Later" из Readwise.

Анализирует каждую статью через LLM и формирует тематические подборки,
которые сохраняются в Markdown-файлы и data/triage.json для фронта.

Пример использования:
    uv run ./app/triage.py --api-key <READWISE_KEY> --openrouter-key <OPENROUTER_KEY>
    uv run ./app/triage.py --api-key <READWISE_KEY> --openrouter-key <OPENROUTER_KEY> --limit 5
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path
from time import sleep

from bs4 import BeautifulSoup
from services.openrouter import analyze_article
from services.readwise import fetch_reader_document_list_api

# Пути относительно корня проекта
ROOT_DIR = Path(__file__).parent.parent
INTERESTS_FILE = ROOT_DIR / "interests.md"
CACHE_FILE = ROOT_DIR / "data" / "triage_cache.json"

TEXT_LIMIT = 25_000
OPENROUTER_RATE_LIMIT_DELAY = 2  # секунды между запросами к OpenRouter


def load_interests() -> tuple[str, str]:
    """Возвращает (содержимое interests.md, MD5-хэш содержимого)."""
    if not INTERESTS_FILE.exists():
        print(f"❌ Файл интересов не найден: {INTERESTS_FILE}")
        sys.exit(1)
    text = INTERESTS_FILE.read_text(encoding="utf-8")
    md5 = hashlib.md5(text.encode()).hexdigest()
    return text, md5


def load_cache() -> dict:
    """Загружает кэш триажа или возвращает пустую структуру."""
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            print(f"⚠️  Не удалось прочитать кэш, создаю новый: {e}")
    return {"interests_hash": "", "articles": {}}


def save_cache(cache: dict) -> None:
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def extract_text(html_content: str | None, summary: str | None) -> str:
    """Извлекает чистый текст из HTML, fallback на summary."""
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        text = soup.get_text(separator=" ", strip=True)
        return text[:TEXT_LIMIT]
    if summary:
        return summary[:TEXT_LIMIT]
    return ""


def main():
    parser = argparse.ArgumentParser(description="Триаж списка Later из Readwise")
    parser.add_argument("--api-key", required=True, help="Readwise API ключ")
    parser.add_argument("--openrouter-key", required=True, help="OpenRouter API ключ")
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Максимальное количество статей для анализа (для отладки)",
    )
    args = parser.parse_args()

    print("🔍 Загружаю список интересов...")
    interests, interests_hash = load_interests()
    print(f"   MD5 интересов: {interests_hash}")

    print("📦 Загружаю кэш триажа...")
    cache = load_cache()

    if cache.get("interests_hash") != interests_hash:
        print("🔄 Список интересов изменился — сбрасываю кэш.")
        cache = {"interests_hash": interests_hash, "articles": {}}
    else:
        cached_count = len(cache.get("articles", {}))
        print(f"   В кэше: {cached_count} статей.")

    print("\n📥 Получаю статьи из Readwise (location=later)...")
    articles = fetch_reader_document_list_api(
        token=args.api_key,
        location="later",
        with_html_content=True,
    )
    print(f"   Получено: {len(articles)} статей.")

    # Статьи для анализа (не в кэше)
    to_analyze = [a for a in articles if a.id not in cache["articles"]]

    if args.limit is not None:
        to_analyze = to_analyze[: args.limit]
        print(f"\n⚡ Режим отладки: анализирую не более {args.limit} статей.")

    skipped = len(articles) - len(to_analyze)
    print(
        f"\n🤖 Нужно проанализировать: {len(to_analyze)} статей (пропущено из кэша: {skipped})."
    )

    analyzed_ok = 0
    analyzed_err = 0

    for i, article in enumerate(to_analyze, 1):
        title = article.title or "(без заголовка)"
        print(f"\n[{i}/{len(to_analyze)}] {title[:80]}")
        print(f"   word_count={article.word_count}, id={article.id}")

        text = extract_text(article.html_content, article.summary)
        if not text:
            print("   ⚠️  Нет текста для анализа, пропускаю.")
            analyzed_err += 1
            continue

        source = "html_content" if article.html_content else "summary (fallback)"
        print(f"   📄 Текст: {len(text)} символов (источник: {source})")

        result = analyze_article(
            title=title,
            text=text,
            word_count=article.word_count,
            summary=article.summary,
            interests=interests,
            openrouter_key=args.openrouter_key,
        )

        if result is None:
            print("   ❌ Анализ не удался, пропускаю статью.")
            analyzed_err += 1
        else:
            cache["articles"][article.id] = result
            cache["interests_hash"] = interests_hash
            print(
                f"   ✅ is_tutorial={result['is_tutorial']}, "
                f"is_foundational={result['is_foundational']}, "
                f"is_evergreen={result['is_evergreen']}, "
                f"interest_score={result['interest_score']}"
            )
            analyzed_ok += 1
            # Сохраняем кэш после каждой статьи — не теряем прогресс при прерывании
            save_cache(cache)

        if i < len(to_analyze):
            sleep(OPENROUTER_RATE_LIMIT_DELAY)

    print(f"\n💾 Сохраняю кэш → {CACHE_FILE}")
    save_cache(cache)

    print(
        f"\n✅ Готово. Проанализировано: {analyzed_ok}, ошибок: {analyzed_err}, "
        f"из кэша: {skipped}, всего в кэше: {len(cache['articles'])}."
    )


if __name__ == "__main__":
    main()
