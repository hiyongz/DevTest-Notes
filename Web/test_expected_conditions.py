#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/12 10:45
# @Author:  haiyong
# @File:    test_expected_conditions.py
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestExpectedConditions():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver. quit()

    def test_url(self):
        self.driver.get("https://www.baidu.com")
        # WebDriverWait(self.driver, 10).until(lambda driver: self.driver.current_url == "http://www.website.com/wait.php")
        # EC.url_changes
        # element = EC.url_to_be('https://www.baidu.com/')  # 判断是否符合
        element = EC.url_changes('https://www.baidu.com/')  # 判断是否符合
        # print(self.driver.current_url)
        WebDriverWait(self.driver, 10).until(element)
        assert element(self.driver) == True

        # EC.alert_is_present()(self.driver)






















