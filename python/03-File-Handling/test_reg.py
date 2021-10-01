#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/31 14:45
# @Author:  haiyong
# @File:    test_reg.py
# python3 -m timeit -n 20 -r 5 -s "import os" "os.popen('python3 test_reg.py')"
import re
from collections import defaultdict
path_war_and_peace = 'war_and_peace.txt'
# My regular expression, matching 'Prince' and 'Princess' plus the next word
regex_prince = r'prince(?:ss)? (\w+)'
# I'm going to store results in a dict which return 0 when we ask for a non-existing key
result = defaultdict(int)
with open(path_war_and_peace,'r', encoding='UTF-8') as f:
    for line in f:
        # Note the re.IGNORECASE flag to be case insensitive
        re_result = re.findall(regex_prince, line, re.IGNORECASE)
        for name in re_result:
            result[name] += 1
# print(result)
# import re
# from collections import defaultdict
# path_war_and_peace = 'war_and_peace.txt'
# regex_prince = r'prince(?:ss)? (\w+)'
# # compiled_regex is a Pattern object
# compiled_regex = re.compile(regex_prince, re.IGNORECASE)
# result = defaultdict(int)
# with open(path_war_and_peace,'r', encoding='UTF-8') as f:
#     for line in f:
#         re_result = compiled_regex.findall(line)
#         for name in re_result:
#             # result[name.groups()[0]] += 1
#             result[name] += 1
# print(result)