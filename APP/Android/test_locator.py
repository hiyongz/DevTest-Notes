#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/11/7 22:33
# @Author:  haiyong
# @File:    test_locator.py

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWebDriverWait:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        # desired_caps['appPackage'] = 'com.xueqiu.android'
        # desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = '.ApiDemos'
        desired_caps['automationName'] = 'Uiautomator2'
        desired_caps['newCommandTimeout'] = 3000
        desired_caps['noReset'] = True
        desired_caps['dontStopAppOnReset'] = True
        desired_caps['skipDeviceInitialization'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeybBoard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        pass
        # self.driver.quit()

    def test_locator(self):
        # self.driver.find_element_by_xpath('//*[@text="行情"]').click()
        # self.driver.find_element_by_id("com.xueqiu.android:id/enter_stock_fund").click()
        # self.driver.find_element_by_accessibility_id("Accessibility").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/enter_stock_fund")
        self.driver.find_element_by_class_name()

