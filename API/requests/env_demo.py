#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/23 15:28
# @Author:  haiyong
# @File:    env_demo.py
import base64
import json

import requests
import yaml


class Api:
    env = yaml.safe_load(open("env.yaml"))
    # env = {
    #     "default":"dev",
    #     "testing-studio":
    #     {
    #     "dev":"127.0.0.1",
    #     "test":"127.0.0.2"
    #     }
    # }

    def send(self,data:dict):
        ## 替换
        data["url"] = str(data["url"]).replace("testing-studio",self.env["testing-studio"][self.env["default"]])
        res = requests.request(data["method"],data["url"],headers=data["headers"])
        return res