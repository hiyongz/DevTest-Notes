#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/11/11 19:23
# @Author:  haiyong
# @File:    MyKeywords.py

class MyKeywords():
    def test_add(self, a, b, c):
        """两数相加

        :a: value1

        :b: value2

        :c: 预期结果

        Example:
        | Test Add | 2 | 3 | 5 |

        """
        if float(a) + float(b) == float(c):
            return True
        else:
            raise RuntimeError("%s + %s != %s"%(a,b,c))