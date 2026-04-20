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
from datetime import datetime, timezone
from pathlib import Path
from time import sleep

from bs4 import BeautifulSoup
from schemas.readwise import ReadwiseDocument
from services.openrouter import analyze_article
from services.readwise import fetch_reader_document_list_api

# Пути относительно корня проекта
ROOT_DIR = Path(__file__).parent.parent
INTERESTS_FILE = ROOT_DIR / "interests.md"
CACHE_FILE = ROOT_DIR / "data" / "triage_cache.json"
TRIAGE_JSON = ROOT_DIR / "data" / "triage.json"
ARTICLES_JSON = ROOT_DIR / "web" / "src" / "assets" / "articles.json"
TRIAGE_DIR = ROOT_DIR / "links" / "triage"

TEXT_LIMIT = 25_000
OPENROUTER_RATE_LIMIT_DELAY = 2  # секунды между запросами к OpenRouter

# Описания подборок: (заголовок, описание критерия)
COLLECTION_META = {
    "top": ("⭐ Топ рекомендаций", "10 статей с наивысшим interest_score"),
    "shortest": (
        "📄 10 самых коротких",
        "Короткие статьи (не туториалы, не основы), отсортированные по объёму",
    ),
    "quick_wins": (
        "⚡ Быстрые победы",
        "Короткие интересные статьи (до 800 слов), не туториалы",
    ),
    "deep_reading": (
        "📖 Глубокое чтение",
        "Длинные статьи (от 1500 слов), не туториалы",
    ),
    "tutorials": ("🛠️ Руководства", "Туториалы и практические руководства"),
    "fundamentals": ("🧠 Основы", "Фундаментальные материалы с долгосрочной ценностью"),
    "timely": ("⏳ Читать сейчас", "Актуальный контент, который может устареть"),
}


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


def build_collections(
    articles: list[ReadwiseDocument],
    cache: dict,
) -> dict[str, list[tuple[ReadwiseDocument, dict]]]:
    """
    Формирует 7 подборок из статей с учётом LLM-оценок из кэша.
    Возвращает dict: ключ подборки → список (статья, triage_data).
    """
    # Объединяем статьи с их оценками из кэша
    enriched = []
    for article in articles:
        triage = cache["articles"].get(article.id)
        if triage is None:
            continue  # статья ещё не проанализирована
        enriched.append((article, triage))

    def score_sort(pair: tuple) -> tuple:
        """Сортировка по interest_score DESC, затем word_count DESC."""
        _, t = pair
        a, _ = pair
        return (-t["interest_score"], -(a.word_count or 0))

    top = sorted(enriched, key=score_sort)[:20]

    shortest = sorted(
        [
            (a, t)
            for a, t in enriched
            if not t["is_tutorial"] and not t["is_foundational"]
        ],
        key=lambda p: (p[0].word_count or 999999),
    )[:30]

    quick_wins = sorted(
        [
            (a, t)
            for a, t in enriched
            if not t["is_tutorial"] and (a.word_count or 0) < 800
        ],
        key=score_sort,
    )[:10]

    deep_reading = sorted(
        [
            (a, t)
            for a, t in enriched
            if not t["is_tutorial"] and (a.word_count or 0) > 1500
        ],
        key=score_sort,
    )

    tutorials = sorted(
        [(a, t) for a, t in enriched if t["is_tutorial"]],
        key=score_sort,
    )

    fundamentals = sorted(
        [(a, t) for a, t in enriched if t["is_foundational"]],
        key=score_sort,
    )

    timely = sorted(
        [(a, t) for a, t in enriched if not t["is_evergreen"]],
        key=score_sort,
    )

    return {
        "top": top,
        "shortest": shortest,
        "quick_wins": quick_wins,
        "deep_reading": deep_reading,
        "tutorials": tutorials,
        "fundamentals": fundamentals,
        "timely": timely,
    }


def format_article_md(article: ReadwiseDocument, triage: dict) -> str:
    """Форматирует одну статью в строку Markdown с пометками триажа."""
    source_url = article.source_url or article.url
    reader_url = article.url
    title = article.title or "(без заголовка)"
    author = f" 👤 {article.author}" if article.author else ""
    word_count = f" 💬 {article.word_count}" if article.word_count else ""
    score = f" ⭐ {triage['interest_score']}"
    saved_at = article.saved_at.strftime(" 🗓️ %Y-%m-%d") if article.saved_at else ""
    reader_link = f" [📖]({reader_url})" if reader_url != source_url else ""

    tags_text = ""
    if article.tags:
        tags = [f"#{tag}" for tag in article.tags]
        tags_text = " 🔖 " + ", ".join(tags)

    flags = []
    if triage["is_tutorial"]:
        flags.append("🛠️ туториал")
    if triage["is_foundational"]:
        flags.append("🧠 основы")
    if triage["is_evergreen"]:
        flags.append("🌲 вечнозелёное")
    flags_text = (" · " + ", ".join(flags)) if flags else ""

    line = f"- [{title}]({source_url}){reader_link}{author}{word_count}{score}{tags_text}{saved_at}{flags_text}\n"

    if article.notes:
        line += f"    > **Заметка:** {article.notes}\n"
    if article.summary:
        line += f"    > **Резюме:** {article.summary}\n"

    return line


