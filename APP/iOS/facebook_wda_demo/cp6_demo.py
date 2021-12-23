#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/12/9 15:36
# @Author:  haiyong
# @File:    cp6_demo.py


import wda
import time
wda.DEBUG = False # default False
wda.HTTP_TIMEOUT = 180.0 # default 180 seconds
wda.DEVICE_WAIT_TIMEOUT = 180.0

class TestDemo():
    def setup(self):
        # self.c = wda.USBClient("00008101-000255021E08001E", port=8100)
        self.c = wda.Client('http://localhost:8100')
        self.c.wait_ready(timeout=300)
        self.c.implicitly_wait(5.0)

    def teardown(self):
        self.c.session().app_terminate("com.tenda.security")

    def test_NFC(self):
        self.c.session('com.tenda.security')
        # time.sleep(10)
        self.c(name="首页").click()
        self.c(name="消息").click()
        self.c(name="我的").click()
        # self.c(name="首页").click()
        self.c(name='icn home add').click()
        time.sleep(5)
        # self.c(name='打开手电筒').click(3)
        self.c(name="打开手电筒").tap()
        time.sleep(10)
        self.c(name='打开手电筒').click(3)

    def test_my(self):
        self.c.session('com.tenda.security')
        # time.sleep(10)
        self.c(name="首页").click()
        self.c(name="消息").click()
        self.c(name="我的").click()
        # self.c(name="首页").click()
        self.c(name='关于我们').click()
        # time.sleep(5)
        # self.c(name='打开手电筒').click(3)
        self.c(name="官网").tap()
        time.sleep(10)
        self.c(name='打开手电筒').click(3)