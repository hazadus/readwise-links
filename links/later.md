# Отложенные ссылки

- Всего ссылок: 71

## Ссылки

- [To vibe or not to vibe](https://martinfowler.com/articles/exploring-gen-ai/to-vibe-or-not-vibe.html) 👤 Birgitta Böckeler 💬 1236 🔖 #llm 🗓️ 2025-09-24
    > **Резюме:** Trusting AI to write code isn't a yes-or-no choice; it depends on risk.  
Assess three things: how likely AI is wrong, how bad the impact would be, and how easily you will detect mistakes.  
Use that judgment to choose how much to review and what safeguards to add.
- [Why Belief Beats Discipline](https://www.joanwestenberg.com/p/why-belief-beats-discipline) 👤 JA Westenberg 💬 1354 🗓️ 2025-09-24
    > **Резюме:** Change starts with belief, not discipline.  
Without real belief, high standards become theater and fail.  
Act "as if" and repeat the behavior until belief and identity follow.
- [Let the domain guide your application structure](https://rednafi.com/go/app_structure/) 👤 Redowan Delowar 💬 1181 🗓️ 2025-09-22
    > **Резюме:** Let the domain, not the technology, guide your app's top-level structure.  
Avoid generic packages like models or handlers that lump multiple domains together.  
Give each domain its own package and have tech packages (http, postgres) depend on them and be wired in cmd.
- [Emerging Patterns in Building GenAI Products](https://martinfowler.com/articles/gen-ai-patterns/) 👤 Martin Fowler 💬 5715 🗓️ 2025-09-22
    > **Резюме:** The article discusses various patterns for building Generative AI (GenAI) products, including direct prompting, embeddings, and retrieval-augmented generation (RAG). It emphasizes the importance of evaluating LLM responses and using relevant document fragments to enhance the accuracy of the generated content. By combining different approaches, such as query rewriting and reranking, developers can improve the performance and relevance of LLM-based systems.
- [Plaguenomics: The Social Recession We Can’t Escape](https://www.joanwestenberg.com/p/plaguenomics-the-social-recession-we-can-t-escape) 👤 JA Westenberg 💬 2562 🗓️ 2025-09-20
    > **Резюме:** Plaguenomics is the post‑COVID collapse of social life and public trust.  
Isolation, stagnant wages, and attention‑seeking algorithms made anger and polarization normal.  
Without systematic fixes, this cycle will produce more violence and fragile democracies.
- [Opening all the files that have been modified in a Git branch](https://alexwlchan.net/2025/review-files-in-text-editor/?ref=rss) 👤 alexwlchan.net 💬 522 🔖 #git 🗓️ 2025-09-19
    > **Резюме:** This shows how to open every file changed in a Git branch in your local editor. Use git merge-base to find the branch point and git diff --name-only to list changed files. Pipe the list to xargs and open -a "Visual Studio Code" to open them all.
- [How Google writes clean, maintainable code](https://engineercodex.substack.com/p/how-google-writes-clean-maintainable) 👤 Leo | Engineer's Codex 💬 1376 🗓️ 2025-09-18
    > **Резюме:** Google follows a process called Readability, which is a mentorship process for disseminating programming language best practices. Each pull request is reviewed for proper code style and best practices by a code readability approver. To earn readability, engineers must submit code to readability reviewers until they have adequate knowledge. This process helps keep the codebase readable, searchable, and predictable, and enforces best practices and style. However, there are drawbacks, such as potential velocity slowdown and human bias. The need for code quality is subjective and depends on the individual and team.
- [Disposable Code Is Here to Stay, but Durable Code Is What Runs the World](https://www.honeycomb.io/blog/disposable-code-is-here-to-stay?utm_source=tldrwebdev) 👤 Honeycomb 💬 1844 🗓️ 2025-09-15
    > **Резюме:** Software is splitting into disposable code and durable code.  
Disposable code is cheap and short-lived; durable code must be reliable, maintainable, and trusted.  
AI speeds creation but cannot replace the tests, observability, and careful rollouts durable systems need.
- [Linking to text fragments with a bookmarklet](https://alexwlchan.net/2025/text-fragments-bookmarklet/?ref=rss) 👤 alexwlchan.net 💬 223 🗓️ 2025-09-15
    > **Резюме:** Text fragments let you link to and highlight specific text on a webpage. The author made a bookmarklet that builds the correct fragment URL from selected text. It makes sharing precise links much easier.
- [Building a Simple Virtual Machine](https://blog.phakorn.com/posts/2025/building-a-simple-vm/) 👤 Phakorn Kiong 💬 2249 🗓️ 2025-09-15
    > **Резюме:** The VM is byte-addressable and uses a 64-bit stack to hold data.  
Opcodes like PUSH1/PUSH8, STORE1/STORE8, LOAD8, ADD, and RETURN manipulate the stack and memory and are compiled into bytecode.  
The program counter walks the bytecode, stores data (e.g., "Hello Wo") into memory, and RETURN reads a memory block by offset and size.
- [Test state, not interactions](http://rednafi.com/go/test_state_not_interactions/) 👤 Redowan Delowar 💬 1542 🗓️ 2025-09-14
    > **Резюме:** Test outcomes and state, not which functions were called.  
LLMs and mock-generated interaction tests are brittle and can miss real bugs.  
Write the first tests yourself and prefer public-API tests with handwritten fakes or real test services.
- [Why I Switched Back From VS Code to IntelliJ IDEA: A Developer's Journey](https://mokkapps.de/blog/why-i-switched-back-from-vscode-to-intellij-idea) 👤 Michael Hoffmann 💬 1310 🗓️ 2025-09-14
    > **Резюме:** I switched back to IntelliJ because its built-in tools made daily work smoother.  
IntelliJ’s Git, indexing, debugging, and database features save time and keep context.  
VS Code is great for quick edits, but for full‑stack or large projects IntelliJ boosts long‑term productivity.
- [I Miss Tabs vs Spaces... And Other AI Musings](https://wsvincent.com/i-miss-tabs-vs-spaces/) 👤 William Vincent 💬 1304 🔖 #llm 🗓️ 2025-09-13
    > **Резюме:** Tabs versus spaces feels tiny next to the questions about AI. Developers use local models and agents to work faster, but they can hallucinate and need careful prompts. AI will change work and the economy, but it won’t replace human understanding and is often overhyped.
- [Agentic AI and Security](https://blog.korny.info/2025/09/12/agentic-ai-and-security) 👤 Korny Sietsma 💬 2746 🔖 #llm 🗓️ 2025-09-13
    > **Резюме:** Agentic AI are LLM tools that act on their own and can run commands you did not write.  
They are most dangerous when they can access private data, read untrusted content, and talk to the outside world.  
Limit agents’ external communication and access to public or untrusted content, and avoid agentic browser extensions and untrusted MCP servers.
- [Why I Ditched Docker for Podman (And You Should Too)](https://codesmash.dev/why-i-ditched-docker-for-podman-and-you-should-too?utm_source=tldrwebdev) 👤 Dominik Szymański 💬 2031 🗓️ 2025-09-12
    > **Резюме:** I switched from Docker to Podman. Docker's persistent dockerd daemon felt like a security and reliability risk. Podman is rootless, integrates well with systemd and pods, and is mostly drop-in compatible, so migration was easy.
- [Keeping Secrets Out of Logs](https://allan.reyes.sh/posts/keeping-secrets-out-of-logs/?utm_source=tldrwebdev) 👤 allan.reyes.sh 💬 6684 🗓️ 2025-09-12
    > **Резюме:** Secrets often end up in logs and there is no single fix.  
Prevent leaks by design: mark secrets at their sources and forbid them from logging sinks with types or taint checks.  
Use layered defenses—tests, formatters, scanners, and people—to catch what slips through.
- [Tunneling SSH over HTTPS](https://blog.frost.kiwi/ssh-over-https-tunneling/) 👤 Wladislav Artsimovich 💬 7549 🗓️ 2025-09-12
    > **Резюме:** Many networks block direct SSH but allow HTTPS.  
Using HTTP CONNECT with tools like corkscrew or proxytunnel lets you tunnel SSH through the proxy by relaying raw TCP.  
Wrapping the tunnel in TLS (HTTPS) hides SSH from packet inspection and helps bypass stricter blocks.
- [Video Game Blurs (and how the best one works)](https://blog.frost.kiwi/dual-kawase/?utm_source=tldrwebdev) 👤 Wladislav Artsimovich 💬 5898 🗓️ 2025-09-12
    > **Резюме:** The article shows how to implement realtime blurs on the GPU with WebGL and why performance matters.  
Box and Gaussian blurs can be slow or artifact-prone, while separable, frequency, and downsample methods speed things up with trade-offs.  
Dual Kawase Blur uses iterative diagonal sampling plus down/upsampling to give fast, motion-stable, Gaussian-like results used in games.
- [On Working with Wizards](https://www.oneusefulthing.org/p/on-working-with-wizards) 👤 Ethan Mollick 💬 2149 🗓️ 2025-09-12
    > **Резюме:** AI is moving from co-workers to wizards that produce impressive but opaque results.  
That makes it hard to check work and erodes our expertise.  
We need a new literacy to know when to summon the wizard, when to collaborate, and how to judge its output.
- [A new experimental Go API for JSON](https://go.dev/blog/jsonv2-exp) 👤 go.dev 💬 3099 🔖 #go 🗓️ 2025-09-10
    > **Резюме:** Go 1.25 introduces an experimental JSON API with encoding/json/v2 and encoding/json/jsontext to improve JSON handling in Go. These new packages offer better streaming, performance, and customization compared to the original encoding/json. The goal is to eventually replace the old API while keeping backward compatibility and involving the Go community.
- [Why I Delete Every Unanswered Email, Every Month](https://www.joanwestenberg.com/p/why-i-delete-every-unanswered-email-every-month) 👤 Joan Westenberg 💬 1372 🗓️ 2025-09-09
    > **Резюме:** The author deletes every unanswered email at the end of each month. She rejects the pressure to always reply and protects time for deep work. Important messages will return; most emails are not worth the cost.
- [How to Test](https://matklad.github.io/2021/05/31/how-to-test.html) 👤 matklad.github.io 💬 4435 🗓️ 2025-09-08
    > **Резюме:** Testing helps keep software working when making changes. Good tests focus on features, not code details, and should be easy to update. Slow or flaky tests make refactoring hard, so testing speed and reliability matter a lot.
- [Vibe coding is not the same as AI-Assisted engineering.](https://addyo.substack.com/p/vibe-coding-is-not-the-same-as-ai) 👤 Addy Osmani 💬 5554 🗓️ 2025-09-05
    > **Резюме:** Vibe coding is free-flow prompting that lets AI write code with little planning.  
It can speed prototypes but often creates hidden security, reliability, and maintenance risks in production.  
AI-assisted engineering uses structured specs, testing, and review so teams keep AI productivity without the risks.
- [Rich Pixels](https://simonwillison.net/2025/Sep/2/rich-pixels/#atom-everything) 👤 Simon Willison 💬 124 🗓️ 2025-09-02
    > **Резюме:** Rich Pixels is a Python library that shows images in the terminal using colored blocks. It uses Unicode characters to display two pixels with different colors in one block. A script called show_image.py resizes and shows images in the terminal using this library.
- [Passkeys and Modern Authentication](https://lucumr.pocoo.org/2025/9/2/passkeys/) 👤 Armin Ronacher 💬 1184 🗓️ 2025-09-02
    > **Резюме:** Passkeys are replacing passwords and can improve security for most people.  
But attestation, non-exportable keys, and auto-enrollment can enable ecosystem lock-in.  
That risks losing account access, reducing user control, and hurting families and developers.
- [Why German Strings are Everywhere](https://cedardb.com/blog/german_strings/?utm_source=substack&utm_medium=email) 👤 cedardb.com 💬 2009 🔖 #joyandcuriosity 🗓️ 2025-08-31
    > **Резюме:** German Strings use a single 128-bit layout to represent any string.  
Strings of 12 or fewer characters are stored inline; longer strings store a length, a pointer, and a four-character prefix for fast checks.  
They are immutable and support persistent, transient, and temporary storage classes to cut copies and speed reads, but appending is costly and lifetimes must be managed.
- [The McPhee method](https://jsomers.net/blog/the-mcphee-method?utm_source=substack&utm_medium=email) 👤 James Somers 💬 4008 🔖 #joyandcuriosity 🗓️ 2025-08-31
    > **Резюме:** McPhee gathers all his reporting up front: notes, transcripts, and excerpts. He then labels, sorts, and arranges those notes into a clear structure before he writes. With the structure set, he drafts quickly and then revises and fact-checks.
- [The Friendship That Made Google Huge | The New Yorker](https://www.newyorker.com/magazine/2018/12/10/the-friendship-that-made-google-huge?utm_source=substack&utm_medium=email) 👤 James Somers 💬 6675 🔖 #joyandcuriosity 🗓️ 2025-08-31
    > **Резюме:** Jeff Dean and Sanjay Ghemawat wrote core software that changed Google and the Internet.  
Side-by-side they built MapReduce to speed search and later created TensorFlow for AI.  
Their friendship and complementary skills let other engineers build huge distributed systems and AI.
- [Rolling the Dice with CSS random()](https://webkit.org/blog/17285/rolling-the-dice-with-css-random/?utm_source=tldrwebdev) 👤 Jen Simmons 💬 1846 🔖 #css 🗓️ 2025-08-30
    > **Резюме:** CSS now has a random() function to create random values for position, size, color, and rotation.  
The article demos star fields, random rectangles, and rotated image stacks.  
You can share randomness per-property, per-element, or globally with idents or element-shared, and try it in Safari Technology Preview.
- [You no longer need JavaScript](https://lyra.horse/blog/2025/08/you-dont-need-js/) 👤 lyra's epic blog 💬 1071 🔖 #css 🗓️ 2025-08-30
    > **Резюме:** Modern JavaScript frameworks add huge bloat and slow sites.  
Plain HTML and new CSS features like nesting and color functions can do a lot of the same work.  
The author wants to show these alternatives so you can choose when JavaScript is truly needed.
- [Git: count files in a repository](https://adamj.eu/tech/2025/08/29/git-count-files/) 👤 adamj.eu 💬 340 🔖 #git 🗓️ 2025-08-30
    > **Резюме:** Count committed files with Git so you ignore generated or downloaded files.  
Run: git ls-files -z | tr -d -c '\0' | wc -c — null bytes prevent errors from filenames with newlines.  
Use git ls-files '<pattern>' | wc -l to count types or git ls-files ':!<pattern>' to exclude files.
- [Python: The Documentary | An origin story](https://youtube.com/watch?v=GfH4QL4VqJ0&si=W-p_AVfiGeQIwieQ) 👤 CultRepo (formerly Honeypot) 🗓️ 2025-08-28
    > **Резюме:** Python began as Guido van Rossum's small project.  
A supportive community and conferences helped it grow into a major tool for science and data.  
The hard move from Python 2 to 3 proved the community's strength and spread Python further.
- [Wicked Python trickery - dynamically patch a Python function's source code at runtime](https://ericmjl.github.io/blog/2025/8/23/wicked-python-trickery-dynamically-patch-a-python-functions-source-code-at-runtime/?utm_source=tldrwebdev) 👤 Eric J. Ma 💬 2315 🔖 #python 🗓️ 2025-08-27
    > **Резюме:** This blog explains how to change a Python function's code while the program runs using compile and exec. The author built ToolBot, which can create and run new functions that use current variables. This method is powerful but has security risks and should be used carefully.
- [Building your own CLI Coding Agent with Pydantic-AI](https://martinfowler.com/articles/build-own-coding-agent.html) 👤 Ben O'Mahony 💬 2899 🔖 #llm, #agents 🗓️ 2025-08-27
    > **Резюме:** They built a CLI coding agent using Pydantic‑AI and MCP that reads code, runs tests, and edits files. MCP servers add sandboxed Python, code reasoning, and file/terminal tools so the model can act. The result is faster, context‑aware development that works best when tailored to your codebase.
- [Building AI Products In The Probabilistic Era](https://giansegato.com/essays/probabilistic-era?utm_source=substack&utm_medium=email) 👤 giansegato.com 💬 4463 🔖 #joyandcuriosity 🗓️ 2025-08-24
    > **Резюме:** AI is probabilistic, not deterministic, and often behaves in unexpected ways.  
Product teams must use continuous data, test real user trajectories, and accept some unpredictability instead of trying to fully control models.  
Organizations that think empirically and in probabilities will win the next era.
- [The Difference Between a Post Flush Watcher and nextTick in Vue](https://michaelnthiessen.com/the-difference-between-a-post-flush-watcher-and-nexttick?ck_subscriber_id=2108193410&utm_campaign=The+Difference+Between+a+Post+Flush+Watcher+and+nextTick+in+Vue+-+18711361&utm_medium=email&utm_source=convertkit) 👤 michaelnthiessen.com 💬 1110 🗓️ 2025-08-24
    > **Резюме:** A post-flush watcher and nextTick both wait until after the DOM updates. The only difference is timing: nextTick runs one microtask later and therefore runs after post-flush watchers. In practice this rarely matters unless you need a strict execution order.
- [Introduction to AT Protocol](https://mackuba.eu/2025/08/20/introduction-to-atproto/?utm_source=tldrwebdev) 👤 Kuba Suder 💬 8494 🔖 #bluesky 🗓️ 2025-08-24
    > **Резюме:** Bluesky is built on the AT Protocol, which defines how data and social features work together. It uses specific lexicons for different functions, allowing both Bluesky and third-party apps to share data on the same network. Bluesky also offers custom feeds and a public API that lets users and developers create and use various social tools easily.
- [What Learning React Won't Teach You: Image Formats](https://idiallo.com/blog/react-and-image-format?utm_source=tldrwebdev) 👤 Ibrahim Diallo 💬 1241 🗓️ 2025-08-24
    > **Резюме:** Image format choices have a huge impact on site speed and bandwidth. Use JPEG for photos, PNG for simple graphics and transparency, and SVG for scalable icons and logos. React guides often skip this, so developers unknowingly bloat apps and hurt user experience.
- [My AI Had Already Fixed the Code Before I Saw It](mailto:reader-forwarded-email/ad2b90fe856ee487d1eee89442319202) 👤 Every 💬 2253 🗓️ 2025-08-24
    > **Резюме:** Compounding engineering builds systems that learn from every bug, pull request, and code review so fixes become permanent.  
The team uses Claude to write tests, iterate prompts, and store workflows in CLAUDE.md so the AI keeps improving automatically.  
This turns one-off fixes into lasting automation that makes future work faster and safer.
- [Instructor and Pydantic - Structured LLM outputs for easy data extraction!](https://www.youtube.com/watch?v=3xUW1Do9zOs) 👤 BugBytes 🗓️ 2025-08-23
    > **Резюме:** Instructor and Pydantic turn LLM text into structured data.  
Read a PDF, extract its text, and send it to the model.  
The model returns validated invoice fields you can use in apps.
- [Commit Messages That Write Themselves](https://newsletter.appliedgo.net/archive/2025-08-17-commit-messages-that-write-themselves/) 👤 The Applied Go Weekly Newsletter 💬 1485 🔖 #go, #git 🗓️ 2025-08-17
    > **Резюме:** A small Go tool reads your staged git diff and uses an LLM to generate Conventional Commit messages.  
It uses LangChainGo so you can swap providers, asks the model for JSON output, and caps diffs to save tokens.  
This issue wraps up the Go & AI mini‑series and asks readers to take a short feedback survey.
- [Why I chose OCaml as my primary language](https://xvw.lol/en/articles/why-ocaml.html?utm_source=tldrwebdev) 👤 xvw, Xavier Van de Woestyne 💬 11234 🗓️ 2025-08-16
    > **Резюме:** OCaml is a versatile and evolving programming language that combines strong static typing with multiple programming paradigms. It has a rich ecosystem, good tooling, and can compile to various targets like JavaScript and WebAssembly. The supportive community and practical features make OCaml a great choice for both learning and professional development.
- [Another article about centering in CSS](https://piccalil.li/blog/another-article-about-centering-in-css/?ref=main-rss-feed) 👤 Piccalilli 💬 1236 🔖 #css 🗓️ 2025-08-14
    > **Резюме:** Centering in CSS is easier than ever with many options like grid and flexbox, but choosing one clear method is key. Using parent-based layouts with grid or flexbox is better than mixing child and parent alignment. Avoid positioning for centering unless you fully control the parent, and focus on simple, consistent principles for your team.
- [Building a web search engine from scratch in two months with 3 billion neural embeddings](https://blog.wilsonl.in/search-engine/?utm_source=tldrwebdev) 👤 Wilson Lin 💬 8008 🗓️ 2025-08-13
    > **Резюме:** The author built a powerful web search engine using 3 billion neural embeddings in just two months. It can understand complex queries and delivers fast, accurate results by using advanced indexing and embedding techniques. This project shows that neural embeddings can greatly improve search quality compared to traditional methods.
- [What are Effect Scopes in Vue?](https://michaelnthiessen.com/what-are-effect-scopes-in-vue?ck_subscriber_id=2108193410&utm_campaign=%F0%9F%94%A5+(230)+What+are+Effect+Scopes+in+Vue?+-+18611005&utm_medium=email&utm_source=convertkit) 👤 michaelnthiessen.com 💬 1063 🔖 #vue, #nuxt 🗓️ 2025-08-13
    > **Резюме:** Effect scopes in Vue group related reactive effects so they can be stopped and cleaned up easily. This helps prevent memory leaks and bugs by controlling how long effects live. They are used inside components and also for advanced patterns like shared composables.
- [Testing with Go and PostgreSQL: ephemeral DBs](https://michael.stapelberg.ch/posts/2024-11-19-testing-with-go-and-postgresql-ephemeral-dbs/) 👤 Michael Stapelberg 💬 2859 🔖 #go, #testing, #postgresql 🗓️ 2025-08-10
    > **Заметка:** From Thorsten Ball interview
    > **Резюме:** This article explains how to use ephemeral PostgreSQL instances for automated testing in Go, which can reduce resource usage and speed up test times. By starting a single PostgreSQL instance for all tests instead of multiple instances, developers can improve efficiency and maintainability. Additionally, optimizing the Go test caching behavior can further decrease test runtime significantly.
- [Donut math: how donut.c works](https://www.a1k0n.net/2011/07/20/donut-math.html?utm_source=substack&utm_medium=email) 👤 a1k0n.net 💬 2469 🔖 #joyandcuriosity 🗓️ 2025-08-10
    > **Резюме:** The code draws a spinning 3D donut using ASCII characters by projecting 3D points onto a 2D screen with math involving rotations and perspective. It calculates the brightness of each point based on lighting and chooses characters to show shading. This creates a cool visual effect of a rotating donut made from simple text symbols.
- [Ludic's Guide To Getting Software Engineering Jobs](https://ludic.mataroa.blog/blog/ludics-guide-to-getting-software-engineering-jobs/) 👤 mataroa.blog 💬 8531 🔖 #career 🗓️ 2025-08-07
    > **Резюме:** Getting software engineering jobs often means starting with many mediocre, short-term roles. Success comes from quickly applying, not stressing about perfect fits, and being open to day-rate contracts. Building connections and being clear about your needs helps find better, well-paid jobs later.
- [Why Building Billing Systems is So Painful](https://www.dmitry.ie/2024/why-building-billing-systems-is-so-painful?utm_source=tldrwebdev) 👤 dmitry.ie 💬 1859 🗓️ 2025-08-07
    > **Резюме:** Billing systems are very complex because they must handle many pricing models, currencies, taxes, and real-time usage tracking. They serve many customers inside a company, like finance, sales, and product teams, each with different needs. Building billing right is hard but important, as it is a critical part of business infrastructure that drives growth and success.
- [Gateway pattern to invoke external dependencies](http://rednafi.com/go/gateway_pattern/) 👤 Redowan Delowar 💬 1179 🔖 #go 🗓️ 2025-08-04
    > **Резюме:** The Gateway pattern helps separate business logic from external service calls by using interfaces. In Go, the consumer defines the interface, allowing easy testing with mocks. This design keeps the service and external dependencies independent and testable.
- [Issuing TLS Certificates in Go](https://getpid.dev/blog/tls-certificates/) 👤 Software Engineering & Personal Thoughts 💬 1511 🔖 #go 🗓️ 2025-08-04
    > **Резюме:** This guide explains how to create TLS certificates in Go, starting with self-signed certificates and building a chain of trust using root and intermediate Certificate Authorities. It shows how to generate keys, create certificate templates, and sign certificates, including those from Certificate Signing Requests (CSRs). The process helps secure communication by ensuring certificates are trusted and valid for their intended use.
- [Benchmarking MicroPython](https://blog.miguelgrinberg.com/post/benchmarking-micropython) 👤 Miguel Grinberg 💬 2096 🗓️ 2025-08-01
    > **Резюме:** MicroPython runs much slower on microcontrollers than on laptops or Raspberry Pi computers. Different microcontrollers perform differently depending on the task, so speed varies. Despite being slow, microcontrollers are still very useful for many projects.
- [Гайд по кастомизации vscode: тайлы и менеджеры горячих клавиш](https://www.youtube.com/watch?v=frZkPK_1Ui4) 👤 Никита Соболев 🗓️ 2025-07-30
    > **Резюме:** Автор показывает, как настроить VSCode для удобной и быстрой работы с помощью тайлинговых менеджеров и горячих клавиш. Это помогает легко переключаться между приложениями и улучшает продуктивность. В следующих видео он расскажет, как минимизировать лишние элементы и сделать интерфейс проще.
- [Embeddings: What they are and why they matter](https://simonwillison.net/2023/Oct/23/embeddings/) 👤 Simon Willison 💬 4839 🗓️ 2025-07-27
    > **Резюме:** Embeddings turn content like text or images into numbers that capture their meaning. They help computers find and compare similar information quickly. This technology powers tools like search engines and question-answering systems.
- [From Async/Await to Virtual Threads](https://lucumr.pocoo.org/2025/7/26/virtual-threads/) 👤 Armin Ronacher 💬 1974 🗓️ 2025-07-27
    > **Резюме:** The article discusses how virtual threads could simplify Python concurrency by replacing complex async/await patterns with a clearer thread-based model. It highlights the benefits of structured concurrency and how virtual threads can improve cancellation and error handling. The author suggests this approach could make concurrent programming easier by moving complexity into the runtime instead of the user’s code.
- [Getting Real](http://gettingreal.37signals.com/) 👤 basecamp.com 💬 426 🔖 #book 🗓️ 2025-07-24
    > **Резюме:** "Getting Real" by 37signals is a valuable resource for anyone creating a web app, offering simple insights and unique ideas. It focuses on practical approaches to software design rather than technical details. Readers from various backgrounds, including entrepreneurs and designers, will find inspiration in its unconventional wisdom.
- [A Friendly Introduction to SVG](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/?from=newsletter) 👤 Josh W. Comeau 💬 3091 🗓️ 2025-07-21
    > **Резюме:** SVG is a special image format that uses shapes like circles and lines written in code. It can be styled and animated using CSS and JavaScript, making it very powerful. SVG images stay sharp no matter how much you zoom in, which is great for web design.
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) 👤 Andrej Karpathy 🔖 #llm 🗓️ 2025-07-21
    > **Резюме:** You can use open-weight language models through inference providers like Together.AI. Together.AI offers a playground where you can try many different open models. Finding basic models is less common on these platforms.
- [MacPaint Art From The Mid-80s Still Looks Great Today](https://blog.decryption.net.au/posts/macpaint.html) 👤 https://decryption.net.au 💬 266 🔖 #joyandcuriosity 🗓️ 2025-07-20
    > **Резюме:** The author explored thousands of MacPaint images from the early 1980s and found impressive digital art. They want to learn more about the artists and also plan to explore similar art on the Amiga computer. For those interested, there are resources like Discmaster and a book called Zen & The Art of The Macintosh to help create this style of art.
- [Mind Management, Not Time Management](private://read/01jy2bx4yjy7cc3fb6cs5zy8ma) 👤 David Kadavy 💬 72204 🗓️ 2025-06-18
    > **Резюме:** David Kadavy emphasizes the importance of managing mental states over time when working on creative projects. He identifies seven mental states and encourages finding a "Creative Sweet Spot" for when to generate ideas. By experimenting with focused time, especially in the morning, you can enhance creativity and productivity.
- [The best way to store your dotfiles: A bare Git repository](https://www.atlassian.com/git/tutorials/dotfiles) 👤 Atlassian 💬 710 🔖 #git, #try 🗓️ 2025-06-06
    > **Резюме:** This tutorial explains a simple way to store dotfiles using a Git bare repository. It involves creating an alias that allows you to manage your configuration files without interfering with other Git repositories. By following the steps provided, you can easily version and replicate your configurations across different systems.
- [PostgreSQL как эффективная база для документных данных](https://youtube.com/watch?v=l8__4kI4zgU&si=FWi3JO7IruJno-N8) 👤 Health Samurai Team 🔖 #postgresql 🗓️ 2025-05-31
    > **Резюме:** PostgreSQL is an effective database for storing document data, allowing for efficient querying and indexing. It supports JSONB for handling complex documents and provides various operators for accessing specific fields. The system can handle large datasets and offers the flexibility to adapt as data grows, making it a robust choice for developers.
- [JavaScript, what is this?](https://piccalil.li/blog/javascript-what-is-this/?ref=main-rss-feed) 👤 Mat “Wilto” Marquis 💬 3410 🔖 #javascript 🗓️ 2025-05-10
    > **Резюме:** In JavaScript, the keyword "this" refers to the object that is currently executing the function, which is often the global object (window) unless specified otherwise. In strict mode, "this" can be undefined, making the behavior more predictable. Arrow functions have a different behavior, as "this" refers to the surrounding lexical context instead of the function's execution context.
- [JavaScript, when is this?](https://piccalil.li/blog/javascript-when-is-this/?ref=main-rss-feed) 👤 Piccalilli 💬 1770 🔖 #javascript 🗓️ 2025-05-02
    > **Резюме:** In JavaScript, the value of "this" depends on how a function is called, not how it is written. When a function is executed, JavaScript creates an execution context that determines the value of "this" based on the calling context. Understanding JavaScript's execution model is key to grasping how "this" works in different situations.
- [Celebrating 50 years of Microsoft | Bill Gates](https://www.gatesnotes.com/meet-bill/source-code/reader/microsoft-original-source-code) 👤 Bill Gates 💬 5503 🗓️ 2025-04-04
    > **Резюме:** Bill Gates reflects on the 50th anniversary of Microsoft, starting with the creation of Altair BASIC in 1975. He shares his pride in how this early code led to a revolution in computing and the company's immense success. Gates also acknowledges the influential teachers who helped shape his journey into the world of technology.
- [🔥uv — швейцарский нож Python-разработчика](https://youtu.be/0Osso8mLL-A) 👤 Диджитализируй! 🔖 #uv 🗓️ 2025-03-17
    > **Резюме:** uv is a powerful package manager for Python developers that simplifies working with different Python versions and dependencies. It allows you to manage project environments without manually creating virtual environments. This tool is highly recommended for efficient dependency management in Python projects.
- [How Core Git Developers Configure Git](https://blog.gitbutler.com/how-git-core-devs-configure-git/) 👤 GitButler 💬 3188 🔖 #git 🗓️ 2025-02-25
    > **Резюме:** The author shares lesser-known Git configuration settings that core Git developers recommend for better performance. These settings include adjusting default branch names, improving diff algorithms, and enhancing push and fetch behavior. By enabling these options, users can streamline their Git experience and make it more efficient.
- [How to Take Smart Notes: One Simple Technique to Boost Writing, Learning and Thinking – for Students, Academics and Nonfiction Book Writers](private://read/01jg1e2q7yj2698nhna2kjbce4) 👤 Ahrens, Sönke 💬 56774 🔖 #pkm, #basb, #outline, #learning, #inspiration 🗓️ 2024-12-26
    > **Резюме:** The book "How to Take Smart Notes" by Sönke Ahrens emphasizes the importance of effective note-taking for improving writing, learning, and thinking. By using a slip-box system, individuals can organize their ideas and connect them, enhancing their understanding and creativity. This method promotes active engagement with material and transforms notes into a valuable resource for future writing.
- [Grep by example: Interactive guide](https://antonz.org/grep-by-example/) 👤 Anton Zhiyanov 💬 1837 🗓️ 2025-05-03
    > **Резюме:** The interactive guide to using grep explains how to search for text patterns efficiently. It covers basics like searching for patterns in files, using regular expressions for advanced searches, and searching for fixed strings. The guide also delves into handling multiple patterns, recursive searches, and various output options like counting matches, limiting results, and displaying only relevant parts of the output. Additionally, it provides insights on using grep options to ignore case sensitivity, invert matches, and customize output formats for different search scenarios.
- [PostgreSQL: как связь 1 к 1 ускоряет базу данных? Разбираемся во внутренней работе СУБД](https://www.youtube.com/watch?v=Pk125DazUyI) 👤 Диджитализируй! 🔖 #postgresql 🗓️ 2024-11-05
    > **Резюме:** Связь один к одному в базах данных PostgreSQL помогает оптимизировать работу с данными. Это позволяет разделять часто и редко используемые данные, улучшая производительность системы. Используйте эту связь, чтобы сделать свои базы данных более эффективными.
- [Promises From The Ground Up](https://www.joshwcomeau.com/javascript/promises/) 👤 joshwcomeau.com 💬 3746 🗓️ 2025-09-06
    > **Резюме:** The text discusses the importance of understanding Promises in JavaScript for modern web development. Promises allow for asynchronous operations and help avoid callback nesting. Modern JavaScript features like async/await simplify handling asynchronous tasks.
