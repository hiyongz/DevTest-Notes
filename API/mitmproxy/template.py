#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/23 19:19
# @Author:  haiyong
# @File:    template.py

import json
from pprint import pprint

import requests
import yaml


class TestHttp:
    def setup(self):
        pass

    def test_request(self):
        r=requests.request(
            'GET',
            url='https://stock.xueqiu.com/v5/stock/stare/notice.json',
            params={
                    {'_t': '1UNKNOWN06f8104c8f011126b0134ad0b793f1a0.2280621283.1589631314152.1589633999816'},
                    {'_s': 'eb1a7a'},
                    {'x': '0.94'},
                    {'stare_type': 'dynamic,event'},
            },
            cookies={
                    {'xq_a_token': 'f4855c806b2fa994489ea1ec96c74f31ed6b1d21'},
                    {'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjIyODA2MjEyODMsImlzcyI6InVjIiwiZXhwIjoxNTkwMTUzMzU5LCJjdG0iOjE1ODc1NjEzNTkyOTgsImNpZCI6Ikp0WGJhTW43ZVAifQ.YdBlGNRLAaX69EJpdZEFoY1ghJaoudBKJt-Pjd0yY2e7GVcXYRVlmXNS5wI7cb-08fy8Js4aperQoszwaoLzMy4SSXmzCmc2CC96ygp3rzEGggrlMhtVeTxoDIxcevjGnYDmozJHk6LcAGJIP7j8ewgsvwRVszPoJ2Jj-HBSp7ZsByUX82HIsL61iObhMCCVj0ANXDlD2CRqMaWyuv5Q8qYtGqXdn3abliLwai5fUjdKPpafuBahnGScOBP6XyUbsncXG_l35sWaJGinigV3LbH7RHCmFnl16V8eCczXLEUKjOzR9NmVaF61pPYh5IA9f6pKlhqazCCW-GFScYyvRg'},
                    {'u': '2280621283'},
                    {'session_id': ''},
                    {'xid': '0'},
            }
        )
        assert r.status_code == 200