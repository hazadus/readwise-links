# Ссылки

- Всего ссылок: 8

## Ссылки

- [Using Playwright to test my static sites](https://alexwlchan.net/2026/playwright/?ref=rss) [📖](https://read.readwise.io/read/01kqknwedwzekqrn1jqhc2qkfg) 👤 alexwlchan 💬 1509 🔖 #testing, #frontend, #playwright 🗓️ 2026-05-02
    > **Заметка:** Интересно будет попробовать, когда соберусь блог возрождать. 
    > **Резюме:** I build a lot of static websites – including this site and all of my local media archives – and I want to test them.
Most of my pages are static HTML and I can write automated tests that analyse the HTML, but for more complex sites I have JavaScript that runs in the browser and modifies the page.
The only way to test that functionality is to open the page in a browser, click around, and see what happens.
I could do that manually, but it quickly gets tedious.
To automate this process, I’ve been using a testing framework called Playwright, which is designed for this sort of end-to-end testing.
It’s a tool that allows you to programatically control a web browser, look at the contents of a page, and make assertions about what’s there.
Playwright can be used to test or script any kind of web app; I’m using it for static sites because those are the only web apps I have.
Playwright is available as a CLI, or there are libraries to use it with TypeScript, Python, .NET, and Java.
All my other tests are written in Python, so that’s what I’m using.
Writing a basic test with Playwright
To set up Playwright with Python, you install the playwright library using pip or uv, then install a web browser for Playwright to control.
(You can’t use Playwright with the browser you use day-to-day; you need special binaries with control hooks.)
I use Safari as my main browser, and Safari is based on WebKit, so let’s install that:
$ uv pip install playwright
$ python3 -m playwright install webkit
Then we can start writing tests.
Here’s a basic test in which Playwright launches WebKit, opens example.com, and checks the text Example domain is visible on the page:
from playwright.sync_api import expect, sync_playwright


def test_basic_playwright() -> None:
    """
    Run a basic test with Playwright: load a web page and check it
    contains the expected text.
    """
    with sync_playwright() as p:
        browser = p.webkit.launch()

        page = browser.new_page()
        page.goto("ht...
- [A Modern Quality Pipeline and Testing Strategy for Frontend Projects](https://alexop.dev/posts/modern-frontend-quality-pipeline/) [📖](https://read.readwise.io/read/01kq2k3gnqeh877w7kgfrnzs8a) 👤 alex.opalic.dev@gmail.com (Alexander Opalic) 💬 3222 🔖 #try, #testing, #frontend 🗓️ 2026-04-25
    > **Заметка:** Продуманная, подробная система тестирования фронтенда на всех уровнях. Для использования при работе над проектами со сложным фронтом.
    > **Резюме:** A modern frontend quality pipeline uses fast tools like Vite+, Oxlint, and Vitest to catch bugs early and run tests efficiently. It splits checks by cost and stage, from editor to CI and preview deployments, ensuring consistent quality across teams. This approach combines types, linting, unit, component, and end-to-end tests with automation to keep code reliable and easy to maintain.
- [Exploratory QA with AI Agents: Building a Site-Agnostic Harness](https://alexop.dev/posts/exploratory-qa-ai-agents-site-agnostic-harness/) [📖](https://read.readwise.io/read/01kpkpxp6w1s029akh17na8pr0) 👤 alex.opalic.dev@gmail.com (Alexander Opalic) 💬 2529 🔖 #codex, #agents, #claude, #testing, #frontend 🗓️ 2026-04-19
    > **Резюме:** A thin Bun runner that hands a coding agent one charter and lets it drive a real browser through an exploratory QA session. Works with Claude, Codex, or Copilot, and any browser CLI.
- [Pikaday](https://pikaday.dbushell.com/?utm_source=tldrwebdev) [📖](https://read.readwise.io/read/01ka9qy0skrkd3wx8b1qnvpn1d) 👤 David Bushell 💬 954 🔖 #html, #frontend 🗓️ 2025-11-17
    > **Заметка:** Подборка примеров полей ввода для дат
    > **Резюме:** Most sites do not need a JavaScript calendar; simpler native inputs or separate fields work better. Native date/time inputs are easier, more accessible, and less error-prone than custom widgets. Keep designs simple, test with real users, and prefer progressive enhancement.
- [How Functional Programming Shaped (and Twisted) Frontend Development](https://alfy.blog/2025/10/04/how-functional-programming-shaped-modern-frontend.html?utm_campaign=Django%2BNewsletter&utm_medium=email&utm_source=Django_Newsletter_308) [📖](https://read.readwise.io/read/01k8ew1w60rexs61srah3wm0gp) 👤 Ahmad Elalfy 💬 4008 🔖 #webdev, #frontend 🗓️ 2025-10-25
    > **Резюме:** Functional programming ideals and React pushed developers to rebuild core browser features in JavaScript. This made many sites more complex, fragile, and slower while ignoring the web’s built-in strengths like HTML, CSS, and native events. Newer tools aim to restore platform-first patterns and progressive enhancement.
- [Stop Ignoring the Browser: The Biggest Frontend Shift in a Decade](https://thenewstack.io/stop-ignoring-the-browser-the-biggest-frontend-shift-in-a-decade/?utm_source=tldrwebdev) [📖](https://read.readwise.io/read/01k81g41w57wrhnmd9czngqgy4) 👤 Alexander T. Williams 💬 1141 🔖 #webdev, #frontend 🗓️ 2025-10-20
    > **Резюме:** Browsers are gaining built-in features that used to only exist in frameworks. This reduces the need for heavy framework layers and improves performance. Frameworks will stay for ergonomics, but their dominance is fading.
- [How to Build Your Own Vue-like Reactivity System from Scratch](https://alexop.dev/posts/how-to-build-your-own-vue-like-reactivity-system-from-scratch/) [📖](https://read.readwise.io/read/01k62y4dz0e5pg996cw8bbdxjf) 👤 Alexander Opalic 💬 777 🔖 #try, #vue, #frontend, #typescript 🗓️ 2025-09-26
    > **Резюме:** The article builds simple ref() and watchEffect() functions to show how Vue-style reactivity works. It explains tracking dependencies with track, triggering updates with trigger, and storing effects in a depMap. The minimal system shows core concepts but omits production features like nested handling and optimizations.
- [If Not React, Then What?](https://infrequently.org/2024/11/if-not-react-then-what/) [📖](https://read.readwise.io/read/01je317cp64m1mdrsvcmnf5std) 👤 Infrequently Noted 💬 9376 🔖 #frontend 🗓️ 2024-12-02
    > **Резюме:** The author argues that despite React being outdated technology, it is still widely used in new applications, causing performance and accessibility issues. They suggest that teams should prioritize HTML and CSS over JavaScript to improve user experience and reduce costs. Ultimately, the focus should be on understanding user needs rather than sticking to familiar frameworks like React.
