#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/10/25 17:28
# @Author:  hiyongz
# @File:    test_parametrize.py

import pytest


class Test_Demo():
    @pytest.mark.parametrize("a, b, result", [(1, 1, 2), (2, 8, 10)])
    def test_case1(self, a, b, result):
        print("\n开始执行测试用例1")
        assert a + b == result


if __name__ == '__main__':
    pytest.main()
