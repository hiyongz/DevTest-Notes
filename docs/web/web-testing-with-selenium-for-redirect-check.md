# selenium URL重定向检查


有时候需要测试URL重定向是否正确，本文介绍一种使用selenium测试URL重定向的方法。


重定向的最直接表现是URL地址发生了变化，所有主要思路就是检查URL地址是否跳转成功。selenium检测URL变化可以使用`expected_conditions` 方法：
```python
from selenium.webdriver.support import expected_conditions as EC

EC.url_changes(current_url) # 检查URL是否改变
EC.url_to_be(new_url) # 检查重定向的URL
EC.url_contains('text') # 检查URL是否包含text
EC.url_matches() # 是否匹配
EC.title_is('New page Title') # 检查标题
EC.title_contains('text')
```

可以使用WebDriverWait方法等待URL是否重定向成功，具体实现请看下面的示例：
```python
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class TestRedirect():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.0.1/")
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_redirect(self, url="http://www.baidu.com", redrect_url="http://www.baidu.com/err_noWan.html", redrect=True,
                      timeout=5):

        js = "window.open('%s')" % url
        self.driver.execute_script(js)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1]) # 切换到新打开的窗口

        element = EC.url_changes(url)  # 判断是否重定向

        try:
            WebDriverWait(self.driver, timeout).until(element)
            flag1 = element(self.driver)
        except:
            flag1 = element(self.driver)

        assert flag1 == True

        element = EC.url_to_be(redrect_url)  # 判断是否符合
        try:
            WebDriverWait(self.driver, timeout).until(element)
            flag2 = element(self.driver)
        except:
            flag2 = element(self.driver)

        assert flag2 == True

        self.driver.close()  # 关闭新打开的窗口
        self.driver.switch_to.window(windows[0]) # 切回窗口
```



