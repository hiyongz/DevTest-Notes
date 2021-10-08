#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/25 11:27
# @Author:  hiyongz
# @File:    test_fixture_autouse.py

import pytest

@pytest.fixture(scope='class', autouse=True)
def login():
    print("登录...")

class Test_Demo():
    def test_case1(self):
        print("\n开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self):
        print("\n开始执行测试用例2")
        assert 2 + 8 == 10

    def test_case3(self):
        print("\n开始执行测试用例3")
        assert 99 + 1 == 100


if __name__ == '__main__':
    pytest.main()