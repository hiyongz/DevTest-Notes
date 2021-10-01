#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/6/6 15:29
# @Author:  hiyongz
# @File:    test_yaml2.py
import yaml




with open("data2.yaml", encoding="utf-8") as f:
    # steps = yaml.safe_load(f)
    steps = yaml.load(f)
    steps.update({"123":1234})
    print(steps)

with open("data2.yaml", "w", encoding="utf-8") as f:
    yaml.dump(steps,f)