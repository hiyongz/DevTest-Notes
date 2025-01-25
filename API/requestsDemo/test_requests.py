#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/20 6:44
# @Author:  haiyong
# @File:    test_cookie.py

import requests

def test_demo():
    url = "http://httpbin.testing-studio.com/cookies"
    header = {#"Cookie":"hogwarts=school",
               'User-Agent': 'hogwarts'
              }
    cookie_data = {"hogwarts":"school"
                   }
    r = requests.get(url=url,headers=header,cookies=cookie_data)
    print(r.request.headers)