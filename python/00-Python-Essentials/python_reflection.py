#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/5/31 21:56
# @Author:  hiyongz
# @File:    python_reflection.py

# Python 反射

class Person():
    def __init__(self, x, y):
        self.age = x
        self.height = y

    def __new__(cls, *args, **kwargs):
        print("begin!!!")
        return object.__new__(cls)

    def __call__(self, *args, **kwargs):
        print("hello!!!")

    def talk(self):
        print(f"My age is {self.age} and height is {self.height}")


p = Person(20, 180)
print(p)
p()
print(p.__dict__)
p.__dict__['age']=22
print(p.__dict__)
p.weight = 60
print(p.__dict__)
print(dir(p))

if (callable(p)):
    print("p is callable")
else:
    print("p is not callable")

#
print(isinstance(p, Person))
print(type(p) == Person)
print(isinstance(p.age, int))
print(type(p.age) == int)

#
print(hasattr(p,"talk"))
print(hasattr(p.talk,"__call__"))

print(getattr(p,"talk"))
print(getattr(p.talk, "__call__"))

if hasattr(p,'walk'):
    print(getattr(p,'walk'))
else:
    print("I can't walk")
print(getattr(p, "walk", None))

setattr(p,'walk','ON')
if hasattr(p,'walk'):
    print(getattr(p,'walk'))
else:
    print("I can't walk")
print(p.__dict__)

delattr(p,'walk')
if hasattr(p,'walk'):
    print(getattr(p,'walk'))
else:
    print("I can't walk")
print(p.__dict__)