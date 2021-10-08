#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/5 9:20
# @Author:  haiyong
# @File:    test_window.py
from time import sleep
from selenium import webdriver

# 多窗口切换
class Testwindows():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver. quit()

    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        self. driver.find_element_by_link_text("立即注册").click()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        windows=self.driver.window_handles
        print(windows)
        # 切换到注册窗口
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("12345678")
        sleep(2)
        # 切换回登录窗口
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("pwd")
        self.driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
        sleep(2)

    def test_window2(self):
        self.driver.get("http://www.baidu.com")
        js = "window.open('http://www.sogou.com')"
        self.driver.execute_script(js)
        sleep(3)
        windows = self.driver.window_handles
        print(windows)
        # 切换到新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id("query").send_keys("test sogou") # 搜狗搜索框
        sleep(3)
        self.driver.close() # 关闭新打开的窗口
        # 切回窗口
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id("kw").send_keys("test baidu") # 百度搜索框
        sleep(3)




















