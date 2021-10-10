#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/19 1:02
# @Author:  haiyong
# @File:    app.py
from appium import webdriver
from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    def start(self):
        _package = 'com.xueqiu.android'
        _activity = 'com.xueqiu.android.common.MainActivity'
        if self._driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1.1'
            desired_caps['deviceName'] = '127.0.0.1:62001'
            desired_caps['appPackage'] = _package
            desired_caps['automationName'] = 'Uiautomator2'
            desired_caps['appActivity'] = _activity
            desired_caps['newCommandTimeout'] = 3000
            desired_caps['noReset'] = True
            # desired_caps['dontStopAppOnReset'] = True
            desired_caps['skipDeviceInitialization'] = True
            desired_caps['autoGrantPermissions'] = True
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeybBoard'] = True
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(_package)
        return self
    def main(self):
        return Main(self._driver)