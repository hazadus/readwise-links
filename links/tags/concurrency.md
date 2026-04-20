# Ссылки

- Всего ссылок: 6

## Ссылки

- [Gist of Go: Concurrency](https://antonz.org/go-concurrency/) [📖](https://read.readwise.io/read/01jfq3wq8y8gq22ae3aharc2d2) 👤 Anton Zhiyanov 💬 365 🔖 #go, #concurrency 🗓️ 2024-12-22
    > **Резюме:** The author is creating an interactive book to teach Go concurrency through practical exercises. It is designed for programmers familiar with Go, covering concurrency tools from the basics. The book includes 44 interactive exercises and aims to make complex topics easy to understand.
- [Gist of Go: Pipelines](https://antonz.org/go-concurrency/pipelines/) [📖](https://read.readwise.io/read/01jfq3m4tv4x617dnkfveyxpn0) 👤 Anton Zhiyanov 💬 3159 🔖 #go, #concurrency 🗓️ 2024-12-22
    > **Резюме:** This text explains how to create concurrent pipelines in Go using goroutines and channels. It highlights the importance of managing goroutines to prevent leaks, using cancel channels, and employing select statements for efficient channel operations. The author provides code examples to illustrate these concepts effectively.
- [Gist of Go: Goroutines](https://antonz.org/go-concurrency/goroutines/) [📖](https://read.readwise.io/read/01jfq2y3gzedm7v08whce62x18) 👤 Anton Zhiyanov 💬 3703 🔖 #go, #concurrency 🗓️ 2024-12-22
    > **Резюме:** The text explains how to count digits in words using goroutines and channels in Go. It outlines a method to create separate goroutines for processing words and counting digits, improving concurrency. The final solution involves using named functions to handle word submission, counting, and filling statistics efficiently.
- [Futures in Go, no package required](https://appliedgo.net/futures/) [📖](https://read.readwise.io/read/01jewy794tdge6nabagnmpqx1q) 👤 Applied Go 💬 1984 🔖 #go, #concurrency 🗓️ 2024-12-12
    > **Резюме:** Goroutines and channels in Go make implementing futures simple and efficient. By using channels, values can be asynchronously computed and retrieved when needed. Go's built-in concurrency features allow for easy management of futures with minimal additional code.
- [Continuous refresh, or: how to keep your API client authorized](https://appliedgo.net/refresh/) [📖](https://read.readwise.io/read/01jen0ck79736h22ksakvt2p4r) 👤 Applied Go 💬 3494 🔖 #go, #try, #concurrency 🗓️ 2024-12-09
    > **Резюме:** Managing access tokens for API clients is crucial to prevent access issues when tokens expire. The solution involves refreshing the token in the background before it expires, ensuring clients always receive a valid token through a simple method call. This can be achieved using Go's concurrency features, either through channels or mutexes, to handle multiple client requests smoothly.
- [Understanding Mutexes](https://www.alexedwards.net/blog/understanding-mutexes) [📖](https://read.readwise.io/read/01jdf95vc4kkr5z78wd4yfb4d4) 👤 Alex Edwards 💬 1166 🔖 #go, #concurrency 🗓️ 2024-11-24
    > **Резюме:** Alex Edwards' article explains how to manage concurrent requests in Go web applications to avoid race conditions. He introduces mutexes and demonstrates how to implement them to protect shared data, ensuring that only one goroutine can modify it at a time. The article also touches on using read/write mutexes for scenarios with more reads than writes, improving efficiency.
