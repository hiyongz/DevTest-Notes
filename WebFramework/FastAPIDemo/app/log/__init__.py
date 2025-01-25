#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/6/11 13:23
# @File    : __init__.py.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码
import datetime
import logging
import os

from config import configs

sys_log = logging.getLogger('sysLogger22')


def log_init():
    filename = 'log' + datetime.datetime.now().strftime('%Y%m%d') + '.log'
    log_path = os.getcwd() + configs.LOG_PATH
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_filename = os.path.join(log_path, filename)
    # format_str = logging.Formatter(
    #     '%s(asctime)s - '
    #     '%s(filename)s - '
    #     '%s(levelname)s - '
    #     '%s(message)s'
    # )
    format_str = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    log_level = logging.INFO
    sys_log.setLevel(level=log_level)
    if not sys_log.handlers:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(format_str)

        file_handler = logging.FileHandler(log_filename, mode='a')
        file_handler.setFormatter(format_str)

        sys_log.addHandler(stream_handler)
        sys_log.addHandler(file_handler)
