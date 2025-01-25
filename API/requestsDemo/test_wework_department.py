#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/5/25 20:02
# @Author:  haiyong
# @File:    test_wework_department.py
import json

import requests


class TestWeworkApi:
    # secret = '4pMEU2kLr_a_J8ff032nlWs5XXXXXXXXXXXXXXXXXXXX'
    secret = 'sYlpdAIwZiJ54sQVrgnyXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    id = 'wWWWW9aXXXXXXXXXXXXXXXXXXXXX8e0'

    def setup(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.id}&corpsecret={self.secret}'
        r = requests.get(url)
        self.token = r.json()["access_token"]

    def test_department(self):
        ## 获取部门列表
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}&id=2'
        r = requests.get(url)
        print(r.json())
        if r.json()["errcode"] == 0:
            ## 删除部门
            url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id=2'
            r = requests.get(url)
            print(r.json())

        ## 创建部门
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}'
        data = {
            "name": "测试",
            "name_en": "test",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        # json.dumps()
        r = requests.post(url, json=data)
        print(r.json())

        ## 更新
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        data = {
            "userid": "test",
            "name": "test123",
            "department": [1],
            "order": [10],
            "position": "后台工程师",
            "mobile": "13800000000",
            "gender": "1",
            "email": "zhangsan@gzdev.com",
        }
        # json.dumps()
        r = requests.post(url, json=data)
        print(r.json())
