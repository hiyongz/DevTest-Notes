#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/3/29 16:52
# @Author:  hiyongz
# @File:    conftest.py
import pprint
import pytest
# from _pytest.main import Session
# def pytest_collection_modifyitems(session:Session,config,items:list):
#     # 对测试用例进行排序
#     # 可以改变用例执行顺序
#     # items.reverse()
#     session.items = items
#
@pytest.fixture()
def login():
    print("登录")
    return 8