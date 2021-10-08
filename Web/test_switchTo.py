#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/9/4 16:45
# @Author:  haiyong
# @File:    test_switchTo.py
import time

from selenium import webdriver


class TestElementFocus():
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=(r'D:/testing_tools/chromedriver89/chromedriver.exe'))
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_element_focus(self):
        self.driver.get("https://www.baidu.com/")
        baidu = self.driver.find_element_by_id("kw")
        assert baidu == self.driver.switch_to.active_element
