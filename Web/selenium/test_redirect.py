#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/11/1 16:56
# @Author:  haiyong
# @File:    test_redirect.py
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