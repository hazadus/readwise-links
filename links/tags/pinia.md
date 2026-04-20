# Ссылки

- Всего ссылок: 4

## Ссылки

- [How to Write Better Pinia Stores with the Elm Pattern](https://alexop.dev/posts/tea-architecture-pinia-private-store-pattern/) [📖](https://read.readwise.io/read/01k6spqky070m84y1yjesaf2zy) 👤 Alexander Opalic 💬 1404 🔖 #pinia 🗓️ 2025-10-05
    > **Резюме:** Pinia is flexible but allows direct, unpredictable state mutations that hurt testability.  
Combine The Elm Architecture with a private store or Vue's readonly to keep update logic pure and expose only selectors and a dispatch.  
Prefer readonly for simplicity; the pattern gives testable, framework-agnostic business logic with Pinia devtools support.
- [Solving Prop Drilling in Vue: Modern State Management Strategies](https://alexop.dev/posts/solving-prop-drilling-in-vue/) [📖](https://read.readwise.io/read/01k62j88e860fj11r58fytgdkm) 👤 Alexander Opalic 💬 798 🔖 #vue, #toot, #pinia, #webdev 🗓️ 2025-09-26
    > **Резюме:** Prop drilling makes code brittle, hard to debug, and slow.  
Use Pinia for app-wide state, composables for reusable logic, and provide/inject for scoped subtree sharing.  
Avoid event buses and prefer typed, testable patterns with DevTools support.
- [Nuxt 3 State Management: Pinia vs useState](https://www.vuemastery.com/blog/nuxt-3-state-mangement-pinia-vs-usestate/?ck_subscriber_id=2108193410&utm_source=convertkit&utm_medium=email&utm_campaign=%F0%9F%94%A5%20%28235%29%20Hidden%20Component%20Pattern,%20UI%20states,%20and%20Dedupe%20fetches%20in%20Nuxt%20-%2019014881) [📖](https://read.readwise.io/read/01k619gqejx525bnn6xy856vnm) 👤 Michael Thiessen 💬 1760 🔖 #nuxt, #pinia 🗓️ 2025-09-25
    > **Резюме:** useState fixes ref issues: cross-request pollution, hydration, and sharing. Pinia adds devtools, organized stores, actions, and getters for a better developer experience. Use Pinia for complex apps and useState for small, simple apps.
- [Nuxt Tip: Accessing Pinia Store in Production Build](https://mokkapps.de/vue-tips/accessing-pinia-store-in-nuxt-production-build) [📖](https://read.readwise.io/read/01k2me5zfka4jnzw413rt952d1) 👤 Michael Hoffmann 💬 86 🔖 #nuxt, #pinia 🗓️ 2025-08-14
    > **Резюме:** In local development, you can easily debug your Pinia store with Nuxt Devtools. In production builds, accessing the Pinia store requires a different command in the browser console. Follow the author on BlueSky or subscribe to the newsletter for more Vue and Nuxt tips.
