#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/5/23 11:12
# @Author:  hiyongz
# @File:    test_new_init.py

# __new__和__init__
# https://zhuanlan.zhihu.com/p/35943253
# class Person(object):
#     def __new__(cls, *args, **kwargs):
#         print("__new__ is called")
#         return object.__new__(cls)
#
#     def __init__(self, x, y):
#         print("__init__ is called")
#         self.name = x
#         self.height = y

# class Singleton(object):
#     # 单例模式
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         print("__new__ is called")
#         if cls._instance is None:
#             cls._instance = object.__new__(cls)
#         return cls._instance
#
#     def __init__(self,x, y):
#         print("__init__ is called")
#         self.name = x
#         self.height = y

class Person(object):
    def __init__(self, name, height):
        print("__init__ is called")
        self.name = name
        self.height = height
    def talk(self):
        print("hello")

class Child(Person):
    def __init__(self, name, height):
        super().__init__(name, height)
        self.name = name
        self.height = height

    def print_name(self):
        print(self.name)

class Parent(Person):
    def __init__(self, name, height):
        super().__init__(name, height)

    def print_color(self):
        print("orange is in orange")

class FruitFactory(object):
    fruits = {"apple": Apple, "orange": Orange}

    def __new__(cls, name):
        if name in cls.fruits.keys():
            return cls.fruits[name]()
        else:
            return Fruit()



if __name__ == '__main__':
    # p1 = Person("zhangsan",180)
    # print(p1)
    # print(p1.name)
    # p2 = Person("lishi",175)
    # print(p2)
    # print(p2.name)

    p1 = Singleton("zhangsan",180)
    print(p1)
    print(p1.name)
    p2 = Singleton("lishi", 175)
    print(p2)
    print(p2.name)
    print(p1.name)
    #
    # fruit1 = FruitFactory("apple")
    # fruit2 = FruitFactory("orange")
    # print(fruit1)
    # print(fruit2)
    # fruit1.print_color()
    # fruit2.print_color()