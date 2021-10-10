#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/23 18:07
# @Author:  haiyong
# @File:    test_response_basic.py
import json


def response(flow):
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        data = json.loads(flow.response.content)
        data['data']['items'][0]['quote']['name'] = data['data']['items'][0]['quote']['name'] + "test"
        data['data']['items'][0]['quote']['current'] = '50'
        flow.response.text = json.dumps(data)