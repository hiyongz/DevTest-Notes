#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/7/22 17:40
# @Author:  haiyong
# @File:    test_tendawifi2.py

import uiautomator2 as u2

class TestU2():
    def setup(self):
        self._device = 'SNHVB20C18002195'
        self._appPackage = 'com.tenda.router.app'
        self._appActivity = '.activity.Anew.Splash.SplashActivity'

        self.d = u2.connect_usb(self._device)
        self.d.set_new_command_timeout(300)
        self.d.app_start(self._appPackage, self._appActivity,wait=True, stop=True)

    def teardown(self):
        # self.d.app_stop(self._appPackage)
        pass

    def test_uiautomator2(self):
        self.d(resourceId="com.tenda.router.app:id/main_radio_btn_toolbox", text="工具箱").click()
        search_ele = self.d(resourceId="com.tenda.router.app:id/id_item_router_action_title", text="联网信息").wait(timeout=3.0)
        assert search_ele == True
        self.d(resourceId="com.tenda.router.app:id/id_item_router_action_title", text="联网信息").click()
        network_mode = self.d(resourceId="com.tenda.router.app:id/item_base_network_mode").get_text()  # get the text
        assert network_mode == "动态IP"










