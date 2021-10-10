#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/23 16:39
# @Author:  haiyong
# @File:    test_request.py

This example shows how to send a reply from the proxy immediately
without sending any data to the remote server.from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    # pretty_url takes the "Host" header of the request into account, which
    # is useful in transparent mode where we usually only have the IP otherwise.

    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        with open("D:/ProgramWorkspace/TestingDemo/test_mitmproxy/stock2.json",encoding="utf-8") as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers

            )
















