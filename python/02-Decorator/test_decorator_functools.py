#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/3/11 7:20
# @Author:  haiyong
# @File:    test_decorator_functools.py
import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('this is wrapper')
        func(*args, **kwargs)
    return wrapper

@my_decorator
def test_decorator(message):
    print(message)

test_decorator('hello world')
print(test_decorator.__name__)
print("######")
help(test_decorator)
