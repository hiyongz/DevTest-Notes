#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/17 14:41
# @Author  : hiyongz
# @File    : userModel.py
# @Project: FastAPIDemo


from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class MyAbstractBaseModel(Model):

    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)
    is_del = fields.IntField(null=False, default="0")

    class Meta:
        abstract = True


class User(MyAbstractBaseModel):

    auth_user_id = fields.CharField(255, null=False, unique=True)
    username = fields.CharField(100, null=True)
    mobile = fields.CharField(100, null=True)
    real_name = fields.CharField(100, null=True)
    email = fields.CharField(100, null=True)
    status = fields.IntField(null=True)
    tencent_user_id = fields.CharField(100, null=True, unique=True)
    tencent_auth_status = fields.IntField(null=True)

    class Meta:
        table = "users"
        table_description = "user info"
        ordering = ["-created_at", "id"]

    class PydanticMeta:
        exclude = ["created_at", "modified_at", "id"]

    def __str__(self):
        return self.auth_user_id if self.auth_user_id else "ClientUserModel"


UserSchemaModel = pydantic_model_creator(User, name="User")
UserInSchemaModel = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)

