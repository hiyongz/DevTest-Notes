#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/23 12:06
# @Author:  haiyong
# @File:    test_encode.py
import base64

import requests
import json

class ApiRequest:
    def send(self,data:dict):
        res = requests.request(data["method"],data["url"],headers=data["headers"])
        if data["encoding"] == "base64":
            return json.loads(base64.b64decode(res.content))
        ## 把加密后的响应发给第三方服务，让第三方服务解密
        elif data["encoding"] == "private":
            return requests.post("url",data=res.content)