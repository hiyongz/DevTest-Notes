#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/5 16:36
# @Author:  haiyong
# @File:    test_register.py
from pageobject.page.main import Main
from pageobject.testcase.test_base import TestBase


class TestRegister(TestBase):
    # def setup(self):
    #     self.main = Main()

    def teardown_method(self):
        self.main._driver.quit()

    def test_register(self):
        assert self.main.goto_register().register()
    def test_login(self):
        assert self.main.goto_login().goto_register().register()
