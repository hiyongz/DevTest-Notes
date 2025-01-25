#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/24 10:29
# @Author  : hiyongz
# @File    : pagination.py
# @Project: FastAPIDemo
import math

from tortoise.queryset import QuerySet

from app.schema.request.baseParams import CustomPaginationParams
from app.schema.response.response_model import PagePydantic


async def pagination(pydantic_model, query_set: QuerySet, params: CustomPaginationParams, callback=None):
    page: int = params.page
    size: int = params.size
    order_by: str = params.ordr_by
    total = await query_set.count()
    total_pages = math.ceil(total / size)

    if page > total_pages and total:
        page = total_pages
    if order_by:
        query_set = query_set.order_by(order_by)

    query_set = query_set.offset((page - 1) * size)
    query_set = query_set.limit(size)

    if callback:
        query_set = await callback(query_set)

    data = await pydantic_model.from_queryset(query_set)

    return PagePydantic(**{
        "items": data,
        "total": total,
        "page": page,
        "size": size,
        "pages": total_pages
    })
