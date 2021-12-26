#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/12/26 10:43
# @Author:  hiyongz
# @File:    test_app_current.py

import uiautomator2 as u2

class TestAppCurrent():
    def setup(self):
        self._device = 'CUYDU19626004019'
        self.d = u2.connect_usb(self._device)

    def teardown(self):
        # self.d.app_stop(self._appPackage)
        pass

    def test_app_current(self):
        self.d.app_current()
        print("66666")
