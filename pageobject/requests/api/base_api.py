#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/25 20:33
# @Author:  haiyong
# @File:    base_api.py
from pprint import pprint
from string import Template

import requests
import yaml
from jsonpath import jsonpath


class BaseApi:
    def send_api(self, req:dict):
        # 使用 request 完成多请求的改造（post, get, delete）
        pprint(req)
        return requests.request(**req).json()
    @classmethod
    def json_path(cls,json,expr):
        tag_id = jsonpath(json, expr)

    @classmethod
    def yaml_load(cls,path):
        with open(path, "r") as f:
            pprint(yaml.safe_load(f))
            return yaml.safe_load(f)

    @classmethod
    def template(cls, path, data, sub=None):
        with open(path, 'r') as f:
            if sub is None:
                return yaml.load(Template(f.read()).substitute(data))
            else:
                # tag_all.yaml
                return yaml.load(
                    Template(
                        yaml.dump(
                            yaml.load(f)[sub])).substitute(data))