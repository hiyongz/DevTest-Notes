#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/3/1 20:33
# @Author:  haiyong
# @File:    conftest.py

# D:\Anaconda3\Lib\site-packages\_pytest\hookspec.py
from typing import List

import pytest
import yaml


def pytest_collection_modifyitems(session, config, items: List):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        # 添加login标签
        # pytest -vs -m login test_hook.py
        if 'login' in item.nodeid:
            item.add_marker(pytest.mark.login)
    items.reverse()

# 添加一个命令行参数
def pytest_addoption(parser, pluginmanager):
    mygroup = parser.getgroup("testgroup") #group将下面所有的 optiongroup都展示在这个group下。
    mygroup.addoption("--env", #注册一个命令行选项
        default='test',  # 参数的默认值
        dest = 'env',  # 存储的变量
        help = 'set your run env' #帮助提示参数的描述信息
    )

# 如何针对传入的不同参数完成不同的逻辑处理?创建一个fixture,
@pytest.fixture(scope='session')
def cmdoption(request):
    env = request.config.getoption("--env", default='test')
    if env == "test":
        print("test环境")
        datapath = "data/test/data.yml"
    if env == "develop":
        print("开发环境")
        datapath = "data/develop/data.yml"
    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return env,datas