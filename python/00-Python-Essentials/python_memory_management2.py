#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/6/21 16:02
# @Author:  haiyong
# @File:    python_memory_management2.py

## 整型
a1 = 300
b1 = 300
c1 = b1
print(a1 is b1)
print(c1 is b1)
a2 = 200
b2 = 200
c2 = b2
print(a2 is b2)
print(c2 is b2)

a = 1.0
b = 1.0
print(a is b)
print(a == b)

# 字符串
print("string1")
a = 'Hello World'
b = 'Hello World'
c = 'Hello Worl'

print(a is b)
print(a == b)
print(a is c+'d')
print(a == c+'d')

print("string2")
a = "Data Science"
b = "Data Science"
print(id(a))
print(id(b))

print("string3")
a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(id(a))
print(id(b))
print("string4")
a = "aa"*5000
b = "aa"*5000
print(id(a))
print(id(b))


print("##########################")
letter = 'd'
a = 'Hello World'
b = 'Hello World'
c = 'Hello Worl' + 'd'
d = 'Hello Worl' + letter
e = " ".join(['Hello','World'])

print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))

print("##########################")
a = (1,2,3,4)
b = (1,2,3,4)
print(a is b)
print(a == b)

l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
l3 = l2
print(l1 == l2)
print(l1 is l2)
print(l2 == l3)
print(l2 is l3)

print(id(l1))
print(id(l2))
print(id(l3))
print("666")
t1 = (1, 2, 3, 4)
t2 = (1, 2, 3, 4)
t3 = t2
print(id(t1))
print(id(t2))
print(id(t3))

a = (1,2,3)
b = (1,2,3)
print(type(a))
print(a is b)
print(a == b)

a = ('1','2','3')
b = ('1','2','3')
print(type(a))
print(a is b)
print(a == b)

a = ([1,2,3],[1,2])
b = ([1,2,3],[1,2])
print(type(a))
print(a is b)
print(a == b)

import sys
letter_d = 'd'
a = sys.intern('Hello World')
b = sys.intern('Hello World')
c = sys.intern('Hello Worl' + 'd')
d = sys.intern('Hello Worl' + letter)
e = sys.intern(" ".join(['Hello','World']))

print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
