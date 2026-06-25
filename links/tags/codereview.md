# Ссылки

- Всего ссылок: 12

## Ссылки

- [Adversarial Communication](https://blog.glyph.im/2026/06/adversarial-communication.html) [📖](https://read.readwise.io/read/01kvsck0xkwt59pjbqrb7hef8y) 👤 Glyph 💬 2762 🔖 #learning, #codereview, #llm-devimpact, #llm-resistance 🗓️ 2026-06-23
    > **Заметка:** "Враждебная коммуникация". Сквозная идея поста – LLM позволяют перенести стоимость верификации выхлопа с "автора", получающего выгоду, на "жертву", которой предстоит всё это разгребать.
    > **Резюме:** “AI” turns every conversation into a fight, because fighting is what
they are good at.
- [The agent principal-agent problem](https://crawshaw.io/blog/agent-principal-agent) [📖](https://read.readwise.io/read/01kr1w2kadyfj1r759s1yh6ezr) 👤 David Crawshaw (david@zentus.com) 💬 1234 🔖 #codereview, #llm-devimpact 🗓️ 2026-05-07
    > **Резюме:** The agent principal-agent problem
2026-05-07
Code review is broken.
The industry-established code review process, review-then-commit, was a straightforward mechanism that allowed a relatively low-trust group of engineers to collaborate. It appears to have been initially developed for the Apache server OSS project in the 90s, corporatized by Google in the early 2000s, and popularized throughout the industry by several means, most notable of which was the GitHub PR.
It was very simple:

A human makes a change.
This change is packaged up, sent to another human for commentary.
Rounds of commentary and adjustments continue until the reviewer approves (LGTMs) it.
The change is committed.

This is not Michael Fagan's defect analysis work or the ticket-like processes used for critical systems changes in fields like aerospace. This will not catch your bugs. It will, however, communicate design changes to other engineers who maintain a mental model of the codebase, and reviewers can use the process to teach norms to contributors. It has advantages, and because there is a gate before the main branch changes, it does not require much trust. That makes it a great tool for scaling a company, because beyond ~10-12 engineers (the "two pizza" team, among other names), trust erodes rapidly. It is also great for scaling OSS. It puts work on reviewers, but there was work on the human making the change too. An imbalance existed but was often manageable.
The crisis of code review
Agents broke this. If you insert an agent into the existing process, your best possible outcome is:

A human instructs a machine to make a change.
The human reviews the code, iterates with comments until they approve it.
This change is packaged up, sent to another human for commentary.
Rounds of commentary and adjustments continue until the reviewer approves (LGTMs) it.
The change is committed.

This doubles the amount of review. But companies were already review limited. In a really well-functioning team, a ...
- [What Is Code Review For?](https://blog.glyph.im/2026/03/what-is-code-review-for.html) [📖](https://read.readwise.io/read/01kjwj2d6ngddzrgxejrw2wsp9) 👤 Glyph Lefkowitz 💬 1353 🔖 #codereview 🗓️ 2026-03-04
    > **Резюме:** Code review is mainly a social process to share knowledge and improve team culture, not a way to catch bugs. Automated tools like tests and linters are better for finding errors reliably. When reviewing code from AI like LLMs, rely on strong automated checks because these tools do not learn or improve like humans.
- [No code reviews by default](https://www.raycast.com/blog/no-code-reviews-by-default?utm_source=substack&utm_medium=email) [📖](https://read.readwise.io/read/01kba8bsbgb2t8n4z5sbprc8kb) 👤 Thomas Paul Mann 💬 1054 🔖 #codereview, #joyandcuriosity 🗓️ 2025-11-30
    > **Резюме:** At Raycast, engineers can push code directly to the main branch without mandatory reviews, fostering a culture of trust and rapid iteration. While code reviews are optional, they are requested when necessary, especially for significant changes or for new team members. This approach allows for quick feedback and continuous updates, helping the team to efficiently build and improve their product.
- [Code Review Developer Guide](https://google.github.io/eng-practices/review/) [📖](https://read.readwise.io/read/01k8qnxqs6q75kg8v6grbdk5ex) 👤 eng-practices 💬 416 🔖 #codereview 🗓️ 2025-10-29
    > **Резюме:** Code review is a process where someone other than the code author examines the code to ensure quality. Google has specific guidelines for code reviewers, focusing on design, functionality, complexity, tests, naming, comments, style, and documentation. It's important to choose the best reviewers and can include in-person reviews for effective feedback.
- [Mistakes I see engineers making in their code reviews](https://seangoedecke.com/good-code-reviews/) [📖](https://read.readwise.io/read/01k8dmp5mbpd8dv1qd65y5868s) 👤 seangoedecke.com 💬 2088 🔖 #codereview 🗓️ 2025-10-25
    > **Резюме:** Code review should look beyond the diff and consider how the change fits the whole codebase. Leave only a few high-value comments and avoid imposing personal style on every PR. If you truly want to block a change, make it a blocking review; otherwise approve so work can move forward.
- [“ChatGPT said this” Is Lazy](https://terriblesoftware.org/2025/10/24/chatgpt-said-this-is-lazy/) [📖](https://read.readwise.io/read/01k8d1q30e11dnsqhhs0fcphnh) 👤 Terrible Software 💬 374 🔖 #llm, #codereview 🗓️ 2025-10-25
    > **Резюме:** Pasting AI output as a review is lazy and unhelpful. Give specific feedback based on your own understanding of the code and context. Use AI to help you think, not to avoid thinking.
- [A guide for Code Reviews](https://yusufaytas.com/a-guide-for-code-reviews/) [📖](https://read.readwise.io/read/01k8awcrr9g8jhmg8es1tkqesg) 👤 https://www.facebook.com/yusufaytas 💬 396 🔖 #codereview 🗓️ 2025-10-24
    > **Резюме:** Send focused, well-documented, and tested code reviews, breaking large features into multiple CRs.  
Reviewers should read the context, give constructive questions and praise, and prefer design discussions over many nitpicks.  
Treat each other respectfully, avoid personal attacks, and use issue tracking and consistent formatting.
- [The price of mandatory code reviews](https://newsletter.manager.dev/p/the-price-of-mandatory-code-reviews) [📖](https://read.readwise.io/read/01k83dhy6n5gzppn0v42gtxv51) 👤 Anton Zaides 💬 1305 🔖 #codereview 🗓️ 2025-10-21
    > **Резюме:** Mandatory code reviews slow shipping but cut bugs a lot. High-quality, fast reviews give the best trade-off. Top teams combine selective reviews, speed, and strong review culture.
- [If you are good at code review, you will be good at using AI agents](https://seangoedecke.com/ai-agents-and-code-review/) [📖](https://read.readwise.io/read/01k5qxxq9k1wek7m1nm220vryz) 👤 seangoedecke.com 💬 1285 🔖 #llm, #codereview 🗓️ 2025-09-22
    > **Резюме:** AI agents can generate lots of code but lack sound judgment.  
Strong code-review skills—seeing structure and alternatives—let you guide agents away from bad designs.  
Using AI well means supervising its architecture choices, not just tweaking lines.
- [Code Review Can Be Better](https://tigerbeetle.com/blog/2025-08-04-code-review-can-be-better/?utm_source=substack&utm_medium=email) [📖](https://read.readwise.io/read/01k3e2qkvxvm2tm7d4m75rxfb5) 👤 matklad 💬 928 🔖 #git, #github, #codereview, #joyandcuriosity 🗓️ 2025-08-24
    > **Резюме:** The author tried a new way to do code reviews by storing comments as commits in git, but it was too complicated to work well. Current web-based tools cause delays and limit local code exploration. For now, they returned to web reviews, hoping better solutions will come.
- [How To Review Code](https://endler.dev/2025/how-to-review-code/) [📖](https://read.readwise.io/read/01k1yvvs1493prkg6v97wd9ajd) 👤 Matthias Endler 💬 2062 🔖 #codereview 🗓️ 2025-08-06
    > **Резюме:** Good code reviews look beyond changes to consider design, future issues, and system fit. Clear communication, respect, and explaining reasons help improve code and teamwork. Running the code and focusing on logic and maintainability lead to better understanding and learning.
