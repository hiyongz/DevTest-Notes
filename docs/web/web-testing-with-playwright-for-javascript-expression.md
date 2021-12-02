# Web自动化测试之playwright：执行JavaScript脚本


在[Selenium执行JavaScript脚本](https://blog.csdn.net/u010698107/article/details/111415957)中介绍了Selenium执行JavaScript脚本的方法，playwright也支持执行JavaScript脚本，playwright本身就是一个Node.js库，本文介绍playwright-python执行js脚本的方法。



playwright-python使用 `evaluate()` 方法来执行JavaScript脚本，和selenium类似，也有两种方法实现元素操作。

- page.evaluate()：直接执行完整的JavaScript脚本。
- locator.evaluate()：定位到元素后再使用JavaScript执行操作。

## page.evaluate()

在浏览器上下文中执行：

```python
page.evaluate(expression, **kwargs)
```

示例代码：

```python
from playwright.sync_api import sync_playwright

class TestJs():
    def setup(self):
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def teardown(self):
        self.browser.close()

    def test_case1(self):
        self.page.goto("https://www.baidu.com/")
        # 获取浏览器语言
        lan = self.page.evaluate("window.navigator.language;")
        assert lan == "zh-CN"

        # 获取当前浏览器标题："百度一下，你就知道"
        title = self.page.evaluate("document.title;")
        assert title == self.page.title()

        self.page.evaluate('document.getElementById("kw").value = "test"') # 搜索框输入“test”
        text = self.page.evaluate("document.getElementById('kw').value") # 读取输入的值
        assert text == "test"

        self.page.evaluate('document.getElementById("su").click()')  # 点击 【百度一下】；page.click("text=百度一下")
        self.page.click("#page >> text=2")
```

## locator.evaluate()

先定位到元素后再进行js操作：

```python
handle = page.query_selector("id=kw")
handle.evaluate('node => node.value = "test"')
```

下面来看一个例子，实现上面代码中的操作：输入“test”，点击【百度一下】

```python
def test_case2(self):
	self.page.goto("https://www.baidu.com/")

	# 搜索框输入“test”
	input_handle = self.page.query_selector("id=kw")
	input_handle.evaluate('node => node.value = "test"')

	text = input_handle.evaluate('node => node.value') # 读取输入的值
	print(text)
	assert text == "test"

	# 点击 【百度一下】
	submit_handle = self.page.query_selector("id=su")
	submit_handle.evaluate('node => node.click()')
	time.sleep(10)
```



