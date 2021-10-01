#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/22 17:27
# @Author:  haiyong
# @File:    test_json.py
import json

data = {
    "name": "tom",
    "age": 20,
    "gender": "male"
}
print(type(data))

data1 = json.dumps(data)
print(data1)
print(type(data1))

data2 = json.loads(data1)
print(type(data2))