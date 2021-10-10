#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/25 20:38
# @Author:  haiyong
# @File:    test_wework.py

from test_requests.api.wework import WeWork


class TestWeWork:
    def test_get_token(self):
        secrete = 'heLiPlmyblHRiKAgGWZky4-KdWqu1V22FeoFex8RfM0'
        print(WeWork().get_token(secrete))