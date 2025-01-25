#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/17 10:41
# @Author  : hiyongz
# @File    : config.py
# @Project: FastAPIDemo


import io
import logging
import os
from contextlib import contextmanager
from functools import lru_cache
from io import StringIO
from typing import Optional

from dotenv.main import DotEnv
from pydantic import Field
from pydantic_settings import BaseSettings
from pydantic import  ConfigDict
from pydantic import BaseConfig

logger = logging.getLogger(__name__)


def my_get_stream(self):
    """重写python-dotenv读取文件的方法，使用utf-8，支持读取包含中文的.env配置文件"""
    if isinstance(self.dotenv_path, StringIO):
        yield self.dotenv_path
    elif os.path.isfile(self.dotenv_path):
        with io.open(self.dotenv_path, encoding='utf-8') as stream:
            yield stream
    else:
        if self.verbose:
            logger.warning("File doesn't exist %s", self.dotenv_path)
        yield StringIO('')


DotEnv._get_stream = contextmanager(my_get_stream)


class IgnoredType:
    pass

class Settings(BaseSettings):
    """System configurations."""
    # model_config = ConfigDict(ignored_types=(IgnoredType,))
    # 系统环境
    ENVIRONMENT: Optional[str] = Field(None, env="ENVIRONMENT")

    # 系统安全秘钥
    SECRET_KEY: str = 'ZEuk2U9svM2WRJql4Fs2lEvD05ZDQXZdKboim__SQqsUUqJwStZJq6u0e30bIL4Qe80PB48X1dcIZHjxqLzUiA'

    # API版本号
    API_V1_STR: str = "/api/v1"

    # token过期时间
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # 算法
    ALGORITHM: str = "HS256"

    # 产品名称
    CDN_PRODUCTION_NAME: dict = {
        "cdn": "cdn"
    }
    LOG_PATH: str
    LOG_LEVEL: str
    SQLITE_DB_NAME: str
    SQLITE_DB_PATH: str
    DEV_REDIS_HOST: str
    DEV_REDIS_PORT: str
    DEV_REDIS_USERNAME: str
    DEV_REDIS_PASSWORD: str
    DEV_REDIS_DB: str
    DEV_MYSQL_SERVER: str
    DEV_MYSQL_USER: str
    DEV_MYSQL_PASSWORD: str
    DEV_MYSQL_DB_NAME: str
    DEV_MYSQL_PORT: str
    PROD_REDIS_PORT: str
    PROD_REDIS_USERNAME: str
    PROD_REDIS_PASSWORD: str
    PROD_REDIS_DB: str
    PROD_MYSQL_USER: str
    PROD_MYSQL_PASSWORD: str
    PROD_MYSQL_DB_NAME: str
    PROD_MYSQL_PORT: str
    TEST_REDIS_PORT: str
    TEST_REDIS_USERNAME: str
    TEST_REDIS_PASSWORD: str
    TEST_REDIS_DB: str
    TEST_MYSQL_SERVER: str
    TEST_MYSQL_USER: str
    TEST_MYSQL_PASSWORD: str
    TEST_MYSQL_DB_NAME: str
    TEST_MYSQL_PORT: str

    # 加载.env文件的配置
    class Config:
        env_file = ".env"
        case_sensitive = True


class DevConfig(Settings):
    """Development configurations."""
    # settings22 = Settings()

    # redis
    REDIS_HOST: Optional[str] = Field(Settings().DEV_REDIS_HOST, env="DEV_REDIS_HOST")
    REDIS_PORT: Optional[int] = Field(Settings().DEV_REDIS_PORT, env="DEV_REDIS_PORT")
    REDIS_USERNAME: Optional[str] = Field(Settings().DEV_REDIS_USERNAME, env="DEV_REDIS_USERNAME")
    REDIS_PASSWORD: Optional[str] = Field(Settings().DEV_REDIS_PASSWORD, env="DEV_REDIS_PASSWORD")
    REDIS_DB: Optional[int] = Field(Settings().DEV_REDIS_DB, env="DEV_REDIS_DB")
    # settings23 = Settings()

    # Mysql
    MYSQL_SERVER: Optional[str] = Field(Settings().DEV_MYSQL_SERVER, env="DEV_MYSQL_SERVER")
    MYSQL_USER: Optional[str] = Field(Settings().DEV_MYSQL_USER, env="DEV_MYSQL_USER")
    MYSQL_PASSWORD: Optional[str] = Field(Settings().DEV_MYSQL_PASSWORD, env="DEV_MYSQL_PASSWORD")
    MYSQL_DB_NAME: Optional[str] = Field(Settings().DEV_MYSQL_DB_NAME, env="DEV_MYSQL_DB_NAME")
    MYSQL_PORT: Optional[int] = Field(Settings().DEV_MYSQL_PORT, env="DEV_MYSQL_PORT")


class TestConfig(Settings):
    """Production configurations."""

    REDIS_HOST: Optional[str] = Field(None, env="TEST_REDIS_HOST")
    REDIS_PORT: Optional[int] = Field(None, env="TEST_REDIS_PORT")
    REDIS_USERNAME: Optional[str] = Field(None, env="TEST_REDIS_USERNAME")
    REDIS_PASSWORD: Optional[str] = Field(None, env="TEST_REDIS_PASSWORD")
    REDIS_DB: Optional[int] = Field(None, env="TEST_REDIS_DB")

    MYSQL_SERVER: Optional[str] = Field(None, env="TEST_MYSQL_SERVER")
    MYSQL_USER: Optional[str] = Field(None, env="TEST_MYSQL_USER")
    MYSQL_PASSWORD: Optional[str] = Field(None, env="TEST_MYSQL_PASSWORD")
    MYSQL_DB_NAME: Optional[str] = Field(None, env="TEST_MYSQL_DB_NAME")
    MYSQL_PORT: Optional[int] = Field(None, env="TEST_MYSQL_PORT")


class ProdConfig(Settings):
    """Production configurations."""

    REDIS_HOST: Optional[str] = Field(None, env="PROD_REDIS_HOST")
    REDIS_PORT: Optional[int] = Field(None, env="PROD_REDIS_PORT")
    REDIS_USERNAME: Optional[str] = Field(None, env="PROD_REDIS_USERNAME")
    REDIS_PASSWORD: Optional[str] = Field(None, env="PROD_REDIS_PASSWORD")
    REDIS_DB: Optional[int] = Field(None, env="PROD_REDIS_DB")

    MYSQL_SERVER: Optional[str] = Field(None, env="PROD_MYSQL_SERVER")
    MYSQL_USER: Optional[str] = Field(None, env="PROD_MYSQL_USER")
    MYSQL_PASSWORD: Optional[str] = Field(None, env="PROD_MYSQL_PASSWORD")
    MYSQL_DB_NAME: Optional[str] = Field(None, env="PROD_MYSQL_DB_NAME")
    MYSQL_PORT: Optional[int] = Field(None, env="PROD_MYSQL_PORT")

from pydantic import BaseModel, ConfigDict
class FactoryConfig:
    """Returns a config instance dependending on the ENV_STATE variable."""

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):

        if self.env_state == "development":
            return DevConfig()

        elif self.env_state == "production":
            return ProdConfig()

        elif self.env_state == "testing":
            return TestConfig()


@lru_cache()
def get_configs():
    """加载一下环境文件"""
    from dotenv import load_dotenv
    load_dotenv(encoding='utf-8')
    return FactoryConfig(Settings().ENVIRONMENT)()


configs = get_configs()











