#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/10/22 21:58
# @Author:  hiyongz
# @File:    test_setup_teardown.py

import pytest


def setup_module():
    print("初始化。。。")


def teardown_module():
    print("清理。。。")

class Test_Demo():
    def test_case1(self):
        print("开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self):
        print("开始执行测试用例2")
        assert 2 + 8 == 10

    def test_case3(self):
        print("开始执行测试用例3")
        assert 99 + 1 == 100


if __name__ == '__main__':
    pytest.main()
