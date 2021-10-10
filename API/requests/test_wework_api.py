#!/usr/bin/python3
# -*-coding:utf-8-*-

import json

import pytest
import requests


class TestWeworkApi:
    # secret = '4pMEU2kLr_a_J8ff032nlWs5X991g8qytjpZJqcWoFI'
    secret = 'sYlpdAIwZiJ54sQVrgnyxT4SxqNeBBNfwrwOpoVhIkE'
    id = 'ww3829a2b3ac7808e0'

    def setup(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.id}&corpsecret={self.secret}'
        r = requests.get(url)
        self.token = r.json()["access_token"]
        print(self.token)

    def test_wework_api(self):
        ## 获取成员
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=test'
        r = requests.get(url)
        print(r.json())
        a = r.json()
        if r.json()["errcode"] == 0:
            ## 删除成员
            url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=test'
            r = requests.get(url)
            print(r.json())

        ## 创建成员
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        data = {
            "userid": "test",
            "name": "test",
            "alias": "jackzhang",
            "mobile": "13800000000",
            "department": [1],
            "order": [10, 40],
            "position": "产品经理",
            "gender": "1",
            "email": "zhangsan@gzdev.com",
        }
        # json.dumps()
        r = requests.post(url, json=data)
        print(r.json())

        ## 更新
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}'
        data = {
            "id": 2,
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        # json.dumps()
        r = requests.post(url, json=data)
        print(r.json())
if __name__=='__main__':
    # pytest.main('-v -x TestDemo')
    pytest.main(['-v','-x','test_wework_api.py'])
    # pytest.main()