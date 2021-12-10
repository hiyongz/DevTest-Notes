#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/9/28 13:43
# @Author:  haiyong
# @File:    test_appium.py

from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAppium():
    def setup(self):
        desired_caps = {
          "platformName": "iOS",
          "platformVersion": "14.8",
          "deviceName": "iPhone12",
          "newCommandTimeout": "3600",
          "udid": "00008101-000255021E08001E",
          "bundleId": "com.facebook.WebDriverAgent.tendatest6.xctrunner",
          "webDriverAgentUrl": "http://localhost:8100",
          # "noReset": True,
          "usePrebuiltWDA": "true",
          # "useNewWDA": False,
          "useXctestrunFile": "false",
          "skipLogCapture": "true",
          # "wdaBaseUrl": "http://localhost",
          "automationName": "XCUITest"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def test_ios(self):
        print("666")