#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/5/18 17:40
# @Author:  haiyong
# @File:    test_tendawifi3.py
import cv2
import uiautomator2 as u2

class TestU2():
    def setup(self):
        self._device = '127.0.0.1:7555'
        self._appPackage = 'com.xueqiu.android'
        self._appActivity = '.common.MainActivity'

        self.d = u2.connect_usb(self._device)
        self.d.set_new_command_timeout(300)
        self.d.app_start(self._appPackage, self._appActivity)

    def teardown(self):
        # self.d.app_stop(self._appPackage)
        pass

    def test_uiautomator2(self):
        self.d(className="android.widget.TextView", text="行情").click()
        search_ele = self.d(resourceId="com.xueqiu.android:id/action_search").wait(timeout=3.0)
        assert search_ele == True
        self.d(resourceId="com.xueqiu.android:id/action_search").click()
        self.d(resourceId="com.xueqiu.android:id/search_input_text").set_text("招商银行")  # set the text


        self.d.xpath('//*[@text="03968"]').wait(3).click()
        wait_price = self.d(resourceId="com.xueqiu.android:id/current_price")[0].wait(timeout=3.0)
        if not wait_price:
            current_price = self.d(resourceId="com.xueqiu.android:id/current_price")[0].get_text()
            assert float(current_price) < 60
        else:
            assert False








