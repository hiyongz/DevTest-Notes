#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/5/23 12:19
# @Author:  haiyong
# @File:    test_apirequest.py
from unittest import TestCase
from test_http import test_encode

class TestApiRequest(TestCase):
    rep_data = {
        "method":"get",
        "url":"http://127.0.0.1:9999/demo.txt",
        "headers":None,
        "encoding":"base64"
    }
    def test_send(self):
        ar = test_encode.ApiRequest()
        print(ar.send(self.rep_data))