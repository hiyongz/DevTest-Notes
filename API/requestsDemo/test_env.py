#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/23 15:33
# @Author:  haiyong
# @File:    test_env.py

from unittest import TestCase
from test_http import env_demo

class TestApi(TestCase):
    data = {
        "method":"get",
        "url":"http://testing-studio:9999/demo.txt",
        "headers":None,
        "encoding":"base64"
    }
    def test_send(self):
        api = env_demo.Api()
        print(api.send(self.data).text)
