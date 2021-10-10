#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/16 18:29
# @Author:  haiyong
# @File:    test.py.py

# mitmdump -p 8999 -s test.py
def request(flow):
    flow.request.headers['User-Agent'] = 'Lagoujiaoyu'
    print(flow.request.headers)