# Read Later Triage — план реализации по шагам

Каждый шаг коммитится отдельно и оставляет проект в рабочем состоянии.

**Сквозное требование:** на всех шагах скрипт должен выводить подробный прогресс в консоль — что делается, сколько статей обработано, какие пропущены (из кэша), ошибки LLM, итоговая статистика по каждой подборке.

---

- [x] **1. `interests.md` — файл текущих интересов**

  Создать `interests.md` в корне репо с bullet-point списком интересов.

  _Приёмка:_ `cat interests.md` показывает список интересов; файл удобно редактировать вручную.

---

- [x] **2. OpenRouter-клиент (`app/services/openrouter.py`)**

  Реализовать функцию `analyze_article(text, interests, openrouter_key) -> dict`, которая:
  - отправляет POST-запрос к OpenRouter API (модель `google/gemini-2.5-pro-exp-03-25:free`)
  - возвращает распарсенный JSON `{is_tutorial, is_foundational, is_evergreen, interest_score}`
  - при невалидном JSON логирует ошибку и возвращает `None`

  _Приёмка:_ запустить вручную небольшой тестовый скрипт или `python -c "from services.openrouter import analyze_article; print('ok')"` без ошибок импорта.

---

- [x] **3. `triage.py` — скелет CLI + анализ + кэш**

  Реализовать `app/triage.py` с аргументами `--api-key`, `--openrouter-key`, `--limit`:
  - читает `interests.md`, считает MD5 hash
  - загружает/инвалидирует `data/triage_cache.json`
  - фетчит статьи `location=later` с `withHtmlContent=true`
  - для каждой статьи не в кэше: BS4 strip → обрезка до 25 000 символов → LLM → запись в кэш
  - fallback на `summary` если `html_content` пустой
  - rate limiting между запросами к OpenRouter
  - сохраняет обновлённый `data/triage_cache.json`

  _Приёмка:_
  ```bash
  uv run ./app/triage.py --api-key <KEY> --openrouter-key <KEY> --limit 3
  ```
  Выполняется без ошибок; `data/triage_cache.json` содержит ровно 3 проанализированные статьи с полями `is_tutorial`, `is_foundational`, `is_evergreen`, `interest_score`.

---

- [x] **4. Генерация Markdown-отчётов (`links/triage/*.md`)**

  Добавить в `triage.py` генерацию 7 файлов подборок согласно критериям из плана.
  Каждый файл содержит заголовок подборки, дату генерации и список статей в формате,
  аналогичном существующим отчётам в `links/`.

  _Приёмка:_
  ```bash
  uv run ./app/triage.py --api-key <KEY> --openrouter-key <KEY> --limit 10
  ```
  В `links/triage/` появляются 7 `.md`-файлов с непустыми списками статей (где критерии позволяют).
  Сортировка: `interest_score` DESC, при равном — `word_count` DESC (кроме `shortest.md` — по `word_count` ASC).

---

- [x] **5. Генерация `data/triage.json`**

  Добавить в `triage.py` генерацию `data/triage.json`:
  - загружает `data/articles.json` для обогащения статей `highlights`
  - собирает коллекции по тем же критериям, что и Markdown-отчёты
  - сохраняет в формате, описанном в `docs/feat-plan.md`

  _Приёмка:_
  ```bash
  uv run ./app/triage.py --api-key <KEY> --openrouter-key <KEY> --limit 10
  ```
  `data/triage.json` содержит корректный JSON с ключами `generated_at`, `interests_hash`, `collections`;
  каждая статья в коллекции имеет блок `triage` и поле `highlights`.

---

- [x] **6. Интеграция в CI (`archive.yml` + GitHub Secret)**

  - Добавить шаг запуска `triage.py` после `main.py` в `.github/workflows/archive.yml`
  - Добавить `OPENROUTER_API_KEY` в список коммитируемых файлов (`git add`)
  - Добавить секрет `OPENROUTER_API_KEY` в GitHub Actions Secrets репозитория вручную

  _Приёмка:_ запустить workflow вручную через GitHub Actions (`workflow_dispatch`);
  в коммите появляются обновлённые `data/triage_cache.json`, `data/triage.json`, `links/triage/*.md`.

---

- [x] **7. Обновление `README.md`**

  Добавить строку с ссылками на подборки рядом с существующими ссылками на Markdown-отчёты:
  ```
  - 🤖 Подборки: ⭐ [Топ](./links/triage/top.md) | ⚡ [Быстрые победы](./links/triage/quick-wins.md) | 📖 [Глубокое чтение](./links/triage/deep-reading.md) | 🛠️ [Руководства](./links/triage/tutorials.md) | 🧠 [Основы](./links/triage/fundamentals.md) | ⏳ [Читать сейчас](./links/triage/timely.md) | 📄 [Короткие](./links/triage/shortest.md)
  ```

  _Приёмка:_ ссылки открываются корректно после того, как шаг 4 сгенерировал файлы.

---

- [x] **8. Фронтенд: страница "Подборки"**

  - Новый роут `/triage` в `web/src/router/index.ts`
  - Новый вью `web/src/views/Triage.vue`: загружает `data/triage.json`, отображает 7 коллекций
    с заголовками, используя существующий `ArticleCard.vue`
  - В `ArticleCard.vue` рядом с заголовком добавить ссылку [📖 Reader] (`article.url`) для открытия в Readwise Reader
  - Добавить ссылку на страницу в `Header.vue`
  - Обновить `vite.config.ts` / сборку если нужно скопировать `triage.json` в `src/assets/`

  _Приёмка:_
  ```bash
  cd web && npm run dev
  ```
  Открыть `http://localhost:3000/triage` — видны 7 секций с карточками статей.
  Карточки кликабельны, теги работают, `npm run build` проходит без ошибок TypeScript.
