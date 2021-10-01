#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/4/30 16:56
# @Author:  haiyong
# @File:    test_argparse.py

# python命令行参数解析 argparse方法

import argparse

# Initialize parser
parser = argparse.ArgumentParser(description="脚本描述信息...")
# 添加参数
parser.add_argument("-f", "--field", help = "字段", action='append')
parser.add_argument("-Y", "--display-filter", help = "条件", nargs='*')
parser.add_argument("-c", "--count", help = "计数", type=int, default=2)

args = parser.parse_args()
print(args)
print(f"field: {args.field}")
print(f"display-filter: {args.display_filter}")
print(f"count: {args.count}")
print(f"type(count): {type(args.count)}")
args = parser.parse_args(['-c3'])
print(f"count: {args.count}")

