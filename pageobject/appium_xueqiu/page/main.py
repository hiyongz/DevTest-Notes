#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/19 8:27
# @Author:  haiyong
# @File:    main.py
from page.base_page import BasePage
from page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")
        return  Market(self._driver)