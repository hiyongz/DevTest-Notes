#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/11/11 19:23
# @Author:  haiyong
# @File:    MyKeywords.py

from robot.api.deco import keyword
from robot.api import logger

class MyKeywords(object):
    def __init__(self):
        self._cal = Calculate()

    def get_keyword_names(self):
        # 获取当前测试类的所有属性
        attributes = [(name, getattr(self._cal, name)) for name in dir(self._cal)]
        # 过滤没有设置robot_name的属性
        keywords = [(name, value) for name, value in attributes
                    if hasattr(value, 'robot_name')]
        # 返回关键字名称
        return [value.robot_name or name for name, value in keywords]

    def run_keyword(self, name, args, kwargs):
        print("Running keyword '%s' with positional arguments %s and named arguments %s."
              % (name, args, kwargs))
        func = getattr(self._cal, name)
        return func(*args,**kwargs)

    def get_keyword_documentation(self, name):
        func = getattr(self._cal, name)
        return func.__doc__

    def get_keyword_arguments(self, name):
        func = getattr(self._cal, name)
        func_args = func.__code__.co_varnames
        if func_args[0] == "self":
            func_args = func_args[1:]
        return func_args


class Calculate(object):

    def not_keyword(self):
        pass

    @keyword
    def test_sub(self, a, b, results=None):
        """两数相减
        """
        if float(a) - float(b) == float(results):
            return True
        else:
            raise RuntimeError("%s - %s != %s"%(a,b,results))

    @keyword
    def test_add(self, a, b, c):
        """两数相加

        :a: value1

        :b: value2

        :c: 预期结果

        Example:
        | Test Add | 2 | 3 | 5 |

        """
        if float(a) + float(b) == float(c):
            return True
        else:
            raise RuntimeError("%s + %s != %s"%(a,b,c))