#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/24 10:09
# @Author  : hiyongz
# @File    : resp.py
# @Project: FastAPIDemo
from typing import Union, Optional

from pydantic import BaseModel
from starlette.responses import JSONResponse
from app.utils.error_code import ErrorBase
from fastapi import status


class respJsonBase(BaseModel):
    code: str
    msg: str
    data: Union[dict, list]


def respSuccessJson(data: Union[list, dict, str] = None, msg: str = "Success"):
    """
    成功放回
    """
    return JSONResponse(
        status_code=200,
        content={
            'code': '0',
            'msg': msg,
            'data': data or {}
        }
    )


def respErrorJson(error: ErrorBase, *, msg: Optional[str] = None, msg_append: str = "",
                  data: Union[list, dict, str] = None, status_code: int = status.HTTP_200_OK):
    """
    错误返回
    """
    return JSONResponse(
        status_code=200,
        content={
            'code': error.code,
            'msg': (msg or error.msg) + msg_append,
            'data': data or {}
        }
    )
