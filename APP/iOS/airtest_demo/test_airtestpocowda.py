# !/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/12/10 16:25
# @Author:  haiyong
# @File:    test_airtest_poco_wda.py

"""
airtest、poco、facebook-wda混合使用
"""

from airtest.core.api import *
from .start_wda import StartWDA
import wda
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.drivers.ios import iosPoco


class TestFacebookWDA():
    def setup(self):
        self.udid = "00008101-000255021E08001E"
        self.wda_bundle_id = "com.facebook.WebDriverAgentRunner.test2.xctrunner"
        self.port = 8100  # 8100为启动WDA设置的端口号
        self.app_name = "com.apple.Preferences"

        # 启动WDA
        self.wda = StartWDA()
        self.wda.stop_wda(self.port)
        self.wda.start_wda(self.udid, self.wda_bundle_id, self.port)

        # airtest初始化连接设备
        init_device(platform="IOS", uuid=f"http://localhost:{self.port}/")
        # poco初始化
        self.poco = iosPoco()
        # facebook-wda连接设备
        self.c = wda.Client(f'http://localhost:{self.port}')

        self.c.session().app_activate(self.app_name)  # 打开设置
        # start_app("com.apple.Preferences")
        self.c.implicitly_wait(3.0)

    def teardown(self):
        self.c.session().app_terminate(self.app_name)  # 退出设置

    def init_devices(self, platform="Android", addr="http://localhost:8100/", uuid=None, wdaId=None, port="8100",
                     stop_wda=True):
        """ 初始化手机
        :platform: Android, IOS or Windows
        :addr: 连接iOS WDA的地址
        :uuid: serialno for Android, handle for Windows, uuid for iOS
        :wdaId: WDA应用的 bundle id
        :port: 侦听的WDA端口号，默认8100
        :stop_wda: 启动WDA前是否杀掉WDA进程，默认会杀掉。建议先杀掉WDA后再启动，如果存在相关进程，可能导致初始化不成功。
        """
        try:
            if platform == "Android":
                init_device(platform="Android", uuid=uuid)
            elif platform.lower() == "ios":
                if stop_wda == True:
                    self.wda.stop_wda(port)
                if self.wda.start_wda(uuid, wdaId, port):
                    init_device(platform, addr)
        except Exception as e:
            raise RuntimeError(e)

    def poco_init_devices(self, platform="Android"):
        """功能描述： 初始化手机
        """
        try:
            if platform.lower() == "android":
                self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
            elif platform.lower() == "ios":
                self.poco = iosPoco()

            print("Poco初始手机成功")
        except Exception as e:
            log_data = 'Poco初始化手机失败'
            print(log_data)
            raise RuntimeError(e)

    def test_demo(self):
        self.c.swipe_up()
        time.sleep(1)
        self.c(name="通用").click()
        time.sleep(1)
        self.poco("关于本机").click()
        assert self.poco('软件版本').attr('value') == "14.8"

        ele = self.c(name="型号名称", className="XCUIElementTypeCell").wait(timeout=3.0)
        assert ele.value == "iPhone 12 mini"
