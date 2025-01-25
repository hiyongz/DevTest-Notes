#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Senzhong
# @Time    : 2020/5/28 10:04
# @File    : __init__.py.py
# @Software: 这是运行在一台超级计算机上的很牛逼的Python代码

from pydantic import BaseModel


class BaseResponse(BaseModel):
    code: int
    msg: str


class BasePageResponse(BaseModel):
    page: int
    size: int
    pages: int
    total: int
