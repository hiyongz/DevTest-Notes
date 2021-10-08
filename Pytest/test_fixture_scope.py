#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/25 11:00
# @Author:  hiyongz
# @File:    test_fixture_scope.py


import pytest

@pytest.fixture(scope="class")
def login():
    print("登录...")

class Test_Demo():
    def test_case1(self, login):
        print("\n开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self, login):
        print("\n开始执行测试用例2")
        assert 2 + 8 == 10

    def test_case3(self, login):
        print("\n开始执行测试用例3")
        assert 99 + 1 == 100


if __name__ == '__main__':
    pytest.main()