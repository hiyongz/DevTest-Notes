#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/25 18:20
# @Author:  haiyong
# @File:    test_deletecontact.py
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDelete():
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
        #teardown方法
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gpp").click()
        pass

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("username",[
        ("test1"),
        ("test2")
    ])
    def test_delete_contact(self,add_fixture,username):
        print(username)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, f"//*[contains(@text, '{username}')]").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/gq0").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/axr").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/drk").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/b89").click()
        sleep(3)
        assert username not in self.driver.page_source
