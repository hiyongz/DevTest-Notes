#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/25 19:32
# @Author:  hiyongz
# @File:    test_parametrize3.py


import pytest
import yaml


class Test_Demo():
    @pytest.mark.parametrize(["a","b","result"],yaml.safe_load(open("./data3.yaml")))
    def test_case1(self, a, b, result):
        print("\n开始执行测试用例1")
        assert a + b == result


if __name__ == '__main__':
    pytest.main()