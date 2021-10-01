#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/6/6 16:32
# @Author:  hiyongz
# @File:    python_closures.py

# Python 闭包

def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of

square = nth_power(2) # 平方
cube = nth_power(3) # 立方
print(square)
print(cube)
print(square.__closure__)
print(square.__closure__[0].cell_contents)
print(cube.__closure__[0].cell_contents)

print(square(2))  # 2的平方
print(cube(2)) # 2的立方
del nth_power
print(square(3)) # 3的平方
