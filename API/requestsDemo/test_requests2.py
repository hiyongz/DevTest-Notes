#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/1/13 22:23
# @Author:  haiyong
# @File:    test_requests2.py
import json

import requests
from jsonpath import jsonpath
from jsonschema import validate
from hamcrest import *

class TestRequest():
    def test_get(self):
        r = requests.get('https://api.github.com/events') #get请求
        # r = requests.get('https://api.github.com/orgs/hiyongz/repos') #get请求
        # r = requests.get('https://api.github.com/repos/hiyongz/DjangoDemo') #get请求
        print(r.status_code)
        assert r.status_code == 200
        # print(r.url)
        # print(r.text)
        # print(r.encoding)
        # print(r.content)
        # json_data = r.json()
        # print(json.dumps(json_data, indent=4))
        # print(r.headers)
        # print(r.cookies)
    def test_json(self):
        r = requests.get('https://api.github.com/repos/hiyongz/DjangoDemo')
        json_data = r.json()
        print(json.dumps(json_data, indent=4))
        print(r.status_code)
        assert r.json()['owner']['login'] == "hiyongz"
        # assert r.status_code == 200
    def test_jsonpath(self):
        r = requests.get('https://api.github.com/repos/hiyongz/DjangoDemo')
        assert jsonpath(r.json(), '$..login')[0] == "hiyongz"

    def test_get_login_jsonschema(self):
        url = "https://api.github.com/repos/hiyongz/DjangoDemo"
        r = requests.get(url)
        data = r.json()
        schema = {
            "name" : "DjangoDemo",
            "owner" : {
            "login" : "hiyongz",
            },
        }
        validate(data, schema=schema)
    def test_hamcrest(self):
        r = requests.get('https://api.github.com/repos/hiyongz/DjangoDemo')
        data = r.json()
        assert_that(data['owner']['login'],equal_to("hiyongz"))


