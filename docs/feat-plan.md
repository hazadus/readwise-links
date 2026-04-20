# Read Later Triage — план реализации

## Цель

Сделать список `later` (~120–150 статей) менее "плоским": LLM анализирует каждую статью и формирует тематические подборки, которые сохраняются в Markdown и отображаются в веб-версии.

## Ключевые решения

| Вопрос | Решение |
|---|---|
| Источник полного текста | Readwise API `withHtmlContent=true` → BS4 strip |
| Список интересов | `interests.md` в корне репо, bullet points, редактируется вручную |
| Кэш-инвалидация | Только при изменении `interests.md` (hash-сравнение) |
| Анализ | 1 статья = 1 LLM-запрос |
| Модель | `openai/gpt-oss-120b:free` via OpenRouter |
| Ключи | CLI-аргументы `--api-key` и `--openrouter-key` (по аналогии с `main.py`) |
| Лимит текста | Первые 25 000 символов после BS4 strip |

## Новые файлы

| Файл | Назначение |
|---|---|
| `interests.md` | Список текущих интересов, редактируется вручную |
| `app/services/openrouter.py` | Клиент OpenRouter API |
| `app/triage.py` | Основной скрипт триажа |
| `data/triage_cache.json` | Кэш LLM-анализа, коммитится в репо |
| `data/triage.json` | Данные подборок для фронта, коммитится в репо |
| `links/triage/top.md` | Топ рекомендаций |
| `links/triage/shortest.md` | 10 самых коротких |
| `links/triage/quick-wins.md` | Быстрые победы |
| `links/triage/deep-reading.md` | Глубокое чтение |
| `links/triage/tutorials.md` | Руководства |
| `links/triage/fundamentals.md` | Основы |
| `links/triage/timely.md` | Читать сейчас |
| `docs/feat-plan.md` | Этот файл |

## Логика `triage.py`

1. Читает `interests.md` → считает MD5 hash
2. Загружает `data/triage_cache.json`
3. Если hash изменился → очищает кэш целиком
4. Фетчит все статьи `location=later` с `withHtmlContent=true`
5. Для каждой статьи **не в кэше**:
   - Извлекает текст из HTML через BeautifulSoup4, обрезает до 25 000 символов
   - Если `html_content` пустой — использует `summary` как fallback
   - Отправляет в LLM: текст статьи + список интересов из `interests.md`
   - Ждёт ответа с rate limiting (задержка между запросами)
   - При невалидном JSON от LLM — логирует ошибку, пропускает статью
   - Получает JSON-ответ, сохраняет в кэш
6. Загружает `data/articles.json` для получения `highlights`
7. Генерирует 7 подборок → записывает `links/triage/*.md` и `data/triage.json`
8. Сохраняет обновлённый `data/triage_cache.json`

## CLI-аргументы `triage.py`

| Аргумент | Обязательный | Описание |
|---|---|---|
| `--api-key` | да | Readwise API key |
| `--openrouter-key` | да | OpenRouter API key |
| `--limit N` | нет | Обрабатывать первые N статей (для отладки) |

## Структура кэша (`triage_cache.json`)

```json
{
  "interests_hash": "abc123",
  "articles": {
    "<article_id>": {
      "is_tutorial": false,
      "is_foundational": true,
      "is_evergreen": true,
      "interest_score": 8
    }
  }
}
```

## LLM-запрос на одну статью

Промпт содержит:
- Список интересов из `interests.md`
- Заголовок, `word_count`, `summary`, очищенный текст статьи (до 25 000 символов)

Ожидаемый JSON-ответ:
```json
{"is_tutorial": bool, "is_foundational": bool, "is_evergreen": bool, "interest_score": 1-10}
```

- `is_tutorial` — требует следования инструкциям за компьютером
- `is_foundational` — теория, концепции, фундаментальные вопросы (не тренды)
- `is_evergreen` — материал не устаревает (в отличие от новостей, анонсов, хайпа)
- `interest_score` — соответствие списку интересов из `interests.md`, от 1 до 10

## Подборки

