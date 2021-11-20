#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/11/9 14:48
# @Author:  haiyong
# @File:    __init__.py.py

from .MyLibrary2 import MyLibrary
from .version import VERSION

_version_ = VERSION


class MyDynamicLibrary2(MyLibrary):
    """
    my test library
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'