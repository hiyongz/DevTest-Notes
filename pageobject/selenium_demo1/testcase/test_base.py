#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/9/5 15:02
# @Author:  hiyongz
# @File:    test_base.py
from page.main import Main


class TestBase:
    app = None
    def setup(self):
        self.main = Main()