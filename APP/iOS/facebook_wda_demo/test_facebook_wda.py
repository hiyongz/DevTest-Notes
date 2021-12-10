#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/7/20 8:47
# @Author:  haiyong
# @File:    test_facebook_wda.py

# facebook-wda 示例代码

# 启动WDA
# tidevice -u 00008101-000255021E08001E wdaproxy -B com.facebook.WebDriverAgent.tendatest.xctrunner --port 8100

# tidevice launch com.apple.Preferences

import wda

wda.DEBUG = True # default False
wda.HTTP_TIMEOUT = 180.0 # default 180 seconds
wda.DEVICE_WAIT_TIMEOUT = 180.0

class TestFacebookWDA():
    def setup(self):
        self.c = wda.Client('http://localhost:8100')  # 8100为启动WDA设置的端口号
        # self.c = wda.USBClient()  # 仅连接一个设备可以不传参数
        self.c = wda.USBClient("00008101-000255021E08001E", port=8100)  # 指定设备 udid 和WDA 端口号
        # self.c = wda.Client("http+usbmux://{udid}:8100".format(udid="00008101-000255021E08001E"))
        # self.c = wda.USBClient("00008101-000255021E08001E", port=8100,
        #                   wda_bundle_id="com.facebook.WebDriverAgent.test2.xctrunner")  # 1.2.0 引入 wda_bundle_id 参数
        # self.c.app_current()  # 显示当前应用信息
        self.c.wait_ready(timeout=300)
        self.c.healthcheck()
        self.c.session().app_activate("com.apple.Preferences")  # 打开设置
        self.c.session('com.apple.Preferences')
        self.c.session('com.tenda.TendaRouter', alert_action='accept')
        # c.session().app_terminate("com.apple.Preferences") # 退出设置
        self.c.implicitly_wait(30.0)

    def teardown(self):
        # self.d.app_stop(self._appPackage)
        pass

    def test_wda(self):
        self.c(name="搜索").set_text("NFC")  # 搜索 NFC
        self.c(name="NFC").click()  # 点击NFC
        self.c.status()
        # self.c(xpath='//Switch').exists  # 判断NFC开关是否存在
        # self.c(xpath='//Switch').get().value  # 获取NFC开关状态
        s = self.c.session('com.apple.Preferences')
        # s(className='XCUIElementTypeTable').child(name='通知').exists
        s(predicate='name MATCHES "^屏幕.*"').click()
        s(classChain='**/XCUIElementTypeWindow[`name MATCHES "^屏幕.*"`]').click()
        self.c.swipe(0.5, 0.5, 0.5, 1.0)
        self.c.swipe_right()
        ele = s(classChain='**/XCUIElementTypeWindow[`name MATCHES "^屏幕.*"`]')
        print(ele.bounds)
        self.c.alert.accept()
        s(text='Dashboard').child(className='Cell')
        s(name="屏幕使用时间").swipe("up")





























