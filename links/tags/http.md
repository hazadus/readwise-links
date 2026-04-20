# Ссылки

- Всего ссылок: 7

## Ссылки

- [Your URL Is Your State](https://alfy.blog/2025/10/31/your-url-is-your-state.html?utm_source=tldrwebdev) [📖](https://read.readwise.io/read/01k96xs212gt7sr6e5eqdxsmp9) 👤 Ahmad Elalfy 💬 2340 🔖 #http, #webdev 🗓️ 2025-11-04
    > **Резюме:** URLs can and should hold app state so pages are shareable, bookmarkable, and restorable.  
Good URL design makes intent, context, and caching explicit.  
Put public, meaningful state in the URL and keep sensitive or transient state out.
- [A complete guide to HTTP caching](https://www.jonoalderson.com/performance/http-caching/) [📖](https://read.readwise.io/read/01k768f0z3jdey8hn7q78h7zpc) 👤 Jono Alderson 💬 9131 🔖 #http 🗓️ 2025-10-10
    > **Резюме:** Caching is a layered ecosystem (browsers, CDNs, proxies, apps) that speeds the web but is often misunderstood.  
HTTP headers like Cache-Control, ETag, and Age guide caching, but intermediaries and browsers add their own rules and heuristics.  
A clear caching strategy balances freshness vs. performance to make sites faster, cheaper, and more reliable.
- [HTTP is not simple](https://daniel.haxx.se/blog/2025/08/08/http-is-not-simple/) [📖](https://read.readwise.io/read/01k258310nhrbaah4hmv625swh) 👤 August 8 💬 1561 🔖 #http, #toot, #network, #programming 🗓️ 2025-08-08
    > **Заметка:** Мейнтейнер curl рассказывет о трудностях реализации HTTP
    > **Резюме:** HTTP looks simple but is actually very complex, especially when fully implemented. The protocol has many tricky details, extra features, and evolving standards that make it hard to get right. Over time, HTTP has grown more complicated and will likely become even more so in the future.
- [The HTTP crash course nobody asked for](https://fasterthanli.me/articles/the-http-crash-course-nobody-asked-for) [📖](https://read.readwise.io/read/01jg6b5zj5cjzpznyw33z6ff2n) 👤 Amos Wenger 💬 17233 🔖 #http 🗓️ 2024-12-28
    > **Резюме:** HTTP requests are sent over TCP connections, allowing multiple requests on the same connection in HTTP/1.1. Servers often respond with error codes like 431 or 400 if they receive problematic requests. HTTP/2 improves error handling by allowing servers to send errors separately from the main response.
- [Пишем свой веб-сервер на Python: протокол HTTP](https://iximiuz.com/ru/posts/writing-python-web-server-part-3/) [📖](https://read.readwise.io/read/01jbyg6rva858a4rs7kya4dq4m) 👤 Ivan Velichko 💬 3836 🔖 #diy, #http 🗓️ 2024-02-20
    > **Резюме:** В статье рассматривается пошаговая реализация простого HTTP/1.1 сервера на Python
- [Пишем свой веб-сервер на Python](https://iximiuz.com/ru/series/writing-python-web-server-ru/) [📖](https://read.readwise.io/read/01jbyg6rtajsksg2gbx9fepvwf) 👤 Ivan Velichko 💬 94 🔖 #diy, #http 🗓️ 2024-02-20
    > **Резюме:** Серия статей о том, как написать свой веб-сервер на Python с самого нуля. Как компьютеры передают данные по сети? Что такое сокеты и для чего они нужны? Какие модели обработки запросов существуют, в чем их плюсы и минусы? Что такое протокол HTTP и для чего он нужен? Ответы на эти и многие другие вопросы эта серия даст тебе.
- [Пишем свой веб-сервер на Python: процессы, потоки и асинхронный I/O](https://iximiuz.com/ru/posts/writing-python-web-server-part-2/) [📖](https://read.readwise.io/read/01jbyg6r2btcs1167fw5e75geq) 👤 Ivan Velichko 💬 2513 🔖 #diy, #http 🗓️ 2024-02-29
    > **Резюме:** Статья сравнивает три подхода к обработке запросов: процессы, потоки и асинхронный I/O.  
Процессы изолируют ошибки, но дороги по ресурсам; потоки легче, но требуют потокобезопасности.  
Асинхронный I/O на одном потоке лучше масштабируется для большого числа ожиданий, но сложнее в оформлении кода.
