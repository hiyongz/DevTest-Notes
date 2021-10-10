#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/25 20:33
# @Author:  haiyong
# @File:    wework.py

import requests

from test_requests.api.base_api import BaseApi


class WeWork(BaseApi):
    corpid = 'ww3829a2b3ac7808e0'

    # 获取 token
    def get_token(self, secrete):
        data = {
            "method": "get",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            "params": {
                "corpid": self.corpid,
                "corpsecret": secrete
            }
        }
        return self.send_api(data)['access_token']