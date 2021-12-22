#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/9/22 13:55
# @Author:  haiyong
# @File:    test_ios_airtest.py

__author__ = "DELL"

from airtest.core.api import *
from airtest.report.report import simple_report

# auto_setup(__file__, logdir=True, devices=["ios:///http://127.0.0.1:8100",])
auto_setup(__file__, logdir=True)
# connect_device("ios:///http://127.0.0.1:8100")
init_device(platform="IOS",uuid="http://localhost:8100/")
# init_device(platform="IOS",uuid="http+usbmux://00008101-000255021E08001E")
# script content
print("start...")

touch(Template(r"tpl1632398524727.png", record_pos=(-0.34, 0.236), resolution=(1125, 2436)))

# generate html report
simple_report(__file__)

keyevent("BACK")

stop_app()












