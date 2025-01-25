#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/30 19:52
# @Author  : hiyongz
# @File    : hello.py
# @Project: FastAPIDemo

from fastapi import APIRouter

from app.log.logger import logger

router = APIRouter()


@router.get("/{name}")
async def root(name):
    logger.info("Root path is Visited")
    hello()
    logger.info(f"{name} Visited")
    return {"message": f"Hello {name}"}


def hello():
    logger.info("hello() called")
