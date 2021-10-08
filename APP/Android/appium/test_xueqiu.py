#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/13 21:31
# @Author:  haiyong
# @File:    test_xueqiu.py
import time

import pytest

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestXueqiu:
    def setup(self):
        # Returns abs path relative to this file and not cwd
        # PATH = lambda p: os.path.abspath(
        #     os.path.join(os.path.dirname(__file__), p)
        # )
        # print(PATH)
        desired_caps = {}
        # desired_caps['recreateChromeDriverSessions'] = True
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        # desired_caps['platformVersion'] = '8.0'
        # desired_caps['deviceName'] = 'WTKDU16813012502'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['automationName'] = 'Uiautomator2'
        # desired_caps['app'] = PATH('D:/testing_tools/tendawifi.apk')
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['newCommandTimeout'] = 3000
        # desired_caps['unicodeKeyboard'] = True
        desired_caps['noReset'] = True
        # desired_caps['dontStopAppOnReset'] = True
        desired_caps['skipDeviceInitialization'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeybBoard'] = True

        # #"adb kill-server",
        # cmdlst = ["taskkill /f /im node.exe","taskkill /f /im adb.exe","""start /b node "C:\\Program Files\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js" --address 127.0.0.1 --port 4723 --session-override --no-reset""","adb shell am force-stop "+desired_caps['appPackage']]
        # # cmdlst = ["taskkill /f /im node.exe","adb shell am force-stop "+desired_caps['appPackage']]
        # #每次运行前先判断屏幕是否点亮,然后再进行操作
        # os.system("adb shell input keyevent 26")
        # os.system("adb shell input swipe 550 1200 550 375")
        # for cmd in cmdlst:
        #     os.system(cmd)
        # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)

    def teardown_method(self):
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    def test_search(self):
        """
        1. 打开雪球app
        2. 点击搜索框
        3. 输入"招商银行"
        4.选择
        5. 获取股价，并判断
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(u"招商银行")
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.xueqiu.android:id/stockCode' and @text='SH600036']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/stock_current_price").text)
        print(current_price)
        assert current_price > 30

    def test_attr(self):
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enabled = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enabled == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(u"招商银行")
            zhaoshan_ele = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/code' and @text='SH600036']")
            # zhaoshan_ele.is_displayed()
            element_display = zhaoshan_ele.get_attribute("displayed")
            print(element_display)
            if element_display == "true":
                print("success")
            else:
                print("fail!!!")

    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        # action.press(x=523,y=1035).move_to(x=523,y=334).release().perform()
        action.press(x=x1, y=y_start).move_to(x=x1, y=y_end).release().perform()
        time.sleep(5)

    def test_get_current(self):
        #
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(u"招商银行")
        current_price = self.driver.find_element_by_xpath(
            "//*[@text='SH600036']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        # 显示等待
        # locator = (MobileBy.XPATH,"//*[@text='SH600036']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        # # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # ele = self.driver.find_element(*locator)
        # print(ele.text)
        # current_price = ele.text
        assert float(current_price) > 30

    def test_myinfo(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        # self.driver.find_element_by_android_uiautomator(
        #     'new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("test")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("test")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        time.sleep(5)

    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("博时基金").instance(0));').click()
        time.sleep(5)


if __name__ == '__main__':
    pytest.main()
