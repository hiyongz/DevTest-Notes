#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/17 14:24
# @Author  : hiyongz
# @File    : users.py
# @Project: FastAPIDemo

from typing import Optional, Dict, List

from pydantic import BaseModel

from app.schema import BasePageResponse, BaseResponse


class UserBaseResponse(BaseModel):
    """
    返回数据的基础结构
    """
    status_code: int
    msg: str


class UserInfoData(BaseModel):
    """
    个人实名数据结构
    """
    userIp: str
    userAgent: str
    name: str
    idcard: str
    provinceId: str
    cityId: str
    address: str


class UserResponse(UserBaseResponse):
    data: UserInfoData = None


class UserPage(BasePageResponse):
    items: List[UserInfoData] = None


class UsersResponse(BaseResponse):
    data: UserPage = None
