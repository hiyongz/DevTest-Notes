#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/5/27 21:36
# @Author:  hiyongz
# @File:    python_memory_management.py

# 列表
# import copy
#
# l1 = [1, 2, 3]
# print(id(l1))  # 返回对象的内存地址
#
# l2 = l1
# print(id(l2))
#
# l1.append(4)
# print(id(l1))
#
# print(l1)
# print(l2)
# print(l1 is l2)
#
# l3 = [4, 5, 6]
# print(id(l3))
#
# # 变量赋值
# a = 1
# print(id(a))
# b = a
# print(id(b))
# a = a + 1
# print(id(a))
# c = 1
# print(id(c))
#
# # == vs is
# a = 1
# b = a
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)
#
# if a is None:
#     print("a is None")
# if a is not None:
#     print("a is not None")
#
# ## Python浅拷贝和深度拷贝
#
# # 不可变数据类型浅拷贝
# a = 1
# b = copy.copy(a)
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)
#
# t1 = (1, 2, 3)
# t2 = tuple(t1)
# print(id(t1))
# print(id(t2))
# print(t1 == t2)
# print(t1 is t2)
# # 可变数据类型浅拷贝
# l1 = [1, 2, 3]
# l2 = list(l1)
# l3 = copy.copy(l1)
# l4 = l1[:]
# print(id(l1))
# print(id(l2))
# print(l1 == l2)
# print(l1 is l2)
# print(id(l3))
# print(id(l4))
#
# l1.append(4)
# print(id(l1))
# print(l1 == l2)
# print(l1 is l2)
#
# print("666666")
# l1 = [[1, 2], (4, 5)]
# l2 = copy.copy(l1)
# print(id(l1))
# print(id(l2))
# print(id(l1[0]))
# print(id(l2[0]))
# l1.append(6)
# print(l1)
# print(l2)
# l1[0].append(3)
# print(l1)
# print(l2)
#
#
#
# ## 深度拷贝
# print("7777777")
# l1 = [[1, 2], (4, 5)]
# l2 = copy.deepcopy(l1)
# print(id(l1))
# print(id(l2))
# l1.append(6)
# print(l1)
# print(l2)
# l1[0].append(3)
# print(l1)
# print(l2)

## python垃圾回收
from sys import getrefcount
#
# print("#############")
# l1 = [1, 2, 3]
# print(getrefcount(l1)) # 查看引用计数
# l2 = l1
# print(getrefcount(l2))

# # del
#
class TestObjectA(dict):
    def __init__(self):
        print("A: hello!!!")
    def __del__(self):
        print("A: bye!!!")
#
# class TestObjectB(dict):
#     def __init__(self):
#         print("B: hello!!!")
#     def __del__(self):
#         print("B: bye!!!")
#
# a = TestObjectA()
# b = a
# c = a
# print(getrefcount(c))
# del a
# print(getrefcount(c))
# del b
# print(getrefcount(c))
# del c
# print("666")

# # 标记清除
# ## 循环引用
# a = TestObjectA()
# b = TestObjectB()
# a['1'] = b
# b['1'] = a
# del a
# del b

# print("666")

# 分代回收
import gc

print(gc.get_threshold())


a = TestObjectA
b = a
print(gc.get_count())
del a
print(gc.get_count())
del b
print(gc.get_count())