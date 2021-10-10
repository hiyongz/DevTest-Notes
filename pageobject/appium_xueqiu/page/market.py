#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/19 8:50
# @Author:  haiyong
# @File:    market.py
from page.base_page import BasePage
from page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)
