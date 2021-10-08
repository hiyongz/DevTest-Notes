#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/20 20:48
# @Author:  haiyong
# @File:    test_webview_apidemo.py
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestBrowser():
    def setup(self):
        desired_caps = {
        'platformName': 'android',
        # 'platformVersion': '5.1.1',
        'platformVersion': '10',
        'appPackage': 'io.appium.android.apis',
        'appActivity': 'io.appium.android.apis.ApiDemos',
        # 'browserName': 'Chrome',
        # 'deviceName': '127.0.0.1:62001',
        'deviceName': 'CUYDU19626004019',
        'noReset': 'true',
        'chromedriverExecutable': 'D:/testing_tools/chromedriver85/chromedriver.exe'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        pass
        # self.driver.quit()
    def test_webview(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        webview ="WebView"
        print(self.driver.contexts)
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{webview}")'
                                                        '.instance(0));').click()

        #self.driver.findelement(MobileBy.ACCESSIBILITY_ID,'i has no focus').send_keys("this is test string")
        #self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'i am a link').click()
        #print(self.driver.page_source)
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[1])
        print(self.driver.current_context)
        print(self.driver.page_source)

        self.driver.find_element(MobileBy.ID, 'i_am_a_textbox').send_keys("this is test string use chrome inspect")
        self.driver.find_element(MobileBy.ID, 'i am a link').click()
        print(self.driver.page_source)