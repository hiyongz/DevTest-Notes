#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/17 21:25
# @Author:  haiyong
# @File:    test_toast.py
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestToast():
    # API Demos
    def setup(self):
        desired_caps = {
            'platformName': 'android',
            'platformVersion': '6.0.1',
            'deviceName': '127.0.0.1:7555',
            'appPackage': 'io.appium.android.apis',
            'appActivity': 'io.appium.android.apis.view.PopupMenu1',
            'automationName': 'Uiautomator2'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element_by_class_name("android.widget.Button").click()
        self.driver.find_element_by_xpath("//*[@text='Search']").click()
        # print(self.driver.page_source)
        # print(self.driver.find_element(MobileBy.XPATH, "//*[@class ='android.widget.Toast']").text)
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'Clicked popup')]").text)

    def test_toast2(self):
        toast_text = "test"
        timeout = 5
        expe = 'pass'
        try:
            message = """.//*[@text="%s"]""" % toast_text
            element2 = WebDriverWait(self.driver, timeout, 0.1).until(EC.presence_of_element_located((MobileBy.XPATH, message)))
            print(element2.text)
            if element2.text == toast_text:
                if expe == 'pass':
                    return True
                else:
                    return False
        except:
            print
            "can't find the toast!"
