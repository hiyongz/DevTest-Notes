# Web自动化测试之playwright：设置浏览器语言
playwright支持基于Chromium内核的Google Chrome 和 Microsoft Edge浏览器, WebKit内核的Apple Safari 和 Mozilla Firefox浏览器，可以对浏览器的语言进行设置，可用来测试产品的语言自适应功能。


playwright设置浏览器语言比selenium更简洁，创建浏览器上下文时设置一下 `locale` 参数：

```python
browser.new_context(locale="zh-CN")
```

chrome浏览器语言设置示例：
```python
from playwright.sync_api import sync_playwright

class TestBrowser():

    def setup(self):
        self.playwright = sync_playwright().start()

    def teardown(self):
        self.browser.close()

    def test_chrome(self):
        self.browser = self.playwright.chromium.launch(channel="chrome", headless=False)
        context = self.browser.new_context(locale="zh-CN") # zh-CN、en-GB
        page = context.new_page()
        page.goto("https://www.baidu.com/")
        lan = page.evaluate("window.navigator.language;")
        print(lan)
        assert lan == "zh-CN"
```

Edge，WebKit，Firefox浏览器类似：

```python
def test_edge(self):
	self.browser = self.playwright.chromium.launch(channel="msedge", headless=False)
	context = self.browser.new_context(locale="de-DE")
	page = context.new_page()
	page.goto("https://www.baidu.com/")
	lan = page.evaluate("window.navigator.language;")
	print(lan)
	assert lan == "de-DE"


def test_firefox(self):
	self.browser = self.playwright.firefox.launch(headless=False)
	context = self.browser.new_context(locale="de-DE")
	page = context.new_page()
	page.goto("https://www.baidu.com/")
	lan = page.evaluate("window.navigator.language;")
	print(lan)
	assert lan == "de-DE"


def test_webkit(self):
	self.browser = self.playwright.webkit.launch(headless=False)
	context = self.browser.new_context(locale="de-DE")
	page = context.new_page()
	page.goto("https://www.baidu.com/")
	lan = page.evaluate("window.navigator.language;")
	print(lan)
	assert lan == "de-DE"
```

上面是同步版本，也可以写成异步方式：

```python
import asyncio
import time

from playwright.async_api import async_playwright


async def test_chrome():
    print('test_chrome start')
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(locale="en-US")  # zh-CN、en-GB
        page = await context.new_page()
        await page.goto("https://www.baidu.com/")
        lan = await page.evaluate("window.navigator.language;")
        assert lan == "en-US"
        await browser.close()
    print('test_chrome done')


async def test_edge():
    print('test_edge start')
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="msedge", headless=False)
        context = await browser.new_context(locale="en-US")  # zh-CN、en-GB
        page = await context.new_page()
        await page.goto("https://www.baidu.com/")
        lan = await page.evaluate("window.navigator.language;")
        assert lan == "en-US"
        await browser.close()
    print('test_edge done')


async def test_firefox():
    print('test_firefox start')
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        context = await browser.new_context(locale="en-US")  # zh-CN、en-GB
        page = await context.new_page()
        await page.goto("https://www.baidu.com/")
        lan = await page.evaluate("window.navigator.language;")
        assert lan == "en-US"
        await browser.close()
    print('test_firefox done')


async def test_webkit():
    print('test_webkit start')
    async with async_playwright() as p:
        browser = await p.webkit.launch(headless=False)
        context = await browser.new_context(locale="en-US")  # zh-CN、en-GB
        page = await context.new_page()
        await page.goto("https://www.baidu.com/")
        lan = await page.evaluate("window.navigator.language;")
        assert lan == "en-US"
        await browser.close()
    print('test_webkit done')


async def main():
    task1 = asyncio.create_task(test_chrome())
    task2 = asyncio.create_task(test_edge())
    task3 = asyncio.create_task(test_firefox())
    task4 = asyncio.create_task(test_webkit())
    tasks = [task1, task2, task3, task4]
    print('before await')
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
end = time.time()
print('Running time: %s Seconds' % (end - start))
```

执行结果：

```python
before await
test_chrome start
test_edge start
test_firefox start
test_webkit start
test_chrome done
test_edge done
test_webkit done
test_firefox done
Running time: 17.376961946487427 Seconds
```

不同国家的语言代码可参考：[https://developers.google.com/admin-sdk/directory/v1/languages](https://developers.google.com/admin-sdk/directory/v1/languages)



