#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/23 7:09
# @Author:  hiyongz
# @File:    test_setup_teardown2.py

import pytest

def setup_function():
    print("初始化。。。")

def teardown_function():
    print("清理。。。")

def test_case1():
    print("开始执行测试用例1")
    assert 1 + 1 == 2

def test_case2():
    print("开始执行测试用例2")
    assert 2 + 8 == 10

def test_case3():
    print("开始执行测试用例3")
    assert 99 + 1 == 100