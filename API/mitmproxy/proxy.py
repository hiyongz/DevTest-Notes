#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/23 19:17
# @Author:  haiyong
# @File:    proxy.py

import os
import sys
from mitmproxy import http

addon_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(addon_dir)
from test_mitmproxy.template import Template


def response(flow: http.HTTPFlow):
    if ".json" in flow.request.pretty_url:
        method = flow.request.method
        url = flow.request.pretty_url.split('?')[0]
        params = [{k: v} for k, v in flow.request.query.fields]
        cookies = [{k: v} for k, v in flow.request.cookies.fields]
        data = {
            "method": method.__repr__(),
            "url": url.__repr__(),
            "params": params,
            "cookies": cookies
        }
        print(Template.render(addon_dir + "/test_proxy/test_http.mustache", data))
