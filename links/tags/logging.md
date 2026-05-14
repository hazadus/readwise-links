# Ссылки

- Всего ссылок: 2

## Ссылки

- [Go structured logging with slog](https://rednafi.com/go/structured-logging-with-slog) [📖](https://read.readwise.io/read/01krg4ph9gm5dpy1kzwe40pj9r) 👤 Redowan Delowar 💬 1933 🔖 #go, #logging 🗓️ 2026-05-13
    > **Заметка:** Хороший вводный материал по slog
    > **Резюме:** The slog package helps create structured logs with levels like Debug, Info, Warn, and Error. It supports output in text or JSON formats and allows adding or removing custom attributes and log levels. This makes logging flexible and easy to organize for better debugging and monitoring.
- [Type-safe slogging](https://rednafi.com/go/typesafe-slogging/) [📖](https://read.readwise.io/read/01kr6xw0dzbzzdmakdyxtnkzpy) 👤 Redowan's Reflections 💬 1251 🔖 #go, #logging 🗓️ 2026-05-09
    > **Заметка:** Хорошие "продвинутые" рекомендации по использованию slog
    > **Резюме:** The author switched to Go's built-in slog for logging because it is reliable and simple despite some extra allocations. They recommend passing the logger as a dependency and using typed attribute helpers to ensure type safety and consistent keys. A tool called sloglint enforces these best practices to keep logging clear and error-free.
