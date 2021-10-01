#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/6/1 21:29
# @Author:  hiyongz
# @File:    python_reflection2.py

class MyService():
    def service1(self):
        print("service1")

    def service2(self):
        print("service2")

    def service3(self):
        print("service3")

if __name__ == '__main__':
    # Ser = MyService()
    # s = input("请输入您想要的服务: ").strip()
    # if s == "service1":
    #     Ser.service1()
    # elif s == "service2":
    #     Ser.service2()
    # elif s == "service3":
    #     Ser.service3()
    # else:
    #     print("error!")

    Ser = MyService()
    s = input("请输入您想要的服务: ").strip()
    if hasattr(Ser, s):
        func = getattr(Ser, s)
        func()
    else:
        print("error!")