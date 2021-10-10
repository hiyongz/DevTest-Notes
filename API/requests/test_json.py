#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/1/5 20:56
# @Author:  haiyong
# @File:    test_json.py
import requests

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)
print(r)
print(r.text)
print(r.url)
