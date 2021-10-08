#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/11/8 1:13
# @Author:  haiyong
# @File:    test_uiautomator.py

import pytest
from appium import webdriver


class TestWebDriverWait:
    def setup(self):
        desired_caps = {}
        # desired_caps['recreateChromeDriverSessions'] = True
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        # desired_caps['deviceName'] = 'WTKDU16813012502'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['automationName'] = 'Uiautomator2'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
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

    @pytest.mark.parametrize('searchkey,type,price', [
        ('招商银行', 'SH600036', 30)
    ])
    def test_search(self, searchkey, type, price):
        """
         1. 打开雪球app
         2. 点击搜索框
         3. 输入"招商银行"
         4. 选择
         5. 获取股价，并判断
        """

        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/tv_search")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/search_input_text")').send_keys(searchkey)
        self.driver.find_element_by_android_uiautomator(f'new UiSelector().text("{type}")').click()
        self.driver.find_element_by_android_uiautomator(f'new UiSelector().text("{type}")').click()
        current_price = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/stock_current_price")').text

        print(current_price)
        assert float(current_price) > 40
