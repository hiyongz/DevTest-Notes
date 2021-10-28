

from playwright.sync_api import sync_playwright
import time

class TestBrowser():
    def test_chrome(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=False)
            page = browser.new_page()
            page.goto("https://www.baidu.com/")
            print(page.title())

    def test_edge(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="msedge", headless=False)
            page = browser.new_page()
            page.goto("https://www.baidu.com/")
            print(page.title())

    def test_firefox(self):
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.baidu.com/")
            print(page.title())

    def test_webkit(self):
        with sync_playwright() as p:
            browser = p.webkit.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.baidu.com/")
            print(page.title())

b = TestBrowser()
b.test_chrome()
b.test_edge()
b.test_firefox()
b.test_webkit()


# with sync_playwright() as p:
#     # for br in [p.chromium, p.firefox, p.webkit]:
#     #     browser = br.launch(headless=False)
#     #     # browser = p.chromium.launch(headless=False)
#     #     # browser = p.webkit.launch(headless=False)
#     #     # browser = p.firefox.launch(headless=False)
#     #     page = browser.new_page()
#     #     page.goto("https://www.baidu.com/")
#     #     print(page.title())
#     #     browser.close()
#     browser = p.chromium.launch(channel="msedge", headless=False)
#     page = browser.new_page()
#     page.goto("https://www.baidu.com/")
#     print(page.title())


