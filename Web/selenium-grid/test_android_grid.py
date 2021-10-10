#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/3 15:39
# @Author:  hiyongz
# @File:    test_grid.py
import os

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common import utils


class TestGrid:
    def setup(self):
        udid = os.getenv("udid")
        desired_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'deviceName': '127.0.0.1:7555',
            'appPackage': 'com.xueqiu.android',
            'appActivity': 'com.xueqiu.android.common.MainActivity',
            'noReset': True,
            # 'udid': "127.0.0.1:7555",
            'udid': udid,
            # 'systemPort': utils.free_port(),
            # 'appActivity': 'com.xueqiu.android.view.WelcomeActivityAlias',
            'automationName': 'Uiautomator2'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # self.driver = webdriver.Remote('http://192.168.0.107:4444/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def testcase1(self):
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys("zhaoshan")
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.xueqiu.android:id/stockCode' and @text='SH600036']").click()












