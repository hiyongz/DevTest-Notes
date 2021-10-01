#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/9/26 16:21
# @Author:  haiyong
# @File:    test_folder.py
import os

print(__file__)

# 获取当前文件__file__的路径
print(os.path.realpath(__file__))

# 获取当前文件__file__的所在目录
print(os.path.dirname(os.path.realpath(__file__)))
# 获取当前文件__file__的所在目录
print(os.path.split(os.path.realpath(__file__))[0])
