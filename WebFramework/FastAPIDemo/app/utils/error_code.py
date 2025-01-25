#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/24 10:15
# @Author  : hiyongz
# @File    : error_code.py
# @Project: FastAPIDemo

from pydantic import BaseModel


class ErrorBase(BaseModel):
    code: str
    msg: str


ERROR_PARAMETER_ERROR = ErrorBase(code="400", msg="参数错误")
