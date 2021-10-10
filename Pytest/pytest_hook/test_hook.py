#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/3/1 20:17
# @Author:  haiyong
# @File:    test_hook.py
import pytest

@pytest.mark.parametrize("name",["张三","李四"])
def test_name(name):
    print(name)

def test_login():
    print('login')

def test_search():
    print('search')

def test_env(cmdoption):
    # print(cmdoption)
    env,datas = cmdoption
    host = datas['env']['host']
    port = datas['env']['port']
    url = str(host) + ":" + str(port)
    print(url)