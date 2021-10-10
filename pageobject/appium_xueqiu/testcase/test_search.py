#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/19 9:03
# @Author:  haiyong
# @File:    test_search.py
from test_appium2.page.app import App


class TestSearch:
    def test_search(self):
        App().start().main().goto_market().goto_search().search("jd")
