#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/22 17:10
# @Author:  haiyong
# @File:    test_file.py

# f = open('data.txt')
# print(f.readable())
# # print(f.readlines())
# print(f.readline())
# f.close()

# 读取图片使用‘rb’模式
with open('data.txt') as f:
    # print(f.readlines())
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break