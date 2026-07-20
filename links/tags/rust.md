# Ссылки

- Всего ссылок: 34

## Ссылки

- [When Rust Gets Ugly](https://corrode.dev/blog/ugly/) [📖](https://read.readwise.io/read/01kxrk96cq6hm10yree4srb9nx) 👤 Matthias Endler 💬 3726 🔖 #rust 🗓️ 2026-07-17
    > **Резюме:** Many people find Rust code ugly because they write it like other languages. Rust wants you to use its own style, focusing on clear structure and explicit error handling. When you change your habits and use Rust’s features, your code becomes cleaner and easier to read.
- [The Pulse: What can we learn from Bun’s rapid Rust rewrite with AI?](https://blog.pragmaticengineer.com/the-pulse-what-can-we-learn-from-buns-rapid-rust-rewrite-with-ai/) [📖](https://read.readwise.io/read/01kxp06edmjxctmfzq3hx1xs8g) 👤 Ivan Klaric 💬 2163 🔖 #bun, #rust 🗓️ 2026-07-16
    > **Резюме:** Jarred Sumner used AI to quickly rewrite Bun from Zig to Rust, fixing many memory bugs. The AI agents rewrote over 500,000 lines of code in just 11 days, a task that would take humans about a year. This shows AI can make large software rewrites faster and more practical than before.
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
- [Rewriting the world in Rust](https://bitfieldconsulting.com/posts/rewrite-in-rust) [📖](https://read.readwise.io/read/01kvswppy9118grz6qtn39x89d) 👤 John Arundel 💬 1976 🔖 #rust 🗓️ 2026-06-23
    > **Резюме:** Rust is a modern language that improves software security by preventing many memory and concurrency bugs. Rewriting all old code in Rust is very hard, and automatic translation does not create good Rust programs. Instead, gradually replacing parts with Rust and redesigning code step-by-step is a more practical and effective approach.
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
- [Rust Prevents Data Races, Not Race Conditions](https://corrode.dev/blog/rust-prevents-data-races-not-race-conditions/) [📖](https://read.readwise.io/read/01ktygb7nkpasjngp24cjjpts8) 👤 Matthias Endler 💬 2605 🔖 #rust 🗓️ 2026-06-12
    > **Резюме:** Rust’s safety guarantees prevent data races by ensuring memory access is properly synchronized. However, Rust does not prevent other concurrency bugs like deadlocks, livelocks, or logic errors from incorrect locking. Programmers still need to carefully manage synchronization to avoid these race conditions.
- [Patterns for Defensive Programming in Rust](https://corrode.dev/blog/defensive-programming/) [📖](https://read.readwise.io/read/01ktkknvzzgagx1vyeq1dhma9j) 👤 Corrode Rust Consulting 💬 3275 🔖 #rust 🗓️ 2026-06-08
    > **Резюме:** Defensive programming in Rust means using the compiler to enforce rules and prevent errors. You can force all struct creation to go through safe constructors by adding private fields and modules. Making fields private and providing getters helps keep data valid and avoids mistakes.
- [Why Bun leaving Zig is Great for Zig](https://dayvster.com/blog/why-bun-leaving-zig-is-great-for-zig/) [📖](https://read.readwise.io/read/01ksg52rndrdjzem1bfh9eeeqh) 👤 Dayvster 💬 976 🔖 #bun, #zig, #rust 🗓️ 2026-05-25
    > **Заметка:** Интересно! Наблюдаем за развитием событий :)
    > **Резюме:** Why Anthropics million line AI rewrite is a massive gamble for Bun, a marketing stunt for Claude, and a quiet win for Zig.
- [Migrating from Go to Rust](https://corrode.dev/learn/migration-guides/go-to-rust/) [📖](https://read.readwise.io/read/01krwwzt19d6zeem88b59z983s) 👤 Matthias Endler 💬 5536 🔖 #go, #rust 🗓️ 2026-05-18
    > **Резюме:** Go and Rust both offer strong concurrency and performance, but Rust has stricter safety checks and a more powerful type system. Rust’s generics and traits provide better code reuse and fewer runtime errors, though compile times are slower and the learning curve is steeper. Moving from Go to Rust means trading simplicity and fast builds for safety, expressiveness, and fewer runtime bugs.
- [Farewell, Rust](https://yieldcode.blog/post/farewell-rust/) [📖](https://read.readwise.io/read/01kj07tvf74q9qh4nsk12xv9yq) 👤 Dmitry Kudryavtsev 💬 2784 🔖 #rust 🗓️ 2026-02-21
    > **Резюме:** The author learned Rust and built a web app but found web development better suited to dynamic languages like Node.js. Despite Rust's strengths in safety and performance, its tooling for web features like templating and internationalization is lacking. The author will use Rust for CPU-heavy or API tasks but prefers Node.js for web projects.
- [Rust is bottom-up, Swift is top-down.](https://nmn.sh/blog/2023-10-02-swift-is-the-more-convenient-rust?utm_source=tldrdev) [📖](https://read.readwise.io/read/01kgkm3jnwpabbfxc13bbef210) 👤 nmn.sh 💬 1633 🔖 #rust, #swift 🗓️ 2026-02-04
    > **Резюме:** Rust is a low-level, fast language that starts with manual memory control and lets you build up. Swift is a high-level, easier language that starts with simple value types and lets you go lower when needed. Both share similar features, but Rust is better for systems programming, while Swift is better for apps and servers, and is now truly cross-platform.
- [Thoughts on Go vs. Rust vs. Zig](https://sinclairtarget.com/blog/2025/08/thoughts-on-go-vs.-rust-vs.-zig/) [📖](https://read.readwise.io/read/01kbpf50b7f86jf08pd9zdpq7e) 👤 sinclairtarget.com 💬 2031 🔖 #go, #zig, #rust 🗓️ 2025-12-05
    > **Резюме:** Go is minimal and stable, trading features for simplicity and readability. Rust is feature-rich and complex, aiming for safety and high performance with strict compile-time guarantees. Zig is experimental and manual, favoring explicit memory control and data-oriented design over OO patterns.
- [Are We Chasing Language Hype Over Solving Real Problems?](https://dayvster.com/blog/are-we-chasing-language-hype-over-solving-real-problems) [📖](https://read.readwise.io/read/01k6ar86z0grw7rgtnbs3hywxz) 👤 Dayvi Schuster 💬 1839 🔖 #rust 🗓️ 2025-09-29
    > **Резюме:** Many developers chase new languages and rewrite reliable tools just because they are trendy. The GNU Core Utils rewrite in Rust is a prime example that may add little value and waste effort. We should prioritize solving real problems and measurable impact over novelty.
- [On Choosing Rust](https://endler.dev/2025/choosing-rust/) [📖](https://read.readwise.io/read/01k67tmafg0beaxc6qag3njb3e) 👤 Matthias Endler 💬 1414 🔖 #rust 🗓️ 2025-09-28
    > **Резюме:** The author defends using Rust for core tools and says critics who call it hype are wrong. Rust brings memory safety, better concurrency, and can match or beat C in real cases. Rewrites are pragmatic and incremental—driven by maintainers, tooling needs, and retiring C programmers, not a coordinated plot.
- [Mac toolbar widgets with xbar and rust](https://blog.korny.info/2025/01/18/toolbar-widgets-with-xbar-and-rust) [📖](https://read.readwise.io/read/01k2khcr2bkjp459p68bgdrkmf) 👤 Korny Sietsma 💬 779 🔖 #rust, #macos, #inspiration 🗓️ 2025-08-14
    > **Заметка:** Интересная тулза для доступа к произвольным скриптам из трея
    > **Резюме:** XBar is a simple Mac tool that shows small widgets on the toolbar using scripts. The author explains how to write plugins in Rust using rust-script, which compiles and runs Rust code like a script. They also share examples, including a clock widget and a music player controller.
- [C++ to Rust Cheat-Sheet](https://corrode.dev/learn/migration-guides/cpp-to-rust/) [📖](https://read.readwise.io/read/01jvhbpdxfj91zp430eyzcw1bz) 👤 Corrode Rust Consulting 💬 869 🔖 #rust 🗓️ 2025-05-18
    > **Резюме:** The "C++ to Rust Cheat-Sheet" by Matthias Endler helps C++ developers quickly compare syntax and constructs with Rust. It includes examples for various programming features like variable declarations and function implementations. This guide is a useful reference for those transitioning from C++ to Rust.
- [Flattening Rust's Learning Curve](https://corrode.dev/blog/flattening-rusts-learning-curve/) [📖](https://read.readwise.io/read/01jtg22gba986fqvnc20d9wqhv) 👤 Corrode Rust Consulting 💬 3042 🔖 #rust 🗓️ 2025-05-05
    > **Резюме:** Learning Rust requires accepting new concepts like ownership and lifetimes. To improve, write a lot of code, listen to the compiler, and build on what you already know. Focus on long-term benefits and set realistic expectations for your progress.
- [The promise of Rust](https://fasterthanli.me/articles/the-promise-of-rust) [📖](https://read.readwise.io/read/01js19n1cd84pmrbh2wz4va3bg) 👤 Amos Wenger 💬 1154 🔖 #rust 🗓️ 2025-04-17
    > **Резюме:** Rust's unique features can be intimidating but also offer valuable lessons in memory management. It requires explicit actions, like cloning or borrowing, to handle data safely, which differs from many other programming languages. This focus on memory safety and performance is what makes Rust stand out from languages like JavaScript and Go.
- [A Year of Rust in ClickHouse](https://clickhouse.com/blog/rust) [📖](https://read.readwise.io/read/01jrrfkx0c7mebbafyweh96dh3) 👤 ClickHouse 💬 2800 🔖 #rust 🗓️ 2025-04-13
    > **Резюме:** ClickHouse is integrating Rust into its C++ codebase to allow the development of new system components. The first successful integration was the BLAKE3 hash function, followed by the PRQL library and the Delta Kernel. However, challenges arose with memory management, compatibility, and dependency management between Rust and C++.
- [Bitfield Consulting](https://bitfieldconsulting.com/posts/things-fall-apart) [📖](https://read.readwise.io/read/01jq4xh9hsqhyd1cyjtg7vbc2a) 👤 Bitfield Consulting 💬 45 🔖 #rust 🗓️ 2025-03-24
    > **Резюме:** Bitfield Consulting offers mentoring for Go and Rust programming languages. You can join their Code Club to receive free learning resources and special offers. Unsubscribing from the mailing list is easy and can be done at any time.
- [Rust vs. Go: A Tale of Two Systems Languages](https://smsk.dev/2025/03/16/rust-vs-go-a-tale-of-two-systems-languages/) [📖](https://read.readwise.io/read/01jphv1d48jzc2tdkw074fs1cb) 👤 devsimsek 💬 638 🔖 #go, #rust 🗓️ 2025-03-17
    > **Резюме:** The author compares Rust and Go, two popular systems programming languages, highlighting their different learning curves and performance characteristics. Go is easier to learn and great for quickly building web services, while Rust offers more control over memory and performance but has a steeper learning curve. Ultimately, the choice between them depends on your specific needs and goals as a programmer.
- [Rust Learning Resources 2025](https://corrode.dev/blog/rust-learning-resources-2025/) [📖](https://read.readwise.io/read/01jnqargm4k4gqfmyfd532kyqq) 👤 Corrode Rust Consulting 💬 970 🔖 #rust 🗓️ 2025-03-07
    > **Резюме:** The author, Matthias Endler, shares a list of Rust learning resources for 2025, emphasizing hands-on experiences and up-to-date content. Resources include Rustlings, Rustfinity, 100 Exercises To Learn Rust, and CodeCrafters, catering to all skill levels. Workshops are also available for personalized learning and practical project completion.
- [Bitfield Consulting](https://bitfieldconsulting.com/posts/writing-terrible-code) [📖](https://read.readwise.io/read/01jn4acatkfea70zewjd92de1r) 👤 Bitfield Consulting 💬 13 🔖 #rust 🗓️ 2025-02-27
    > **Резюме:** The secret of being a great coder is to write terrible code. Wait, wait. Hear me out: I’m going somewhere with this.
- [Seeking Purity](http://lucumr.pocoo.org/2025/2/8/seeking-purity) [📖](https://read.readwise.io/read/01jkkfqwjnjqfatr3mbstf2etd) 👤 Armin Ronacher's Thoughts and Writings 💬 1475 🔖 #rust 🗓️ 2025-02-08
    > **Резюме:** Armin Ronacher discusses the idea of "purity" in technology, focusing on Rust's strong emphasis on memory safety. He compares this to past experiences with Python's transition from version 2 to 3, highlighting the tensions that arise when strict principles clash with practical realities. Ronacher argues that a balanced, pragmatic approach is necessary for progress, as pushing for purity can create friction and resistance in established communities.
- [Fat Rand: How Many Lines Do You Need To Generate A Random Number?](http://lucumr.pocoo.org/2025/2/4/fat-rand) [📖](https://read.readwise.io/read/01jkagnjdshyh0wvdjendgb753) 👤 Armin Ronacher's Thoughts and Writings 💬 1268 🔖 #rust 🗓️ 2025-02-05
    > **Резюме:** The author discusses the dependency issues related to the Rust crate "rand," which is used for generating random numbers. They highlight how the dependency tree has grown significantly, raising concerns about the number of lines of code and compile times. The author suggests that Rust's standard library may need to include more features to reduce reliance on external crates like rand.
- [Rust vs Zig Showdown (HTMX Webapp)](https://www.youtube.com/watch?v=hWaaG9sN_Z8) [📖](https://read.readwise.io/read/01jjgyn48psmx9c1b41e1353tb) 👤 Code to the Moon 🔖 #rust 🗓️ 2025-01-26
    > **Резюме:** The video compares Rust and Zig programming languages in building a web app using HTMX. It explains how user data is handled with locks for reading and writing, ensuring safe data management. The discussion highlights the similarities and differences in memory allocation and API implementation between the two languages.
- [Error Handling No-Goes In Go](https://brainbaking.com/post/2024/03/error-handling-no-goes-in-go/) [📖](https://read.readwise.io/read/01jj2rr8m6dbfp7frynek09vq4) 👤 Brain Baking 💬 878 🔖 #go, #rust 🗓️ 2025-01-20
    > **Заметка:** Автор в очередной раз критикует паттерны обработки ошибок в Go, и хвалит оные в Rust.
    > **Резюме:** The text discusses the challenges of error handling in Go code and compares it to Java and Rust. It highlights the readability and elegance of Rust's error handling approach using Result<T, E> enums. The author expresses a desire to learn Rust due to its superior error handling compared to Go.
- [Jan 3 The magic function](https://bitfieldconsulting.com/posts/magic-function) [📖](https://read.readwise.io/read/01jgvjj8rrjmhcz4g703z9p73g) 👤 John Arundel 💬 1307 🔖 #rust 🗓️ 2025-01-05
    > **Резюме:** In his book "The Secrets of Rust: Tools," John Arundel discusses the importance of creating good abstractions in programming. He demonstrates this by designing a simple command-line tool in Rust that counts lines of input. Arundel emphasizes the need for intuitive APIs and proposes a "magic function" approach to guide the design process.
- [A half-hour to learn Rust](https://fasterthanli.me/articles/a-half-hour-to-learn-rust) [📖](https://read.readwise.io/read/01jg6b51wdgmey5qmd7bzrd7jc) 👤 Amos Wenger 💬 6376 🔖 #rust 🗓️ 2024-12-28
    > **Резюме:** The text introduces basic concepts of Rust programming, focusing on match arms, lifetimes, and function behavior with closures. It explains how borrowed references work and the differences between function types like `Fn` and `FnMut`. The author also highlights how closures can capture variables and affect their mutation.
- [Migrating from Java to Rust](https://corrode.dev/migration-guides/java-to-rust/) [📖](https://read.readwise.io/read/01jeqne2td1drxdzvt6n813zkq) 👤 Corrode Rust Consulting 💬 2536 🔖 #rust 🗓️ 2024-12-10
    > **Резюме:** This article helps technical leaders decide whether to migrate Java applications to Rust, highlighting the benefits like improved performance and resource usage. It offers practical tips for a smooth transition, such as starting small, having a clear plan, and training teams in Rust. Ultimately, the decision should involve team input and consider both immediate and long-term goals.
- [Writing a REST API in Rust](https://www.shuttle.rs/blog/2024/01/31/write-a-rest-api-rust) [📖](https://read.readwise.io/read/01jbyg6tesh0bx38z63v2gh0tn) 👤 shuttle.rs 💬 1373 🔖 #rest, #rust 🗓️ 2024-02-08
    > **Резюме:** This article provides a guide on writing a REST API in Rust. It covers topics such as project initialization, adding a database and migrations, writing routes, and deployment. The article includes code snippets and explanations for each step. It also suggests ways to extend the project and provides further reading recommendations. Overall, the article aims to help readers deploy their first API in Rust and highlights the benefits of using Rust for web services.
- [Rust vs C++: A Real-World Perspective | corrode Rust Consulting](https://corrode.dev/blog/cpp-rust-interop/) [📖](https://read.readwise.io/read/01jbyg695j0a5zzw5gp2h5n6bc) 👤 Corrode Rust Consulting 💬 1415 🔖 #rust 🗓️ 2024-08-14
    > **Резюме:** Choosing between Rust and C++ involves practical considerations beyond theoretical debates. Rust simplifies code development and refactoring, allowing developers to focus on higher-level tasks and complete code reviews more efficiently. Despite its benefits, Rust has a steeper learning curve and a less mature ecosystem compared to C++, but it can be integrated into existing C++ projects gradually.
- [Don't Unwrap Options: There Are Better Ways | corrode Rust Consulting](https://corrode.dev/blog/rust-option-handling-best-practices/) [📖](https://read.readwise.io/read/01jbyg661et5s873jw2pkqsdtv) 👤 Corrode Rust Consulting 💬 1639 🔖 #rust 🗓️ 2024-09-04
    > **Резюме:** The article discusses safer alternatives to using `unwrap()` when handling the `None` variant of `Option` in Rust. It highlights the new `let-else` syntax as the best approach for returning errors, as it is clear and easy for beginners to understand. Overall, the author encourages avoiding `unwrap()` to create more robust and maintainable code.
- [One year of Rust in production - Dmitry Kudryavtsev](https://yieldcode.blog/post/one-year-of-rust-in-production/) [📖](https://read.readwise.io/read/01jbyg64gmascbynpc9w8jj9jy) 👤 Dmitry Kudryavtsev 💬 1873 🔖 #rust 🗓️ 2024-09-23
    > **Резюме:** It's been almost a year for me developing, maintaining, and running a production web application written in Rust.