Сортировка там, где не указано иное: по `interest_score` DESC, при равном — по `word_count` DESC.

| Подборка | Файл | Критерий отбора |
|---|---|---|
| Топ рекомендаций | `links/triage/top.md` | top 10 по `interest_score`, любой тип |
| 10 самых коротких | `links/triage/shortest.md` | `!is_tutorial`, `!is_foundational`, `word_count` ASC |
| Быстрые победы | `links/triage/quick-wins.md` | `!is_tutorial`, `word_count < 800`, top 10 по `interest_score` |
| Глубокое чтение | `links/triage/deep-reading.md` | `!is_tutorial`, `word_count > 1500` |
| Руководства | `links/triage/tutorials.md` | `is_tutorial = true` |
| Основы | `links/triage/fundamentals.md` | `is_foundational = true` |
| Читать сейчас | `links/triage/timely.md` | `!is_evergreen` (устаревающий контент) |

## Интеграция в пайплайн

### `archive.yml`
```yaml
- name: Run triage script
  env:
    READWISE_API_KEY: ${{ secrets.READWISE_API_KEY }}
    OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
  run: |
    uv run ./app/triage.py --api-key "$READWISE_API_KEY" --openrouter-key "$OPENROUTER_API_KEY"
```

Запускается **после** основного `main.py` (чтобы `data/articles.json` был актуален). В коммит включаются:
- `data/triage_cache.json` — кэш LLM-анализа
- `data/triage.json` — данные для фронта
- `links/triage/*.md` — все файлы подборок

Секрет `OPENROUTER_API_KEY` нужно добавить в GitHub Actions Secrets репозитория.

### Локальный запуск
```bash
uv run ./app/triage.py --api-key <READWISE_KEY> --openrouter-key <OPENROUTER_KEY>
uv run ./app/triage.py --api-key <READWISE_KEY> --openrouter-key <OPENROUTER_KEY> --limit 5
```

## Формат `data/triage.json`

```json
{
  "generated_at": "2026-04-20T03:00:00Z",
  "interests_hash": "abc123",
  "collections": {
    "top":          [ <article>, ... ],
    "shortest":     [ <article>, ... ],
    "quick_wins":   [ <article>, ... ],
    "deep_reading": [ <article>, ... ],
    "tutorials":    [ <article>, ... ],
    "fundamentals": [ <article>, ... ],
    "timely":       [ <article>, ... ]
  }
}
```

Каждый `<article>` — поля из `articles.json`, необходимые для рендера `ArticleCard.vue`, плюс блок `triage`:

```json
{
  "id": "...",
  "title": "...",
  "url": "...",
  "source_url": "...",
  "author": "...",
  "image_url": "...",
  "word_count": 1500,
  "summary": "...",
  "notes": "...",
  "tags": [{"name": "go", "created": "..."}],
  "highlights": [...],
  "saved_at": "...",
  "last_moved_at": "...",
  "published_date": "...",
  "triage": {
    "is_tutorial": false,
    "is_foundational": true,
    "is_evergreen": true,
    "interest_score": 8
  }
}
```

`highlights` подтягиваются из `data/articles.json`, сгенерированного `main.py`.

## Веб-версия

Новая страница/вкладка "Подборки" с теми же карточками `ArticleCard.vue`, сгруппированными по 7 коллекциям. Данные берутся из `data/triage.json`.

В `README.md` добавляется строка со ссылками на все подборки рядом с существующими ссылками на Markdown-отчёты:
```
- 🤖 Подборки: ⭐ [Топ](./links/triage/top.md) | ⚡ [Быстрые победы](./links/triage/quick-wins.md) | 📖 [Глубокое чтение](./links/triage/deep-reading.md) | 🛠️ [Руководства](./links/triage/tutorials.md) | 🧠 [Основы](./links/triage/fundamentals.md) | ⏳ [Читать сейчас](./links/triage/timely.md) | 📄 [Короткие](./links/triage/shortest.md)
```

## Вне скоупа (на потом)

- Анализ недавней активности для автоопределения интересов
- Скачивание статей в Markdown через Defuddle
- Отображение Markdown-контента статей через Comark
