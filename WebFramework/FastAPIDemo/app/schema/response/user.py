#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/24 10:54
# @Author  : hiyongz
# @File    : user.py
# @Project: FastAPIDemo
from typing import Union

from pydantic import BaseModel
from app.schema import BaseResponse, BasePageResponse


class UserInfoData(BaseModel):
    """
    个人数据结构
    """
    is_del: int
    auth_user_id: str
    username: str
    mobile: str
    real_name: Union[str, None]
    email: str
    status: int


class UserResponse(BaseResponse):
    data: UserInfoData = None


class UserPage(BasePageResponse):
    items: list[UserInfoData] = None


class UsersResponse(BaseResponse):
    data: UserPage = None
