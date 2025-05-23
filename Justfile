# Форматировать код с помощью black и isort
format:
    @echo "🧹 Форматирование кода..."
    uv run black app
    uv run isort app
    @echo "✅ Код отформатирован"

# Запустить скрапер
scrape:
    uv run ./app/scrape.py