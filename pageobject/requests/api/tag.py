#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/25 20:33
# @Author:  haiyong
# @File:    tag.py

from test_requests.api.base_api import BaseApi
from test_requests.api.wework import WeWork


class Tag(BaseApi):
    secrete = 's3OypWGu1WoLj4Duudd5PGJgk1LFT4c3mB1Ddl_VGc4'

    def __init__(self):
        self.token = WeWork().get_token(self.secrete)

    def add(self, **data):
        # data = {
        #     "method": "post",
        #     "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
        #     "params": {
        #         "access_token": self.token
        #     },
        #     "json": {
        #         "group_name": "test",
        #         "tag": [{"name": tag_name}]
        #     }
        # }
        data = self.yaml_load("tag_add.yaml")
        ##### 方法1
        # data['params']['access_token'] = self.token
        # data['json']['tag'][0]['name'] = tag_name
        ##### 方法2 ：模板的方法
        self.template("tag_add.yaml", {"token": self.token, "tag_name": tag_name})
        ##### 方法3
        data.update({"token": self.token})
        self.template("tag_add.yaml", data)
        return self.send_api(data)

    def get(self):
        # data = {
        #     "method": "post",
        #     "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
        #     "params": {
        #         "access_token": self.token
        #     },
        #     "json": {
        #         "tag_id": []
        #     }
        # }
        data = self.yaml_load("tag_get.yaml")
        data['params']['access_token'] = self.token
        return self.send_api(data)

    def delete(self, tag_id):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "tag_id": [
                    tag_id
                ]
            }
        }
        return self.send_api(data)

    def update(self, tag_id, name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {

                "id": tag_id,
                "name": name
            }
        }
        return self.send_api(data)