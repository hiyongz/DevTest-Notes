#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/11/11 19:23
# @Author:  haiyong
# @File:    MyKeywords.py

from robotlibcore import DynamicCore
from robotlibcore import keyword
from .keywords1 import Library1, Library2

class MyLibrary(DynamicCore):
    """General library documentation."""

    def __init__(self):
        libraries = [Library1(), Library2()]
        DynamicCore.__init__(self, libraries)

    @keyword
    def keyword_in_main(self, arg1, arg2='default'):
        pass
