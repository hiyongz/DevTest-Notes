#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/14 22:21
# @Author:  haiyong
# @File:    test_touchaction.py
import time

import pytest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestXueqiu:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['automationName'] = 'Uiautomator1'
        desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
        desired_caps['newCommandTimeout'] = 3000
        desired_caps['noReset'] = True
        desired_caps['dontStopAppOnReset'] = True
        desired_caps['skipDeviceInitialization'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeybBoard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)

    def teardown_method(self):
        self.driver.quit()

    def test_touchaction_unlock(self):
        # 手势操作
        action = TouchAction(self.driver)
        action.press(x=175, y=250).wait(200).move_to(x=537, y=250).wait(200).move_to(x=900, y=250).wait(200).move_to(
            x=896, y=608).wait(200).move_to(x=898,y=973).wait(200).release().perform()
