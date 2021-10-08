#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/10/25 16:15
# @Author:  hiyongz
# @File:    test_fixture_params.py

import pytest


@pytest.fixture(scope="module", params=[
    [1, 1, 2],
    [2, 8, 10],
    [99, 1, 100]
])
def data(request):
    yield request.param


class Test_Demo():
    def test_case1(self):
        print("\n开始执行测试用例1")
        assert 2 + 8 == 10

    def test_case2(self, data):
        print("\n开始执行测试用例2")
        assert data[0] + data[1] == data[2]

    def test_case3(self):
        print("\n开始执行测试用例3")
        assert 99 + 1 == 100


if __name__ == '__main__':
    pytest.main()
