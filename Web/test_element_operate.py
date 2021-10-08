#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/9/4 15:32
# @Author:  haiyong
# @File:    test_element_operate.py
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLocator():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_demo1(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("test")
        sleep(2)
        baidu = self.driver.find_element_by_id("su")
        baidu.click()
        print(baidu.get_attribute("type"))
        print(baidu.get_attribute("id"))
        print(baidu.get_attribute("value"))
        print(baidu.get_attribute("class"))