#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/11/11 19:23
# @Author:  haiyong
# @File:    MyKeywords.py

from robotlibcore import keyword

class Library1(object):

    @keyword
    def example(self):
        """Keyword documentation."""
        pass

    @keyword
    def example_test2(self, arg1, arg2='default'):
        """Keyword documentation."""
        pass

    @keyword
    def another_example(self, arg1, arg2='default'):
        """Keyword documentation."""
        pass

    def not_keyword(self):
        pass


class Library2(object):

    @keyword('Custom name')
    def this_name_is_not_used(self):
        pass

    @keyword(tags=['tag', 'another'])
    def tags(self):
        pass
