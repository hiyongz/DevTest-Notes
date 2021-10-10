#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/25 15:16
# @Author:  haiyong
# @File:    app.py
import yaml

from test_appium_wechatwork.page.base_page import BasePage
from test_appium_wechatwork.page.main import Main
from appium import webdriver


class App(BasePage):
    def start(self):
        # 启动 app
        desired_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'deviceName': yaml.safe_load(open("../page/configuration.yaml"))["caps"]["deviceName"],
            'appPackage': 'com.tencent.wework',
            'appActivity': 'com.tencent.wework.launch.WwMainActivity',
            'automationName': 'Uiautomator2',
            'noReset': True,
            'unicodeKeyboard': True,
            'resetKeybBoard': True,
        }
        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self._driver.implicitly_wait(5)
        return self

    def stop(self):
        pass

    def restart(self):
        pass

    def main(self):
        return Main(self._driver)
