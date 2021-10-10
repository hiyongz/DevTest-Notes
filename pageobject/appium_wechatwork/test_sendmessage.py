#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/25 17:08
# @Author:  haiyong
# @File:    test_sendmessage.py
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestSendMessage():
    def setup_class(self):
        desired_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'deviceName': '127.0.0.1:7555',
            'appPackage': 'com.tencent.wework',
            'appActivity': 'com.tencent.wework.launch.WwMainActivity',
            'automationName': 'Uiautomator2',
            'noReset': True,
            'unicodeKeyboard': True,
            'resetKeybBoard': True,
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    @pytest.fixture()
    def add_fixture(self):
        # setup方法
        yield
        # teardown方法
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gpp").click()
        sleep(2)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gpp").click()

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("username,message", [
        ("test1", "Hello!"),
        ("test2", "Hi")
    ])
    def test_send_message(self, add_fixture, username, message):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq_").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ffq").send_keys(username)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/dnb").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/dtv").send_keys(message)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/dtr").click()
        elements = self.driver.find_elements(MobileBy.ID, "com.tencent.wework:id/dtg")
        print(elements)
        assert message == elements[-1].text
