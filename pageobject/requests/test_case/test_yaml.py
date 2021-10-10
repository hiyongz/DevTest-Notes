#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/26 20:14
# @Author:  haiyong
# @File:    test_yaml.py
from pprint import pprint
from test_requests.api.base_api import BaseApi
import yaml
def test_load():
    with open("test_tag.yaml","r") as f:
        pprint(yaml.safe_load(f))
def test_template():
    print(BaseApi.template("../api/tag_add.yaml", {"token": "123", "tag_name": "demo"}))