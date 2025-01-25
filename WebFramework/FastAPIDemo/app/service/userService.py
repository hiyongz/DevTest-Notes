#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/24 11:02
# @Author  : hiyongz
# @File    : userService.py
# @Project: FastAPIDemo
import asyncio
import time

from tortoise import transactions

from app.dao.users import UserDao


async def worker_1(num):
    start_time = time.time()
    print(f"worker_{num} start")
    await asyncio.sleep(num)
    print(f"worker_{num} done")
    end_time = time.time()
    print("worker_{} 耗时： {}秒".format(num, end_time - start_time))
    return num


class UserService():
    async def get_user_by_id(self, user_id: int):
        user = await UserDao().get_user_by_id(user_id)
        return user

    @transactions.atomic()
    async def add_user(self):
        user = await UserDao().create()
        a = 1 / 0
        return user
