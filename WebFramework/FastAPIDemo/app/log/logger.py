#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/23 9:15
# @Author  : hiyongz
# @File    : logger.py
# @Project: FastAPIDemo


import os
import time
from loguru import logger

from config import configs

# 定位到log日志文件
log_path = os.getcwd() + configs.LOG_PATH

if not os.path.exists(log_path):
    os.mkdir(log_path)
logPath = os.path.join(log_path, f'log_{time.strftime("%Y-%m-%d")}.lof')
logger.configure(extra={"request_id": ""})


# 日志简单配置 文件区分不同级别的日志
logger.add(logPath, rotation="500 MB", encoding='utf-8', enqueue=True,
           format="{time:YYYY-MM-DD HH:mm:ss.ms} [{extra[request_id]}] | {level} | {module}.{function}:{line} : {"
                  "message}",
           level=configs.LOG_LEVEL)

__all__ = ["logger"]