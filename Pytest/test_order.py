#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/7/20 20:54
# @Author:  haiyong
# @File:    test_order.py
import sys

import pytest

from test_pytest.calc import Calc


def setup_module():
    print("setup_module")


class TestOrder:

    @classmethod
    def setup_class(cls):
        print("setup_class")

    def setup_method(self):
        print("setup_method")

    def setup(self):
        print("setup")
        self.calc = Calc()

    def teardown(self):
        print("teardown")

    def teardown_method(self):
        print("teardown_method")

    @pytest.mark.run(order=-1)
    def test_zadd(self):
        print("add")
        assert self.calc.add(1, 2) == 3

    @pytest.mark.run(order=1)
    def test_div(self):
        print("div")
        assert self.calc.div(1, 2) == 0.5

    @pytest.mark.parametrize("a, b", [
        (1, 2), (2, 3), (3, 4)
    ])
    def test_params(self, a, b):
        print("params")
        data = (a, b)
        self.calc.add2(data)
        self.calc.add(*data)