#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/23 15:54
# @Author:  haiyong
# @File:    mytask.py

# CPU密集型和IO密集型任务

import time
import os


class Task():
    def cpu_bound_task(self, n, i):
        print(f'子进程: {os.getpid()} - 任务{i}')
        while n > 0:
            n -= 1

    def io_bound_task(self, n, i):
        print(f'子进程: {os.getpid()} - 任务{i}')
        print(f'IO Task{i} start')
        time.sleep(n)
        print(f'IO Task{i} end')

    def test_cpu_bound(self):
        print('主进程: {}'.format(os.getpid()))
        start = time.time()
        for i in range(2):
            self.cpu_bound_task(100000000,i)
        end = time.time()
        print(f"耗时{end - start}秒")

    def test_io_bound(self):
        print('主进程: {}'.format(os.getpid()))
        start = time.time()
        for i in range(2):
            self.io_bound_task(4,i)
        end = time.time()
        print(f"耗时{end - start}秒")

if __name__ == "__main__":
    t = Task()
    t.test_cpu_bound()
    t.test_io_bound()
