# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Does

**Readwise Links** is a personal link archiving system. A GitHub Actions workflow runs daily to:
1. Fetch links from Readwise Reader API → generate Markdown reports and `data/articles.json`
2. Trigger a deploy workflow → build a Vue.js frontend → publish to GitHub Pages

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
  → web/npm run build    — bundle Vue app with updated data/articles.json as asset
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

### Generated data files

- `links/` — Markdown reports by location + `links/tags/` by tag
- `data/articles.json` — full JSON dump consumed by the frontend
- `data/toots.json` / `data/skeets.json` — published post tracking

### Vue.js frontend (`/web/src`)

- **Views**: `Home.vue` (main listing), `About.vue`
- **Components**: `ArticleCard.vue`, `TagFilter.vue`, `Header.vue`, `Tag.vue`
- **Router**: `router/index.ts`
- **Types**: `src/types/`
- **Utils**: `src/utils/markdown.ts` — Markdown parsing helpers
- The build copies `data/articles.json` into `src/assets/articles.json` for Vite to bundle

### CI/CD (`.github/workflows/`)

- `archive.yml` — daily Python run; commits updated `links/` and `data/`
- `deploy.yml` — builds and deploys Vue app to GitHub Pages
- `toot.yml` / `skeet.yml` — social publishing workflows

## Key Tech

- **Python 3.12+**, Pydantic v2, `uv`, `httpx` (async scraper), `requests` (API), BeautifulSoup4, Jinja2
- **Vue 3.5**, TypeScript 5.6, Vite 6, Tailwind CSS 3.4, Vue Router 4, VueUse
