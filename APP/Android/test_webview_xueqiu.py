#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/20 21:52
# @Author:  haiyong
# @File:    test_webview_xueqiu.py
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebview():
    # API Demos
    def setup(self):
        desired_caps = {
            'platformName': 'android',
            'platformVersion': '5.1.1',
            'deviceName': '127.0.0.1:62001',
            # 'deviceName': '192.168.249.101:5555',
            'appPackage': 'com.xueqiu.android',
            'appActivity': 'com.xueqiu.android.common.MainActivity',
            'automationName': 'Uiautomator2',
            'noReset': 'true',
            # 'chromedriverExecutable': 'D:/testing_tools/chromedriver80/chromedriver.exe',
            'chromedriverExecutableDir': 'D:/testing_tools',
            'chromedriverChromeMappingFile': 'D:/ProgramWorkspace/TestingDemo/test_appium_webview/mapping.json'

        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_webview(self):
        # 点击交易
        self.driver.find_element(MobileBy.XPATH,"//*[@text='交易']").click()
        sleep(5)
        A_locator = (MobileBy.XPATH, '//[*@id="Layout_app_3V4"]/div/div/ul/li[1]/div[2]/h1')
        print(self.driver.contexts)
        # 切换上下文
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 点击A股开户
        print(self.driver.window_handles)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(A_locator))
        self.driver.find_element(*A_locator).click()
        kaihu_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(kaihu_window)
        # 显式等待
        phonenumber_locator = (MobileBy.ID, 'phone-number')
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(phonenumber_locator))
        # 输入用户名和验证码,点击立即开户
        self.driver.find_element(*phonenumber_locator).send_keys("12345678901")
        self.driver.find_element(MobileBy.ID, 'code').send_keys("1234")
        self.driver.find_element(MobileBy.XPATH, '/html/body/div/div/div[2]/div/div[2]/h1').click()