def write_markdown_reports(
    collections: dict[str, list[tuple[ReadwiseDocument, dict]]],
    generated_at: datetime,
) -> None:
    """Записывает 7 Markdown-файлов подборок в links/triage/."""
    TRIAGE_DIR.mkdir(parents=True, exist_ok=True)
    date_str = generated_at.strftime("%Y-%m-%d %H:%M UTC")

    filenames = {
        "top": "top.md",
        "shortest": "shortest.md",
        "quick_wins": "quick-wins.md",
        "deep_reading": "deep-reading.md",
        "tutorials": "tutorials.md",
        "fundamentals": "fundamentals.md",
        "timely": "timely.md",
    }

    for key, pairs in collections.items():
        title, description = COLLECTION_META[key]
        filename = filenames[key]
        path = TRIAGE_DIR / filename

        content = f"# {title}\n\n"
        content += f"_{description}_\n\n"
        content += f"Сгенерировано: {date_str} · Статей: {len(pairs)}\n\n"

        if pairs:
            content += "## Статьи\n\n"
            for article, triage in pairs:
                content += format_article_md(article, triage)
        else:
            content += "_Нет статей, удовлетворяющих критериям._\n"

        path.write_text(content, encoding="utf-8")
        print(f"   📝 {filename}: {len(pairs)} статей")


def load_articles_lookup() -> dict[str, dict]:
    """Загружает articles.json и возвращает dict id → enriched_article."""
    if not ARTICLES_JSON.exists():
        print(f"⚠️  {ARTICLES_JSON} не найден, highlights не будут включены.")
        return {}
    try:
        articles = json.loads(ARTICLES_JSON.read_text(encoding="utf-8"))
        return {a["id"]: a for a in articles}
    except (json.JSONDecodeError, KeyError, OSError) as e:
        print(f"⚠️  Не удалось загрузить articles.json: {e}")
        return {}


def build_article_json(
    article: ReadwiseDocument,
    triage: dict,
    enriched: dict,
) -> dict:
    """Собирает объект статьи для triage.json: поля для ArticleCard + блок triage."""
    return {
        "id": article.id,
        "url": article.url,
        "source_url": article.source_url,
        "title": article.title,
        "author": article.author,
        "image_url": article.image_url,
        "word_count": article.word_count,
        "summary": article.summary,
        "notes": article.notes,
        "tags": article.tags,
        "highlights": enriched.get("highlights") or [],
        "saved_at": article.saved_at.isoformat() if article.saved_at else None,
        "last_moved_at": (
            article.last_moved_at.isoformat() if article.last_moved_at else None
        ),
        "published_date": article.published_date,
        "triage": triage,
    }


def write_triage_json(
    collections: dict[str, list[tuple[ReadwiseDocument, dict]]],
    interests_hash: str,
    generated_at: datetime,
) -> None:
    """Записывает data/triage.json для фронтенда."""
    print(f"\n💾 Загружаю articles.json для обогащения highlights...")
    lookup = load_articles_lookup()
    print(f"   Загружено {len(lookup)} статей из articles.json.")

    result: dict = {
        "generated_at": generated_at.isoformat(),
        "interests_hash": interests_hash,
        "collections": {},
    }

    for key, pairs in collections.items():
        result["collections"][key] = [
            build_article_json(article, triage, lookup.get(article.id, {}))
            for article, triage in pairs
        ]

    TRIAGE_JSON.parent.mkdir(parents=True, exist_ok=True)
    TRIAGE_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    total = sum(len(v) for v in result["collections"].values())
    print(f"   ✅ Сохранено → {TRIAGE_JSON} ({total} позиций в коллекциях).")


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
        f"\n🤖 Нужно проанализировать: {len(to_analyze)} статей "
        f"(пропущено из кэша: {skipped})."
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
        f"\n✅ Анализ завершён. Проанализировано: {analyzed_ok}, ошибок: {analyzed_err}, "
        f"из кэша: {skipped}, всего в кэше: {len(cache['articles'])}."
    )

    # Формируем подборки и записываем отчёты
    generated_at = datetime.now(tz=timezone.utc)
    collections = build_collections(articles, cache)

    print("\n📂 Генерирую Markdown-отчёты...")
    write_markdown_reports(collections, generated_at)

    write_triage_json(collections, interests_hash, generated_at)

    total_in_collections = sum(len(v) for v in collections.values())
    print(
        f"\n🎉 Готово! Подборки сохранены в {TRIAGE_DIR}/ и {TRIAGE_JSON} "
        f"(всего позиций: {total_in_collections})."
    )


if __name__ == "__main__":
    main()
