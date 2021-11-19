#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/11/9 14:48
# @Author:  haiyong
# @File:    __init__.py.py

from .MyKeywords import MyKeywords
from .version import VERSION

_version_ = VERSION


class MyLibrary(MyKeywords):
    """
    my test library
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'