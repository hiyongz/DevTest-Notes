#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/24 10:51
# @Author  : hiyongz
# @File    : baseParams.py
# @Project: FastAPIDemo
from typing import List

from fastapi import Query
from fastapi_pagination import Params
from pydantic import BaseModel


class CustomPaginationParams(Params):
    page: int = Query(1, ge=1, description="页码")
    size: int = Query(10, ge=1, le=1000, description="每页条目数")
    order_by: str = Query("id", description="排序字段")


class DeviceIdsIN(BaseModel):
    ids: List = None
