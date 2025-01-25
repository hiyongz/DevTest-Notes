#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/17 14:49
# @Author  : hiyongz
# @File    : users.py
# @Project: FastAPIDemo

from faker import Faker
from app.log import sys_log
from app.model import User, UserSchemaModel
from tortoise import transactions

class UserDao():
    async def create0(self):
        """根据认证ID查询用户"""
        fake = Faker(["zh_CN"])
        id_card = fake.ssn()
        return await UserSchemaModel().create(
            username=fake.name(),
            mobile=fake.phone_number(),
            birthDate=id_card[6:14],
            email=fake.email(),
            status=1
        )

    async def create(self):
        """根据认证ID查询用户"""
        fake = Faker(["zh_CN"])
        id_card = fake.ssn()
        user = User(auth_user_id=1,
                    username=fake.name(),
                    mobile=fake.phone_number(),
                    birthDate=id_card[6:14],
                    email=fake.email(),
                    status=1)
        return await user.save()

    @transactions.atomic()
    async def create_transactions(self):
        """根据认证ID查询用户"""
        fake = Faker(["zh_CN"])
        id_card = fake.ssn()
        user = await UserSchemaModel().create(
            username=fake.name(),
            mobile=fake.phone_number(),
            birthDate=id_card[6:14],
            email=fake.email(),
            status=1
        )
        return user


    async def create_transactions2(self):
        """根据认证ID查询用户"""
        user = ""
        async with transactions.in_transaction():
            fake = Faker(["zh_CN"])
            id_card = fake.ssn()
            user = await UserSchemaModel().create(
                username=fake.name(),
                mobile=fake.phone_number(),
                birthDate=id_card[6:14],
                email=fake.email(),
                status=1
            )
        return user

    async def get_user_by_id(self, user_id: int):
        """根据认证ID查询用户"""
        try:
            user = await UserSchemaModel.from_queryset_single(User.get(auth_user_id=user_id))
        except Exception as e:
            sys_log.error(msg={
                "msg": "查询用户失败",
                "error": "{}".format(e)
            })
            return None
        return user


    async def get_tencet_user_list(self, skip: int, limit: int):
        """查询用户列表"""

        if limit > 10000:
            raise ValueError("最多只能查询10000条数据")

        try:
            rows = await UserSchemaModel.from_queryset(User.all().limit(limit).offset(skip))
        except Exception as e:
            sys_log.error(msg={
                "msg": "查询用户列表失败",
                "error": "{}".format(e)
            })
            return None
        return rows
