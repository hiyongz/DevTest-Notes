#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/20 7:04
# @Author:  haiyong
# @File:    test_auth.py
import requests
from requests.auth import HTTPBasicAuth
def test_oauth():
    url = "http://httpbin.testing-studio.com/basic-auth/dcbh/123"
    r = requests.get(url=url, auth=HTTPBasicAuth("dcbh","123"))
    print(r.text)