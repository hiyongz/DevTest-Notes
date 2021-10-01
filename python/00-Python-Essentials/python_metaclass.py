#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/6/5 17:23
# @Author:  hiyongz
# @File:    python_metaclass.py

# Python元类

class MyMetaClass(type):
    def __new__(meta, name, bases, attrs):
        print(meta, "__new__ is called")
        # 动态添加属性
        attrs['name'] = "zhangsan"
        attrs['talk'] = lambda self: print("hello")
        return super(MyMetaClass, meta).__new__(meta, name, bases, attrs)

    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        print(metacls, "__prepare__ is called")
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, attrs, **kwargs):
        print(cls, "__init__ is called")
        super().__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        print(cls, "__call__ is called")
        return super().__call__(*args, **kwargs)


class Myclass(metaclass=MyMetaClass):
    pass

if __name__ == '__main__':
    cla = Myclass()
    print(cla.name)
    cla.talk()
    print(cla.__dir__())