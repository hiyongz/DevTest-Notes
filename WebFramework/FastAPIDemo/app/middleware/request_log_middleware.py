#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/24 12:47
# @Author  : hiyongz
# @File    : request_log_middleware.py
# @Project: FastAPIDemo
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from app.log.logger import logger


class RequestLogMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, header_namespace: str):
        super().__init__(app)
        # 自定义参数，用于定义middleware的header名称空间
        self.header_namespace = header_namespace

    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        with logger.contextualize(request_id=request_id):
            logger.info(f"Request: {request.method} {request.url}")
            logger.debug(f"Request Headers: {request.headers}")
            logger.debug(f"Request Body: {await request.body()}")
            try:
                # 将Request请求传回原路由
                response = await call_next(request)
                logger.info(f"Response Status Code: {response.status_code}")
                logger.debug(f"Response Headers: {response.init_headers()}")
                logger.debug(f"Response Body: {await response.body()}")
                return response
            except Exception as ex:
                logger.error(f"Request failed: {ex}")
                return JSONResponse(
                    content={
                        "code": '500',
                        "msg": ex,
                        "data": {}},
                    status_code=500)
            finally:
                pass
