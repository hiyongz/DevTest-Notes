#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/3/29 10:39
# @Author:  hiyongz
# @File:    test_calc2.py
'''
pytest
'''
import pytest
from test_pytest.calc import Calc
import yaml

# data1 = [(1, 2, 3),
#          (-1, -2, -3),
#          (0, 1, 1),
#          (0, -1, -1),
#          (0.1, 0.2, 0.3),
#          (999999, 1000000, 1999999)]
# data1 = yaml.load(open("test_pytest_data.yaml"))
data2 = [(1, 2, 0.5),
         (-1, -2, 0.5),
         (0, 1, 0),
         (1, 0, 0),
         (0.1, 0.2, 0.5)]


def setup_module():
    # 整个文件只执行一次
    print("setup_module")
# @pytest.fixture(scope="module")
def data():
    with open("test_pytest_data.yaml") as f:
        return yaml.load(f)
def steps():
    with open("test_pytest_steps.yaml") as f:
        return yaml.load(f)

class TestCalc():
    @classmethod
    def setup_class(cls):
        # 类执行之前的初始化操作
        print("setup_class")

    def setup(self):
        self.calc = Calc()

    # def setup_method(self):
    #     self.calc = Calc()
    def teardown(self):
        print("teardown")

    # def teardown_method(self):
    #     print("teardown_method")
    @pytest.mark.demo1
    @pytest.mark.parametrize("a, b, result", data())
    def test_add(self, a, b, result):
        data = (a,b)
        # assert self.calc.add(a, b) == result
        self.steps(data,pytest.approx(result))


    @pytest.mark.demo2  # 添加标签
    @pytest.mark.parametrize("a, b, result", data2)
    def test_div(self, a, b, result):
        assert self.calc.div(a, b) == result

    def steps(self,data,r):
        test_steps = steps()
        for step in test_steps:
            if step == "add":
                assert self.calc.add(*data) == r
            elif step == "add_1":
                assert self.calc.add_1(data) == r


    # def test_add_1(self):
    #     data = (1, 2)
    #     assert self.calc.add_1(data) == 3
    #     assert self.calc.add(*data) == 3
