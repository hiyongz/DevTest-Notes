#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/19 8:55
# @Author:  haiyong
# @File:    search.py
from page.base_page import BasePage


class Search(BasePage):
    def search(self,value):
        self._params["value"] = value
        self.steps("../page/search.yaml")