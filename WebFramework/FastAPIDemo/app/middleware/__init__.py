#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/17 14:19
# @Author  : hiyongz
# @File    : __init__.py
# @Project: FastAPIDemo

from starlette.middleware.cors import CORSMiddleware

from app.middleware.request_log_middleware import RequestLogMiddleware

# 指定允许跨域请求的url
origins = [
    "*"
]


def middleware_init(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # 请求日志中间件
    # app.add_middleware(RequestLogMiddleware, header_namespace="middleware")

