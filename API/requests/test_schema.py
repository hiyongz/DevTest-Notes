#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/1/16 18:41
# @Author:  haiyong
# @File:    test_schema.py
import json

import requests
from jsonschema import validate
class TestRequest():
    def test_get_login_jsonschema(self):
        url="https://testerhome.com/api/v3/topics.json"
        data = requests.get(url, params={'limit': '2'}).json()
        schema = json.load(open("topic_schema.json"))
        validate(data, schema=schema)