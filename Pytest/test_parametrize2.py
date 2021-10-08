#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/25 18:15
# @Author:  hiyongz
# @File:    test_parametrize2.py

import pytest
data = [(1, 1, 2),
         (2, 8, 10),
         (99, 1, 100)
         ]

class Test_Demo():
    def setup_method(self):
        print("初始化。。。")

    def teardown_method(self):
        print("清理。。。")

    @pytest.mark.parametrize("a, b, result", data)
    def test_case1(self, a, b, result):
        print("\n开始执行测试用例1")
        assert a + b == result


if __name__ == '__main__':
    pytest.main()
