#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/24 9:58
# @Author  : hiyongz
# @File    : exception.py
# @Project: FastAPIDemo
from starlette.exceptions import HTTPException  # 官方推荐注册异常处理器时，应该注册到来自 Starlette 的 HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def global_exception_handler(request, exc):
    if exc.status_code == 500:
        err_msg = 'Server Internal Error'
    else:
        err_msg = exc.detail
    return JSONResponse({
        'code': exc.status_code,
        'msg': err_msg,
        'data': {}
    })


# 请求数据无效时的错误处理
async def validate_exception_handler(request, exc):
    """
    example: http://127.0.0.1/user/{user_id}
    success: http://127.0.0.1/user/1
    failed: http://127.0.0.1/user/d
    """
    err = exc.errors()[0]
    return JSONResponse({
        'code': '400',
        'err_msg': err['msg'],
        'data': {}
    })


global_exception_handlers = {
    HTTPException: global_exception_handler,
    RequestValidationError: validate_exception_handler
}


class BaseAPIException(HTTPException):
    status_code = 400
    detail = 'api error'

    def __init__(self, detail: str = None, status_code: int = None):
        self.detail = detail or self.detail
        self.status_code = status_code or self.status_code
