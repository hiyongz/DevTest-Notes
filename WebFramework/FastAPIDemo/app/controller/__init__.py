#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/17 10:41
# @Author  : hiyongz
# @File    : __init__.py
# @Project: FastAPIDemo

from app.controller import users
from config import configs


def router_init(app):
    app.include_router(
        users.router,
        prefix=configs.API_V1_STR,
        tags=["Tencent_CDN"],
        # dependencies=[Depends(get_token_header)],
        responses={404: {"description": "Not found"}},
    )
