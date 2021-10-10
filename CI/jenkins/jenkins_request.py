#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/6/28 15:20
# @Author:  haiyong
# @File:    jenkins_request.py
import json

import requests

url = "http://admin:admin@192.168.30.8:8080/job/demo/build"

# payload = {'Jenkins-Crumb': 'a43dfa440dc045a49757a93454bbd335c27fbaa90cf65e6d79ef6d6833386e7d'}
header = {'Jenkins-Crumb': '0a49b192a3388815e1bfbb2b7ca88faf0a5e883d9a98195a427e508aa1d08cbf'}
        
# ret = requests.post(url,json=payload)
ret = requests.post(url=url,headers=header)
# ret = requests.post(url=url,cookies=header)

# print(ret.text)


# url = "http://admin:admin@192.168.30.8:8080/job/demo/lastBuild/buildNumber"
# ret = requests.get(url)
# print(ret.text)

# url = "http://admin:admin@192.168.30.8:8080/job/demo/17/api/json"
# ret = requests.get(url)
# print(json.dumps(ret.json(),indent=2))

