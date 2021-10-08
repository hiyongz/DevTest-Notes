#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/5/18 16:47
# @Author:  haiyong
# @File:    test_tendawifi.py
import time

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
            'automationName': 'Uiautomator2',
            'appPackage': 'com.tenda.router.app',
            'appActivity': '.activity.Anew.Splash.SplashActivity',
            'noReset':True,
            'newCommandTimeout': 3000,
            'unicodeKeyboard': True,
            'skipDeviceInitialization': True,
            'dontStopAppOnReset': True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass
        # self.driver.quit()

    def test_browser(self):
        sleep(5)
        start = time.time()
        self.driver.find_element_by_id("com.tenda.router.app:id/main_radio_btn_toolbox").click()
        search_locater = (By.ID,"com.tenda.router.app:id/id_item_router_action_logo")
        WebDriverWait(self.driver,30).until(expected_conditions.visibility_of_element_located(search_locater))
        end = time.time()
        print("总共用时{}秒".format((end - start)))

