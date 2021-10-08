#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/11/8 16:50
# @Author:  haiyong
# @File:    test_attribute.py

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

class TestWebDriverWait:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'CUYDU19626004019'
        # desired_caps['appPackage'] = 'com.xueqiu.android'
        # desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = '.ApiDemos'
        desired_caps['automationName'] = 'Uiautomator2'
        desired_caps['newCommandTimeout'] = 3000
        # desired_caps['noReset'] = True
        desired_caps['dontStopAppOnReset'] = True
        desired_caps['skipDeviceInitialization'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeybBoard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        # pass
        self.driver.quit()

    def test_locator(self):

        elem = self.driver.find_element_by_xpath('//*[@text="App"]')
        print("text:" + elem.get_attribute("text"))
        print("resource-id:" + elem.get_attribute("resource-id"))
        print("class:" + elem.get_attribute("class"))
        print("package:" + elem.get_attribute("package"))
        print("content-desc:" + elem.get_attribute("content-desc"))
        print("bounds:" + elem.get_attribute("bounds"))
        print("checkable:" + elem.get_attribute("checkable"))
        print("checked:" + elem.get_attribute("checked"))
        print("clickable:" + elem.get_attribute("clickable"))
        print("enabled:" + elem.get_attribute("enabled"))
        print("password:" + elem.get_attribute("password"))
        print("displayed:" + elem.get_attribute("displayed"))
        print("######################")
        print("text:" + elem.text)
        print(elem.location)
        print(elem.size)
        print(elem.is_displayed)
        print(elem.is_enabled)
        print(elem.is_selected)
