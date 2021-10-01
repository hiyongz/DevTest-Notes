#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/3/11 21:24
# @Author:  haiyong
# @File:    test_timer.py

import functools
import time

def timer(func):
    # 统计函数执行时间
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"{func.__name__} 执行时间为：{run_time:.4f} 秒")
        return value
    return wrapper_timer

@timer
def test_sum(num):
    sum = 0
    for i in range(num+1):
        sum = sum + i
    print(sum)

test_sum(100000)