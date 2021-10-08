#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/9/24 16:56
# @Author:  haiyong
# @File:    test_ios_poco.py

from airtest.core.api import *
from airtest.report.report import simple_report
from poco.drivers.ios import iosPoco

# 连接设备、初始化日志路径
auto_setup(__file__, logdir=True)
init_device(platform="IOS",uuid="http://localhost:8100/")
# init_device(platform="IOS",uuid="http+usbmux://00008101-000255021E08001E")
# 打开【设置】
start_app("com.apple.Preferences")

# 初始化ios poco
poco = iosPoco()

# 点击
poco("通用").click()
poco("关于本机").click()
# 断言
assert poco('软件版本').attr('value') == "14.8"

# generate html report
simple_report(__file__)