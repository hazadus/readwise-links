# Ссылки

- Всего ссылок: 5

## Ссылки

- ['Make invalid states representable' considered harmful](https://seangoedecke.com/invalid-states/) 👤 seangoedecke.com 💬 2050 🔖 #softwaredesign 🗓️ 2025-09-08
    > **Резюме:** Software should be more flexible than the domain model and allow some invalid states. Hard constraints like strict state machines, foreign keys, or required protobuf fields break under edge cases and schema changes. Prefer soft, changeable checks in code so systems can adapt when reality forces exceptions.
- [Do the simplest thing that could possibly work](https://seangoedecke.com/the-simplest-thing-that-could-possibly-work/) 👤 seangoedecke.com 💬 1720 🔖 #toot, #development, #programming, #microservices, #softwaredesign 🗓️ 2025-08-29
    > **Заметка:** Шон на примерах рассказывает о важности простоты дизайна ПО.
    > **Резюме:** Build the simplest thing that could possibly work and only add complexity when real requirements force it.  
Simple means fewer moving parts and less coupling, so the system is easier to understand and maintain.  
Avoid premature scaling and over‑engineering, but think hard to find genuinely simple solutions.
- [Everything I know about good system design](https://seangoedecke.com/good-system-design/) 👤 seangoedecke.com 💬 3948 🔖 #development, #softwaredesign 🗓️ 2025-06-22
    > **Заметка:** Всё по делу пишет. Никаких открытий, но рекомендации хорошие. 
    > **Резюме:** Good system design means minimizing stateful parts because they can cause problems. Databases are often slow, so use indexes wisely and send read queries to replicas to avoid overload. Use caching carefully and choose pushing or pulling data methods based on how often data changes and how many clients need it.
- [When worse is better](https://www.bitecode.dev/p/when-worse-is-better) 👤 Bite Code! 💬 2434 🔖 #development, #inspiration, #softwaredesign 🗓️ 2025-03-11
    > **Резюме:** The author argues that sometimes a simpler, less sophisticated approach can be more effective and cost-efficient than striving for perfection in technology. They emphasize that while it’s crucial to produce good software, most projects lack the resources to achieve the best possible outcomes. Ultimately, evaluating whether a solution can be made "worse" might lead to better results overall.
- [Great software design looks underwhelming](https://seangoedecke.com/great-software-design/) 👤 seangoedecke.com 💬 1295 🔖 #development, #inspiration, #softwaredesign 🗓️ 2025-03-08
    > **Резюме:** Great software design often appears simple because it focuses on eliminating potential failure modes during the design stage. Instead of adding complex solutions to manage risks, effective design minimizes these risks from the start. Boring and straightforward approaches can lead to more reliable software than flashy, complicated ones.
