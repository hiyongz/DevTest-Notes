#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/5/18 17:40
# @Author:  haiyong
# @File:    test_tendawifi2.py
import cv2
import uiautomator2 as u2

class TestU2():
    def setup(self):
        self._device = '127.0.0.1:7555'
        self._appPackage = 'com.xueqiu.android'
        self._appActivity = '.common.MainActivity'

        self.d = u2.connect_usb(self._device)
        self.d.set_new_command_timeout(300) # accessibility服务的最大空闲时间，超时将自动释放
        # self.d.app_install('http://some-domain.com/some.apk')
        self.d.app_start(self._appPackage, self._appActivity)

    def teardown(self):
        # self.d.app_stop(self._appPackage)
        pass

    def test_uiautomator2(self):
        print("66666")
        self.d.app_current()
        # self.d(className="android.widget.TextView", text="行情").click()
        # self.d(className="android.widget.TextView", textMatches="^行.*").click()
        # self.d(resourceId="android:id/tabs").child(text="行情").click()
        # self.d(className="android.widget.ImageView").sibling(text="行情").click()
        # self.d(resourceId="android:id/tabs").child_by_text("行情").click()
        # self.d(text="雪球").right(text="行情").click()
        # self.d(resourceId="com.xueqiu.android:id/tab_name", instance=1).click()

        # print(self.d(resourceId="com.xueqiu.android:id/tab_name").count)
        # # same as count property
        # print(len(self.d(resourceId="com.xueqiu.android:id/tab_name")))
        # # get the instance via index
        # self.d(resourceId="com.xueqiu.android:id/tab_name")[1].click()
        # self.d(resourceId="com.xueqiu.android:id/tab_name")[1].click_exists(timeout=10.0)

        self.d(resourceId="cloud_account_login_et_password").get_text()
        self.d.xpath('//*[@text="行情"]').wait(10.0).click()
        self.d.xpath('//*[@text="行情"]').parent()
        self.d(resourceId="com.xueqiu.android:id/tab_name").parent()

        print(self.d(text="行情").exists)
        print(self.d.exists(text="行情"))
        self.d(text="行情").exists(timeout=3)  # wait Settings appear in 3s, same as .wait(3)

        print(self.d(text="行情").info)

        x, y = self.d(text="行情").center()
        print("666666:",x,y)
        x, y = self.d(text="行情").center(offset=(0, 0)) # left-top x, y
        print("888888:", x, y)
        self.d.toast.show("Hello world")
        self.d.toast.show("Hello world", 1.0)  # show for 1.0s, default 1.0s
        self.d.toast.get_message(5.0, 10.0, "default message")
        # im = self.d(text="行情").screenshot()
        # im.save("行情.jpg")
        # self.d.screenshot(filename="screenshot.png")
        # self.d.screenshot("saved.jpg")
        # self.d.screenshot().save("saved.png")
        # cv2.imwrite('saved.jpg', self.d.screenshot(format='opencv'))

        print(self.d(text="行情").get_text())

        self.d(resourceId="com.xueqiu.android:id/action_search").click()
        self.d(resourceId="com.xueqiu.android:id/search_input_text").wait(timeout=3.0)  # 等待元素出现
        self.d(resourceId="com.xueqiu.android:id/search_input_text").set_text("招商银行")  # set the text
        self.d(resourceId="com.xueqiu.android:id/search_input_text").clear_text()  # clear the text

        # self.d.service("uiautomator").stop()
        #
        # self.d.app_list_running()
        #
        # self.d.click()
        # self.d.long_click()
        self.d.app_current()
        self.d.swipe()
        self.d.pinch_in()
        # self.d.swipe_ext("right")
        #
        ele = self.d(text="微信")
        # ele.click()
        # ele.long_click()
        # ele.double_click()
        ele.swipe()
        ele.clear_text()

        x, y = self.d(text="工具箱").center(offset=(0, 0))

        self.d(text="Settings").wait_gone(timeout=1.0)

