#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/3/11 7:19
# @Author:  haiyong
# @File:    test_decorator_repeat.py

def repeat(count):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(count):
                print(f'counter: {i}')
            func(*args, **kwargs)
        return wrapper
    return my_decorator


@repeat(4)
def test_decorator(message):
    print(message)

test_decorator('hello world')