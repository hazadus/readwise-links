# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Does

**Readwise Links** is a personal link archiving system. A GitHub Actions workflow runs daily to:
1. Fetch links from Readwise Reader API → generate Markdown reports and `data/articles.json`
2. Analyse "Read Later" articles via LLM (OpenRouter) → generate triage collections in `links/triage/` and `data/triage.json`
3. Trigger a deploy workflow → build a Vue.js frontend → publish to GitHub Pages

Optional manual scripts publish selected links to Mastodon (`toot.py`) and Bluesky (`skeet.py`).

## Commands

### Python backend (managed by `uv`)
```bash
uv sync --all-groups --link-mode=copy   # install dependencies
uv run ./app/main.py --api-key <KEY>    # run archiving workflow
uv run ./app/scrape.py                  # download full HTML archive (slow)
uv run ./app/toot.py                    # post to Mastodon
uv run ./app/skeet.py <handle> <pass>   # post to Bluesky
just format                             # black + isort (or: uv run black app && uv run isort app)
```

### Vue.js frontend (`/web`)
```bash
npm run dev      # dev server at localhost:3000
npm run build    # TypeScript + Vite production build
npm run preview  # preview production build
```

There are no automated tests in this project.

## Architecture

```
GitHub Actions (daily 03:00 UTC)
  → app/main.py          — fetch Readwise API → write links/ and data/articles.json
  → app/triage.py        — LLM triage of "later" articles → links/triage/*.md, data/triage.json
  → web/npm run build    — bundle Vue app with updated data/articles.json + data/triage.json as assets
  → GitHub Pages deploy
```

### Python backend (`/app`)

| File/Dir | Role |
|---|---|
| `services/readwise.py` | Readwise Reader API v3 client with pagination and rate limiting |
| `schemas/readwise.py` | Pydantic v2 models for Readwise documents |
| `formatters/markdown.py` | Renders docs to Markdown grouped by location (new/later/shortlist/archive) and tags |
| `formatters/json.py` | Serializes docs to JSON (datetime handling) |
| `reports.py` | Orchestrates report generation, writes `links/*.md`, `links/tags/*.md`, `data/articles.json` |
| `main.py` | CLI entry point |
| `integrations/mastodon/` | Mastodon posting; tracks published posts in `data/toots.json` |
| `integrations/bluesky/` | Bluesky posting; tracks published posts in `data/skeets.json` |
| `scrape.py` | Async scraper: downloads full HTML pages + CSS/JS/images into a local archive |
| `triage.py` | LLM triage: fetches `location=later` articles, calls OpenRouter API, generates `links/triage/*.md` and `data/triage.json`; caches results in `data/triage_cache.json` |
| `services/openrouter.py` | OpenRouter API client; `analyze_article()` returns `{is_tutorial, is_foundational, is_evergreen, interest_score}` |
| `interests.md` | User interest list (bullet points); MD5 hash used to invalidate triage cache |

### Generated data files

- `links/` — Markdown reports by location + `links/tags/` by tag
- `links/triage/` — 7 LLM-curated collections: `top.md`, `quick-wins.md`, `deep-reading.md`, `tutorials.md`, `fundamentals.md`, `timely.md`, `shortest.md`
- `data/articles.json` — full JSON dump consumed by the frontend
- `data/triage.json` — triage collections with `triage` metadata per article; consumed by the frontend
- `data/triage_cache.json` — LLM analysis cache keyed by article ID + interests hash
- `data/toots.json` / `data/skeets.json` — published post tracking

### Vue.js frontend (`/web/src`)

- **Views**: `Triage.vue` (root `/` — LLM collections with tab switcher), `Home.vue` (`/archive` — full archive), `About.vue`
- **Components**: `ArticleCard.vue` (shows `★ N` interest score badge when `article.triage` present), `TagFilter.vue`, `Header.vue`, `Tag.vue`
- **Router**: `router/index.ts` — `/` → Triage, `/archive` → Home, `/about` → About
- **Types**: `src/types/note.d.ts` — `ReadwiseDocument`, `Article`, `TriageData`, `TriageArticle`, `TriageCollections`, `TriageJson`
- **Utils**: `src/utils/markdown.ts` — Markdown parsing helpers
- Both `data/articles.json` and `data/triage.json` are copied into `src/assets/` by CI before build

### CI/CD (`.github/workflows/`)

- `archive.yml` — daily Python run; commits updated `links/` and `data/`
- `deploy.yml` — builds and deploys Vue app to GitHub Pages
- `toot.yml` / `skeet.yml` — social publishing workflows

## GitHub CLI Notes

`gh pr edit` fails with a deprecation error due to Projects (classic). Use `gh api` to update PR descriptions:

```bash
gh api repos/hazadus/readwise-links/pulls/<NUMBER> -X PATCH -f body='...'
```

## Key Tech

- **Python 3.12+**, Pydantic v2, `uv`, `httpx` (async scraper), `requests` (API), BeautifulSoup4, Jinja2
- **Vue 3.5**, TypeScript 5.6, Vite 6, Tailwind CSS 3.4, Vue Router 4, VueUse
