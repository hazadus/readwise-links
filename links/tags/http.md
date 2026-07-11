# Ссылки

- Всего ссылок: 10

## Ссылки

- [Tracing HTTP Requests with Rust](https://blainsmith.com/articles/tracing-http-requests-with-rust/) [📖](https://read.readwise.io/read/01kwm62v3vkwd2f5y0mscd3c63) 👤 Unknown 💬 1306 🔖 #http, #rust 🗓️ 2026-07-03
    > **Резюме:** Recently, I wrote about using Go's net/http/httptrace to get the per-phase timing breakdown for HTTP requests - DNS, TCP, TLS, and server processing. After writing about that package, I wanted to know what the same breakdown costs in Rust: whether the ecosystem has an equivalent, and what building one reveals about how the two languages approach instrumentation.
The short answer is there's no equivalent. reqwest doesn't expose per-phase timestamps. hyper's client is a Tower Service, not a single blessed HTTP client with hook points. Getting DNS/TCP/TLS granularity means working at the connector level directly. So I built httptrace, a small crate that does for Rust what net/http/httptrace does for Go, and this is a walkthrough of what building it involved.
No Context to Piggyback On
Go's httptrace works by riding on context.Context. You build a *ClientTrace, attach it to a context with httptrace.WithClientTrace, and http.Transport pulls it back out at each phase via httptrace.ContextClientTrace. The trace travels with the request. Any middleware that forwards the context propagates tracing without knowing tracing exists.
Rust has nothing that plays the same role. There's no ambient value that flows through an async call graph the way context.Context does through Go's. tracing's spans get closest, but they're an observability mechanism, not a request-scoped value you can staple typed callbacks to and expect the transport to invoke. So httptrace in Rust has to take the trace as an explicit argument, not pull it from somewhere implicit. That single constraint shapes the rest of the design: instead of one universal hook point, the crate exposes two separate entry points depending on whether you want a single traced request or a reusable connector, and you pass a ClientTrace into whichever one you're using.
pub struct ClientTrace {
    pub(crate) dns_start: Callback<DnsStartInfo>,
    pub(crate) dns_done: Callback<DnsDoneInfo>,
    pub(crate) connect_start: Callback<Co...
- [RFC 10008: The HTTP QUERY Method](https://blainsmith.com/articles/rfc-10008-http-query-method/) [📖](https://read.readwise.io/read/01kvbq0ck6h3f4hammnkvqm6dj) 👤 Unknown 💬 404 🔖 #go, #http, #rust 🗓️ 2026-06-17
    > **Резюме:** RFC 10008 was published on June 15, 2026 and defines a new HTTP method: QUERY. It fills a gap that has existed for as long as I have been building APIs. You have data to send to the server in order to describe what you want back, but GET does not have a body and POST is neither safe nor idempotent. QUERY gives you a method that accepts a request body while remaining safe, idempotent, and cacheable.
If you have ever built an SDK that talks to a JSON-RPC API you have felt this pain. JSON-RPC by design sends a JSON payload describing the method and parameters. That payload has to go in the body, which means POST, which means caches and intermediaries treat every request as a state-changing operation. Retry logic gets complicated. CDN caching is off the table. You end up building your own application-level caching because HTTP's built-in mechanisms cannot help you.
QUERY changes that. The semantics are simple: send a body, get a response, and the whole exchange is treated like a GET from the perspective of caching and safety.
In Go
Go's net/http already lets you use arbitrary method strings with http.NewRequest, so SDK code using QUERY looks about like you would expect:
body, _ := json.Marshal(map[string]any{
	"jsonrpc": "2.0",
	"method":  "getScore",
	"params":  []any{"0xABC123", "latest"},
	"id":      1,
})

req, _ := http.NewRequestWithContext(ctx, "QUERY", "https://rpc.example.com", bytes.NewReader(body))
req.Header.Set("Content-Type", "application/json")

resp, _ := http.DefaultClient.Do(req)
No new dependencies needed. The standard library handles it because HTTP methods are just strings.
In Rust
With reqwest you can use reqwest::Method to define a custom method:
use reqwest::{Client, Method};

let client = Client::new();
let query_method = Method::from_bytes(b"QUERY").unwrap();

let resp = client
    .request(query_method, "https://rpc.example.com")
    .header("Content-Type", "application/json")
    .body(r#"{"jsonrpc":"2.0","method":"getScore","params":["0xA...
- [Tracing HTTP Requests with Go's net/http/httptrace](https://blainsmith.com/articles/httptrace-with-go/) [📖](https://read.readwise.io/read/01ksn5nf0pxys92m3e633sspsn) 👤 Unknown 💬 1369 🔖 #go, #http 🗓️ 2026-05-27
    > **Заметка:** Хороший разбор httptrace. Может пригодиться для аналитики при разработке веб-приложений.
    > **Резюме:** net/http/httptrace has been in the standard library since Go 1.7 and most Go developers I talk to have never used it. It exposes hooks for the points in an outgoing HTTP request that you usually cannot see from outside the transport: DNS resolution, connection acquisition, TLS handshake, the moment bytes go on the wire, the moment the first response byte comes back.
The interesting part is how it plugs in. There is no Tracer interface on http.Client, no middleware to register. You attach a ClientTrace to a context.Context and the transport pulls it back out via httptrace.ContextClientTrace at the points where it matters. I want to walk through that design choice first because it explains how the package composes with the rest of the stdlib, then build two things with it: a curl --trace-style CLI and a reusable http.RoundTripper that logs timings for every request.
Why Context, Not an Interface
The obvious design for request tracing would be to define a Tracer interface, add a Tracer field to http.Client or http.Transport, and call methods on it from inside the transport. That is roughly how most languages handle this.
Go's standard library does not work that way. Instead, httptrace.WithClientTrace returns a new context carrying a *ClientTrace, you attach that context to your request with req.WithContext(ctx), and the transport pulls the trace back out via httptrace.ContextClientTrace at the points where it matters.
trace := &httptrace.ClientTrace{
    DNSStart: func(info httptrace.DNSStartInfo) {
        fmt.Printf("DNS start: %s\n", info.Host)
    },
    DNSDone: func(info httptrace.DNSDoneInfo) {
        fmt.Printf("DNS done: %v\n", info.Addrs)
    },
}

ctx := httptrace.WithClientTrace(context.Background(), trace)
req, _ := http.NewRequestWithContext(ctx, http.MethodGet, "https://example.com", nil)
http.DefaultClient.Do(req)
This is unusual but it pays off. The trace travels with the request, so any middleware that forwards the context propagates tracing for f...
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
