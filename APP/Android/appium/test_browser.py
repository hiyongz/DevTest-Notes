#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/19 10:25
# @Author:  haiyong
# @File:    test_browser.py
from appium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestBrowser():
    def setup(self):
        desired_caps = {
            'platformName': 'android',
            'deviceName': 'CUYDU19626004019',
            'platformVersion': '10',
            'browserName':'Chrome',
            'noReset':True,
            'automationName': 'Uiautomator2',
            'chromedriverExecutable': 'D:/testing_tools/chromedriver86/chromedriver.exe'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("https://m.baidu.com")
        sleep(5)
        # self.driver.find_element_by_id("index-kw").click()
        # sleep(5)
        self.driver.find_element_by_id("index-kw").send_keys("test")
        search_locater = (By.ID,"index-bn")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(search_locater))
        self.driver.find_element(*search_locater).click()
        sleep(5)
