#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/4/3 19:07
# @Author:  haiyong
# @File:    test_encode.py.py

import pytest

@pytest.mark.parametrize("name",["张三","李四"])
def test_name(name):
    print(name)