#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/18 20:02
# @Author:  haiyong
# @File:    demo.py
import requests
from jsonpath import jsonpath
from hamcrest import *

class TestDemo():
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "testing"
        }
        r = requests.get('http://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "testing"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200
    def test_header(self):
        r = requests.post('http://httpbin.testing-studio.com/post', headers={"h":"header"})
        print(r.text)
        assert r.status_code == 200
        assert r.json()['headers']['H'] == "header"

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "testing"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

    def test_hogwarts_json(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        print(jsonpath(r.json(), '$..name'))
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == "霍格沃兹测试学院公众号"
        assert jsonpath(r.json(),'$..name')[0] == "霍格沃兹测试学院公众号"

    def test_hamcrest(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        # print(r.text)
        print(r.json())
        print(jsonpath(r.json(), '$..name'))
        assert_that(r.json()['category_list']['categories'][0]['name'],equal_to("霍格沃兹测试学院公众号"))

















