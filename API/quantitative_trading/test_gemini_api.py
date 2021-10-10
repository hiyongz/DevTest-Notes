#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/1/10 9:54
# @Author:  haiyong
# @File:    test_gemini_api.py

import requests, json

base_url = "https://api.gemini.com/v2"
# base_url = "https://api.sandbox.gemini.com/v2"
response = requests.get(base_url + "/ticker/btcusd")
btc_data = response.json()

print(json.dumps(btc_data, indent=4))












