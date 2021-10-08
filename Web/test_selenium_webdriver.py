#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/5/20 16:07
# @File:    test_selenium_webdriver.py
import json
import time
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class TestWeixin:
    def setup(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(executable_path="D:/testing_tools/chromedriver88/chromedriver.exe")
        self.driver.implicitly_wait(10)
    def teardown_method(self):
        self.driver.quit()

    def test_weixin(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.ID, 'kw')
        ele.send_keys("test")
        time.sleep(2)
        self.driver.find_element(By.ID, 'su').click()
        time.sleep(2)
        assert self.driver.title == 'test_百度搜索'      