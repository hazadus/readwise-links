# Ссылки

- Всего ссылок: 7

## Ссылки

- [Why use ORMs if LLMs write code?](https://blog.ploeh.dk/2026/08/13/why-use-orms-if-llms-write-code/) [📖](https://read.readwise.io/read/01kzx00jpg01gapxfksrx78kas) 👤 Mark Seemann 💬 249 🔖 #db, #sql, #llm-devimpact 🗓️ 2026-08-13
    > **Заметка:** Соглашусь с автором. Нынче становится всё проще обходиться без ORM. 
    > **Резюме:** 

The return of SQL?


        It's no secret that I'm no fan of ORMs. Most people, on the other hand, find them indispensable. As one reader commented:
    


            "I can work with raw SQL ofcourse... but the mapping... oh the mapping..."
        
qfilip


        This seems to capture something essential. When I discuss ORMs, the most common argument in favour seems to revolve around the amount of boilerplate code required to communicate with a relational database. And indeed, it's significant.
    

        As I've argued, however, I'm not convinced that ORMs solve that problem.
    

        But now that LLMs write code, does it even matter?
    

        In addition to my individual reservations, it strikes me that ORMs come with many issues related to query efficiency. The vibe I'm getting from ORM experts is that if you really know a particular ORM, you can fine-tune the queries it makes. There are, however, various pitfalls to avoid: Anti-patterns to eschew, idioms to follow, particular APIs to keep clear of, certain parameter values to explicitly pass, etc.
    

        Which strikes me as ironic, because wasn't the whole promise of ORMs that you could read from and write to a relational database without getting bogged down in the details of SQL?
    

        So instead of fiddling with a temperamental and implicit ORM API, why not write fine-tuned parametrized SQL queries? Or rather, ask an LLM to do that for you, as well as all the boilerplate code.
    

        You should, of course, remind it to avoid SQL injection vulnerabilities.
    

      This blog is totally free, but if you like it, please consider supporting it.
- [You should add debug views to your DB](https://chrispenner.ca/posts/views-for-debugging?utm_source=tldrwebdev) [📖](https://read.readwise.io/read/01k3dw1jc9hce9knwm4vq30qsd) 👤 Chris Penner 💬 728 🔖 #db, #sql 🗓️ 2025-08-24
    > **Резюме:** Debugging often means repeating complex joins and getting ID-heavy rows. Add a debug view that pre-joins tables and exposes readable fields like project and branch names. Views save time, are easy to change, and work well for one-off queries despite minor index tradeoffs.
- [Оптимизация Запросов В Postgresql](https://readwise.io/reader/document_raw_content/33757448) [📖](https://read.readwise.io/read/01jy11ac8jpd6fyyyydq45vjw9) 👤 Домбровская Г, Новиков Б, Бейликова А 💬 61368 🔖 #sql, #book, #postgresql 🗓️ 2025-06-18
- [Postgresql. Профессиональный SQL](https://readwise.io/reader/document_raw_content/324141976) [📖](https://read.readwise.io/read/01jy1157ae1pcb35m51cwyqqk9) 👤 Евгений Моргунов 💬 98953 🔖 #sql, #book, #postgresql 🗓️ 2025-06-18
    > **Резюме:** The text discusses using statistical functions in PostgreSQL to analyze flight delays and ticket sales for an airline. It emphasizes the importance of accurate data and decision-making methods, such as the Pareto principle, in understanding financial patterns. Additionally, it covers optimizing query performance by accurately estimating the number of rows returned by functions in the database.
- [Postgresql Основы Языка SQL](https://readwise.io/reader/document_raw_content/20530573) [📖](https://read.readwise.io/read/01jy1149gxa18qk82beyq4tgr7) 👤 Е. П. Моргунов 💬 66946 🔖 #sql, #book, #postgresql 🗓️ 2025-06-18
    > **Резюме:** The text discusses various aspects of working with a database using PostgreSQL. It covers topics such as coordinating the creation of educational materials, accessing databases through applications, transactions in databases, handling null values in databases, creating views and indexes for performance optimization, executing queries, working with multiple tables, creating materialized views, transaction isolation levels, locking mechanisms, and improving performance through denormalization. It emphasizes the importance of understanding these concepts for efficient database management and query execution in PostgreSQL.
- [Life Altering Postgresql Patterns](https://mccue.dev/pages/3-11-25-life-altering-postgresql-patterns) [📖](https://read.readwise.io/read/01jqmaa1y0sw4pcg8659jm64h1) 👤 Ethan McCue 💬 1367 🔖 #sql, #postgresql 🗓️ 2025-03-30
    > **Резюме:** The article shares helpful PostgreSQL practices that can improve database management and usability. Key recommendations include using UUIDs for primary keys, adding created_at and updated_at timestamps, and employing soft deletes instead of permanent deletions. The author emphasizes naming conventions and the importance of schemas to maintain organization in larger applications.
- [SQL help from ChatGPT](https://leancrew.com/all-this/2025/03/sql-help-from-chatgpt/) [📖](https://read.readwise.io/read/01jq2cp9bfpa9fj60xq3jwbwfz) 👤 Dr. Drang 💬 2371 🔖 #llm, #sql 🗓️ 2025-03-23
    > **Резюме:** The author improved SQL queries for searching a database of books and authors. With help from ChatGPT, he learned to better combine results and reduce duplicates in his searches. He also created shell scripts to quickly find books by title or author.
