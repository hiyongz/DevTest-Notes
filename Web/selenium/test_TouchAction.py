#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/4 19:16
# @Author:  haiyong
# @File:    test_TouchAction.py
from selenium import webdriver
from selenium. webdriver import TouchActions
from time import sleep
class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self. driver.quit()

    def test_touchaction_scrollbottom(self):
        """
        打开 Chrome
        打开 url : http: //www, baidu, com
        向搜索框中输入selenium测试
        通过 TouchAction点击搜索框
        滑动到底部,点击下一页
        关闭 Chrome
        return:
        """
        self.driver.get("http://www.baidu.com")
        input = self.driver.find_element_by_id("kw")
        search = self.driver.find_element_by_id("su")
        input.send_keys("test")
        action = TouchActions(self.driver)
        action.tap(search)
        action.perform()
        action.scroll_from_element(input, 0, 10000).perform()
        next = self.driver.find_element_by_link_text("下一页 >")
        next.click()
        sleep(3)









