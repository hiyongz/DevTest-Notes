#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/3/29 10:03
# @Author:  hiyongz
# @File:    calc.py
class Calc:
    def add(self, a: int, b: int) -> int:
        return a + b

    def add_1(self, para: tuple):
        return para[0] + para[1]

    def div(self, a, b):
        return a / b
