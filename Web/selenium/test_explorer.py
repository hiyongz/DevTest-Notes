#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/5 10:36
# @Author:  haiyong
# @File:    test_explorer.py
import os

from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest


class Testbrowser():
    def setup(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome(executable_path=(r'D:/testing_tools/chromedriver83/chromedriver.exe'))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_test(self):
        # 百度搜索测试
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("test")
        # self.driver.find_element(By.ID,'kw').send_keys("test")
        # self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("test")
        # self.driver.find_element(By.CSS_SELECTOR,'id=kw').send_keys("test")
        self.driver.find_element(By.ID, 'su').click()
