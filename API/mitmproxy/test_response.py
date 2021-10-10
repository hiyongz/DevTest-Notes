#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/23 18:04
# @Author:  haiyong
# @File:    test_response.py

import json

from mitmproxy import http

url_index = dict()
arrays = [-5, -3, -1, 0, 1, 3, 5, 100]


def response(flow: http.HTTPFlow) -> None:
    # if "Content-Type" in flow.response.headers.keys() and \
    #         "json" in flow.response.headers['Content-Type']:
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        url = flow.request.url.split('.json')[0]
        if url not in url_index.keys():
            url_index[url] = 0
        else:
            url_index[url] += 1

        # 去等价类中的某一个，根据访问次数循环使用
        seed = url_index[url] % len(arrays)
        print(seed)
        data = json.loads(flow.response.text)
        # 对数据进行批量修改
        data_new = json_travel(data, num=arrays[seed])
        json_new = json.dumps(data_new, indent=2)
        flow.response.text = json_new


def json_travel(data, array=None, text=1, num=1):
    data_new = None
    # 如果是词典，对词典进行遍历
    if isinstance(data, dict):
        data_new = dict()
        for k, v in data.items():
            data_new[k] = json_travel(v, array, text, num)

    # 如果是列表，对列表的每一项进行遍历
    elif isinstance(data, list):
        data_new = list()
        for item in data:
            item_new = json_travel(item, array, text, num)
            if array is None:
                data_new.append(item_new)
            elif len(data_new) < array:
                data_new.append(item_new)
            else:
                pass
    # 如果是字符串
    elif isinstance(data, str):
        data_new = data * text
    # 如果是int或者float这样的数字
    elif isinstance(data, int) or isinstance(data, float):
        #对数字进行一个乘积计算
        data_new = data * num
    # 其他数据类型保持原样
    else:
        data_new = data
    return data_new


def test_json_travel():
    with open("demo.json") as f:
        data = json.load(f)
        print(json_travel(data, array=0))
        print(json_travel(data, text=5))
        print(json_travel(data, num=5))

