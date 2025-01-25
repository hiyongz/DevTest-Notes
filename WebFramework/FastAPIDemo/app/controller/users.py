#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/17 11:04
# @Author  : hiyongz
# @File    : users.py
# @Project: FastAPIDemo
import asyncio
import time

from fastapi import APIRouter, Depends
from fastapi_pagination import paginate, Params

from app.model import UserSchemaModel, User
from app.schema.request.baseParams import CustomPaginationParams, DeviceIdsIN
from app.schema.response.user import UsersResponse
from app.service.userService import worker_1
from app.utils.constant import HTTP
from app.utils.pagination import pagination
from app.dao.users import UserDao
from app.log import sys_log

router = APIRouter()


# @router.get("/user", response_model=UserResponse)
@router.get("/user")
async def getUser():
    """
    读取用户
    """
    cdn_user = await UserDao().get_user_by_id(1)
    sys_log.info("666666666")
    return {'status_code': HTTP.HTTP_200_OK, "msg": "系统配置信息如下", 'data': cdn_user}


@router.get("/users", response_model=UsersResponse)
async def getUsers(params: Params = Depends()):
    """
    读取用户
    """
    user_list = await UserDao().get_tencet_user_list(0, 0)
    user_page = paginate(user_list, params)
    page_dict = {
        'total': user_page.total,
        'page': user_page.page,
        'pages': user_page.pages,
        'items': user_page.items
    }
    return {'code': HTTP.HTTP_200_OK, "msg": "Success", 'data': page_dict}


@router.get("/users2", response_model=UsersResponse)
async def getUsers2(params: CustomPaginationParams = Depends()):
    """
    读取用户
    """
    user_page = await pagination(UserSchemaModel, User.filter(), params)
    return {'code': HTTP.HTTP_200_OK, "msg": "Success", 'data': user_page}


@router.post("/users3", response_model=UsersResponse)
async def getUsers3(params: CustomPaginationParams):
    """
    读取用户
    """
    user_page = await pagination(UserSchemaModel, User.filter(), params)
    return {'code': HTTP.HTTP_200_OK, "msg": "Success", 'data': user_page}


@router.get("/userAdd")
async def addUser():
    """
    读取用户
    """
    user = await UserDao().create()
    return {'code': HTTP.HTTP_200_OK, "msg": "Success", 'data': user}


@router.post("/coroutine_test")
async def coroutine_test(ids: DeviceIdsIN):
    """
    读取用户
    """
    # # 方法1
    start_time = time.time()
    # tasks = [worker_1(int(id)) for id in ids]
    # result = await asyncio.gather(*tasks)
    #
    # # 方法2
    # tasks = []
    # for id in ids:
    #     tasks.append(worker_1(int(id)))
    # results = await asyncio.gather(*tasks)

    # 方法3
    results = []
    for id in ids.ids:
        results.append(await worker_1(int(id)))
    end_time = time.time()
    print("共耗时：{}秒".format(end_time - start_time))
    return {'code': HTTP.HTTP_200_OK, 'msg': "Success", 'data': results}






