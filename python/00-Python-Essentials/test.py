#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/6/6 17:14
# @Author:  hiyongz
# @File:    test.py


def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of


square = nth_power(2) # 平方
print(square(2)) # 2的平方
print(square.__closure__)
print(square.__closure__[0].cell_contents)

del nth_power
print(square(3)) # 3的平方