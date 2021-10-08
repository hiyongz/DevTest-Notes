#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/10/23 7:16
# @Author:  hiyongz
# @File:    test_setup_teardown3.py

class Test_Demo():
    # def setup_class(self):
    #     print("初始化。。。")
    #
    # def teardown_class(self):
    #     print("清理。。。")
    def setup_method(self):
        print("初始化。。。")

    def teardown_method(self):
        print("清理。。。")
    def test_case1(self):
        print("开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self):
        print("开始执行测试用例2")
        assert 2 + 8 == 10

    def test_case3(self):
        print("开始执行测试用例3")
        assert 99 + 1 == 100
