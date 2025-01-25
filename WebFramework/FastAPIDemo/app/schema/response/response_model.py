#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/24 10:46
# @Author  : hiyongz
# @File    : response_model.py
# @Project: FastAPIDemo
from typing import Generic, TypeVar, Sequence
from pydantic import BaseModel
from app.schema import BaseResponse, BasePageResponse

T = TypeVar("T")


class PagePydantic(BaseModel, Generic[T]):
    items: Sequence[T]
    total: int
    page: int
    size: int
    pages: int


class PageModel(BasePageResponse):
    data: Sequence[T]
