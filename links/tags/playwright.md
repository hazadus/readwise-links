# Ссылки

- Всего ссылок: 1

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
