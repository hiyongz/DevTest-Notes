#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/6/3 22:23
# @Author:  hiyongz
# @File:    test_lambda.py


# 匿名函数
from functools import reduce


def cube(y):
    return y*y*y

lambda_cube = lambda y: y*y*y

print(cube(3))
print(lambda_cube(3))

# 例子1
list_num = [3, 4, 6, 2, 5, 8]
list_square = [x ** 2 for x in list_num if x % 2 == 0]
list_square2 = [(lambda x: x** 2)(x) for x in list_num if x % 2 == 0]
print(list_square)
print(list_square2)

# l1 = [(1, 20), (3, 0), (9, 10), (2, -1)]
# l.sort(key=lambda x: x[1]) # 按列表中元组的第二个元素排序
# print(l)

mydict = {1:"apple",3:"banana",2:"orange"}
mydict = sorted(mydict.items(), key=lambda x: x[0], reverse=True)
print(mydict)

# filter() 函数

list_num = [3, 4, 6, 2, 5, 8]
list_even = list(filter(lambda x: x % 2 == 0, list_num))
print(list_even)

list_even2 = [i for i in list_num if i % 2 == 0]
print(list_even2)

list_even3 = []
for i in list_num:
    if i % 2 == 0:
        list_even3.append(i)
print(list_even3)

list1 = ['', None, 6, 2, False, 8, True]
list1 = list(filter(None, list1))
print(list1)

# map() 函数
print("map")
list_num = [3, 4, 6, 2, 5, 8]
list_square = list(map(lambda x: x**2, list_num))
print(list_square)

list_square2 = [(lambda x: x** 2)(x) for x in list_num]
print(list_square2)

list_square3 = [x**2 for x in list_num]
print(list_square3)

# python -mtimeit -s "list_num=range(1000000)" "list(map(lambda x:x**2, list_num))"
# python -mtimeit -s "list_num=range(1000000)" "[x**2 for x in list_num]"
# python -m timeit -s "list_num=range(1000000)" "l = []" "for x in list_num: l.append(x**2)"

# reduce() 函数
print("reduce")
list_num = [3, 4, 6, 2, 5, 8]
sum = reduce(lambda x, y: x + y, list_num)
print(sum)