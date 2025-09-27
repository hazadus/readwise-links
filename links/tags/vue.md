# Ссылки

- Всего ссылок: 25

## Ссылки

- [Vue 3.5's onWatcherCleanup: Mastering Side Effect Management in Vue Applications](https://alexop.dev/posts/vue-35s-onwatchercleanup-mastering-side-effect-management-in-vue-applications/) 👤 Alexander Opalic 💬 688 🔖 #vue 🗓️ 2025-09-26
    > **Резюме:** Vue 3.5 adds onWatcherCleanup to attach cleanup logic directly inside watchers. It automatically aborts requests, clears timers, and removes listeners before reruns or when a watcher stops. This makes code clearer, reduces memory leaks, and fits cleanly into Vue’s reactivity system.
- [How to Structure Vue Projects](https://alexop.dev/posts/how-to-structure-vue-projects/) 👤 Alexander Opalic 💬 1740 🔖 #vue 🗓️ 2025-09-26
    > **Резюме:** This article explains different Vue project structures based on project size and complexity, such as flat structures for small projects and feature-sliced designs for large applications. It emphasizes that the right structure enhances scalability, maintainability, and team collaboration. Choosing the appropriate architecture is crucial as it should evolve with your organization's needs.
- [Atomic Architecture: Revolutionizing Vue and Nuxt Project Structure](https://alexop.dev/posts/atomic-design-vue-or-nuxt/) 👤 Alexander Opalic 💬 1176 🔖 #vue, #nuxt 🗓️ 2025-09-26
    > **Резюме:** Atomic Design organizes UI into atoms, molecules, organisms, templates, and pages to make components smaller and clearer. Applied to Vue/Nuxt, atoms are pure single-purpose components, molecules combine atoms, and organisms are larger reusable pieces. Refactoring a Todo app this way reduces duplication, simplifies testing, and improves maintainability.
- [Create a Native-Like App in 4 Steps: PWA Magic with Vue 3 and Vite](https://alexop.dev/posts/create-pwa-vue3-vite-4-steps/) 👤 Alexander Opalic 💬 1944 🔖 #pwa, #vue 🗓️ 2025-09-26
    > **Резюме:** This tutorial teaches you how to create a Progressive Web App (PWA) using Vue 3 and Vite in four simple steps. You will set up a Vue project, create necessary assets, configure Vite for PWA support, and implement offline functionality with service workers. By the end, you'll have a fully functional PWA that works across various devices and can be installed on users' home screens.
- [SQLite in Vue: Complete Guide to Building Offline-First Web Apps](https://alexop.dev/posts/sqlite-vue3-offline-first-web-apps-guide/) 👤 Alexander Opalic 💬 5636 🔖 #vue 🗓️ 2025-09-26
    > **Резюме:** The guide "SQLite in Vue" by Alexander Opalic teaches how to create offline-first web apps using SQLite in Vue.js. It covers key features like executing SQL commands and managing database connections. The guide is designed to help developers easily integrate SQLite into their applications.
- [How to Use the Variant Props Pattern in Vue](https://alexop.dev/posts/vue-typescript-variant-props-type-safe-props/) 👤 Alexander Opalic 💬 718 🔖 #vue 🗓️ 2025-09-26
    > **Резюме:** The Variant Props Pattern (VPP) in Vue uses TypeScript’s discriminated unions to create type-safe component variants. This approach prevents mixing incompatible props by marking unused properties as "never." It helps developers build components, like notifications, that manage different states without errors.
- [Building Local-First Apps with Vue and Dexie.js](https://alexop.dev/posts/building-local-first-apps-vue-dexie/) 👤 Alexander Opalic 💬 1354 🔖 #vue 🗓️ 2025-09-26
    > **Резюме:** This guide shows how to build local-first, offline-capable web apps using Vue 3 and Dexie.js. Dexie stores data in IndexedDB locally and uses Dexie Cloud for sync, auth, and conflict resolution. A todo app example and a repository pattern demonstrate setup, sync configuration, and best practices.
- [The Browser That Speaks 200 Languages: Building an AI Translator Without APIs](https://alexop.dev/posts/building-client-side-ai-translator-vue/) 👤 Alexander Opalic 💬 1247 🔖 #try, #vue, #webworkers 🗓️ 2025-09-26
    > **Резюме:** This guide shows how to build a free offline AI translator for 200 languages using Vue and Transformers.js. It runs Meta’s NLLB-200 model locally in a Web Worker and streams translation updates. The app includes language selectors, a progress bar, and a simple Vue interface.
- [Solving Prop Drilling in Vue: Modern State Management Strategies](https://alexop.dev/posts/solving-prop-drilling-in-vue/) 👤 Alexander Opalic 💬 798 🔖 #vue 🗓️ 2025-09-26
    > **Резюме:** Prop drilling makes code brittle, hard to debug, and slow.  
Use Pinia for app-wide state, composables for reusable logic, and provide/inject for scoped subtree sharing.  
Avoid event buses and prefer typed, testable patterns with DevTools support.
- [How to Do Visual Regression Testing in Vue with Vitest?](https://alexop.dev/posts/visual-regression-testing-with-vue-and-vitest-browser/) 👤 Alexander Opalic 💬 993 🔖 #vue, #vitest, #testing 🗓️ 2025-09-26
    > **Резюме:** Visual regression testing captures screenshots of Vue components and compares them to baseline images to catch unintended UI changes. Vitest’s experimental browser mode with Playwright renders stories in a real browser, takes screenshots, and compares them to baselines. It needs extra config and manual diff review, but helps keep the UI consistent and lets designers inspect changes.
- [What are Effect Scopes in Vue?](https://michaelnthiessen.com/what-are-effect-scopes-in-vue?ck_subscriber_id=2108193410&utm_campaign=%F0%9F%94%A5+(230)+What+are+Effect+Scopes+in+Vue?+-+18611005&utm_medium=email&utm_source=convertkit) 👤 michaelnthiessen.com 💬 1063 🔖 #vue, #nuxt 🗓️ 2025-08-13
    > **Резюме:** Effect scopes in Vue group related reactive effects so they can be stopped and cleaned up easily. This helps prevent memory leaks and bugs by controlling how long effects live. They are used inside components and also for advanced patterns like shared composables.
- [Bulletproof Watchers in Vue](https://michaelnthiessen.com/bulletproof-watchers-in-vue?ck_subscriber_id=2108193410&utm_source=convertkit&utm_medium=email&utm_campaign=Bulletproof+Watchers+in+Vue+(no+more+leaks+or+duplicate+effects)+-+18562994) 👤 michaelnthiessen.com 💬 1040 🔖 #vue, #nuxt, #toot, #webdev, #programming 🗓️ 2025-08-09
    > **Заметка:** Дельные советы от Майкла по работе с watch()
    > **Резюме:** Vue watchers can leak memory by creating overlapping effects like timers or API calls when reactive data changes quickly. Using the onCleanup function lets you cancel old effects before new ones start, preventing leaks and bugs. Vue 3.5 added onWatcherCleanup to manage multiple cleanups easily, making watchers more reliable and your app faster.
- [12 Design Patterns in Vue](https://michaelnthiessen.com/12-design-patterns-vue) 👤 michaelnthiessen.com 💬 1662 🔖 #try, #vue, #nuxt, #toot, #webdev, #patterns, #programming 🗓️ 2025-08-04
    > **Заметка:** Краткая и ёмкая подборка паттернов разработки с Vue от Майкла. Очень качественный материал!
    > **Резюме:** The article discusses 12 design patterns specifically for Vue, highlighting their importance in writing maintainable code. It introduces concepts like Thin Composables, Humble Components, and the Strategy Pattern, showing how to simplify and organize Vue applications. For more detailed examples and additional patterns, readers can explore further resources provided in the article.
- [Vercel BUYING NuxtLabs - What it means for you!](https://www.youtube.com/watch?v=NiQB7QPJAiM) 👤 Alexander Lichter 🔖 #vue, #nuxt 🗓️ 2025-07-13
    > **Резюме:** This week's acquisition of NuxtLabs was a suprise for most of us - but what does it mean for Nuxt as a framework, for the community and for YOU?!

Disclaimer: This video shares my own opinion and not the official stance of VoidZero nor the Nuxt core team as a whole.

---
Links and Resources

🔗 NuxtLabs announcement 
🎙 Full @DejaVueFm episode with Daniel and Sébastien https://www.youtube.com/watch?v=xHbjFW9EJ-8
🔗 Nuxt Governance document https://github.com/nuxt/governance
🔗 Nitro Governance document https://github.com/nitrojs/governance/blob/main/README.md
🔗 Daniel's Reddit AMA https://www.reddit.com/r/vuejs/comments/1lvdkwr/i_lead_the_nuxt_core_team_ama/

---
Chaptermarks
00:00 Intro
00:21 What happened?
01:17 Am I part of Vercel now?
01:29 Did I know about the acquisition?
01:57 NuxtLabs IS NOT Nuxt
02:45 What does it mean for NuxtLabs?
03:20 What will happen with the products of NuxtLabs?
05:06 What does it mean for Nuxt as a framework?
10:08 Consequences for Nitro and UnJS
11:26 What changes for Vue?
12:09 What is in for Vercel?
13:35 Who are the "winners" of this acquisition?
14:10 And who are the "losers"?
15:16 Addressing Worries
16:42 Wrapping Up

---

Links marked with * are affiliate links. I get a small commission when you register for the service or buy the product through my link. This helps me keeping the channel running. I only include affiliate links for services or product mentioned that we use ourselves or have good experience with.
- [More Features of Vue's VS Code Extension](https://www.youtube.com/watch?v=RcPcO4_Ct_U) 👤 Alexander Lichter 🔖 #vue 🗓️ 2025-07-03
    > **Резюме:** The Vue VS Code extension helps you add components easily and shows helpful hints about missing properties. It also supports reactive props and auto-adds ".value" for refs, saving time. Premium features include visualizing reactivity, focus mode, and highlighting template changes to improve coding clarity.
- [How Vue Composables Work – Explained with Code Examples](https://www.freecodecamp.org/news/how-vue-composables-work/) 👤 freeCodeCamp.org 💬 1767 🔖 #vue 🗓️ 2025-06-14
    > **Резюме:** Vue composables are tools that allow developers to reuse stateful logic across different components in a Vue application. They help manage logic that changes over time, making code easier to maintain. By extracting this logic into composables, developers can keep their applications organized while ensuring each component has its own state.
- [Шпаргалка по VueUse: когда использовать какую функцию](https://hazadus.ru/blog/vueuse-cheat-sheet) 👤 hazadus.ru 💬 1754 🔖 #vue 🗓️ 2025-05-28
    > **Резюме:** The document provides a summary of key functions in VueUse. It explains when to use each function effectively. This helps developers choose the right tools for their projects.
- [Rendering Mechanism](https://vuejs.org/guide/extras/rendering-mechanism#:~:text=The%20main%20benefit%20of%20virtual%20DOM%20is,the%20direct%20DOM%20manipulation%20to%20the%20renderer.) 👤 vuejs.org 💬 1600 🔖 #vue 🗓️ 2025-05-25
    > **Резюме:** Vue.js - The Progressive JavaScript Framework
- [Building charts in Vue with D3](https://dev.to/jacobandrewsky/building-charts-in-vue-with-d3-38gl) 👤 dev.to 💬 736 🔖 #vue 🗓️ 2025-05-19
    > **Резюме:** This guide explains how to create interactive charts using Vue.js and D3.js. Vue manages the app's state, while D3 handles the actual data visualization. By combining these tools, you can build dynamic and responsive data visualizations for web applications.
- [Extracting Composables for Code Organization ​](https://vuejs.org/guide/reusability/composables.html) 👤 vuejs.org 💬 2447 🔖 #vue, #nuxt 🗓️ 2025-04-09
    > **Резюме:** Vue.js - The Progressive JavaScript Framework
- [Good practices and Design Patterns for Vue Composables](https://dev.to/jacobandrewsky/good-practices-and-design-patterns-for-vue-composables-24lk) 👤 dev.to 💬 1140 🔖 #vue, #nuxt 🗓️ 2025-04-09
    > **Резюме:** I recently had a great discussion with my team at Vue Storefront about patterns for writing Vue...
- [FastAPI и Vue.js 3: телеграм-бот с MiniApp для записи и автоматических уведомлений. Пишем фронтенд](https://habr.com/ru/companies/amvera/articles/874970/) 👤 yakvenalex 💬 7955 🔖 #try, #vue, #fastapi, #miniapp, #telegram 🗓️ 2025-01-21
    > **Резюме:** The article discusses creating a Telegram bot using FastAPI and Vue.js 3, focusing on frontend development. It highlights the importance of setting up a structured project with components and routers for better code reusability and navigation. The guide also covers preparing user interfaces for booking appointments with doctors within the application.
- [Пишем морской бой на VueJS и Python](https://habr.com/ru/articles/874188/) 👤 Green21 💬 5065 🔖 #vue, #fastapi, #websocket 🗓️ 2025-01-20
    > **Резюме:** The article explains how to create the popular game "Battleship" using VueJS and Python. Players must enter a nickname and complete a simple captcha before arranging their ships on the grid. The game continues until one player sinks all of the opponent's ships, and players can restart by refreshing the page.
- [Build 3D Scenes Declaratively with TresJS using Vue - AlvaroSabu](https://alvarosaburido.dev/blog/build-3d-scenes-declaratively-with-tresjs-using-vue?ck_subscriber_id=2108193410) 👤 alvarosaburido.dev 💬 1119 🔖 #vue 🗓️ 2025-08-02
    > **Резюме:** TresJS simplifies creating 3D scenes using Vue components, making web development more accessible. It allows developers to build visually stunning 3D experiences with less code and hassle. This tutorial will guide you through the basics of TresJS and help you create your first 3D scene.
- [Building a VS Code Extension Using Vue.js](https://www.codemag.com/article/2107071?ck_subscriber_id=2108193410) 👤 CODE Magazine, EPS Software Corp., <a href="/People/Bio/Bilal.Haidar">Bilal Haidar</a> 💬 6594 🔖 #vue 🗓️ 2024-09-11
    > **Резюме:** This article explains how to build a Visual Studio Code extension using Vue.js and the Webview API. It guides readers through creating a VS Code command to open a Vue.js app inside a Webview and shows how to communicate between the extension and the app. The process includes setting up project files and using special URIs to load resources effectively.
