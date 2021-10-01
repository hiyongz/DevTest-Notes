#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/3/10 21:30
# @Author:  haiyong
# @File:    test_decorator.py

# python装饰器实例

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('this is wrapper')
        func(*args, **kwargs)
        print('bye')
    return wrapper

@my_decorator
def test_decorator(message):
    print(message)

test_decorator('hello world')




