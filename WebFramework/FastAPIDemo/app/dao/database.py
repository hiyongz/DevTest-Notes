#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/17 13:14
# @Author  : hiyongz
# @File    : database.py
# @Project: FastAPIDemo
import os

import redis
from config import configs
from tortoise.contrib.fastapi import register_tortoise

# mysql数据库url
SQLALCHEMY_DATABASE_URL = "mysql://{}:{}@{}:{}/{}?charset=utf8".format(
    configs.MYSQL_USER,
    configs.MYSQL_PASSWORD,
    configs.MYSQL_SERVER,
    configs.MYSQL_PORT,
    configs.MYSQL_DB_NAME
)

sqlite_path = os.getcwd() + configs.SQLITE_DB_PATH
if not os.path.exists(sqlite_path):
    os.mkdir(sqlite_path)
sqlite_db_filename = os.path.join(sqlite_path, configs.MYSQL_DB_NAME)
SQLITE_DATABASE_URL = f"sqlite://{sqlite_db_filename}"
# 数据库迁移配置
TORTOISE_ORM = {
    "connections": {"default": SQLITE_DATABASE_URL},
    "apps": {
        "model": {
            "model": ["aerich.model", "app.model.model"],
            # 须添加“aerich.model” 后者“model”是上述models.py文件的路径
            "default_connection": "default",
        },
    },
}

def db_init(app):
    register_tortoise(
        app,
        db_url=SQLITE_DATABASE_URL,
        modules={"model": ["app.model.userModel"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )


pool = redis.ConnectionPool(
    host=configs.REDIS_HOST,
    port=configs.REDIS_PORT,
    password=configs.REDIS_PASSWORD,
    db=configs.REDIS_DB,
)
redis_session = redis.Redis(connection_pool=pool)