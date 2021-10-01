#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/23 15:58
# @Author:  haiyong
# @File:    calc_multiProcess.py

# python 多进程

from multiprocessing import Process
from multiprocessing import Pool, cpu_count
import os
import time
from multi_process.mytask import Task

class TestProcess():

    def multiprocess_cpu_bound(self):
        print(f'父进程: {os.getpid()}')
        start = time.time()
        p1 = Process(target=Task.cpu_bound_task, args=(self,100000000,1))
        p2 = Process(target=Task.cpu_bound_task, args=(self,100000000,2))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        end = time.time()
        print("耗时{}秒".format((end - start)))

    def multiprocess_io_bound(self):
        print(f'父进程: {os.getpid()}')
        start = time.time()
        p1 = Process(target=Task.io_bound_task, args=(self,4, 1))
        p2 = Process(target=Task.io_bound_task, args=(self,4, 2))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        end = time.time()
        print("耗时{}秒".format((end - start)))

    def multiprocess_cpu_bound2(self):
        # https://zhuanlan.zhihu.com/p/46368084
        # Pool类创建多进程
        print(f"CPU内核数:{cpu_count()}")
        print(f'父进程: {os.getpid()}')
        start = time.time()
        p = Pool(4)
        for i in range(2):
            p.apply_async(Task.cpu_bound_task, args=(self,100000000,i))
        p.close()
        p.join()
        end = time.time()
        print(f"耗时{end - start}秒")
    def multiprocess_io_bound2(self):
        # Pool类创建多进程
        print(f"CPU内核数:{cpu_count()}")
        print(f'父进程: {os.getpid()}')
        start = time.time()
        p = Pool(8)
        for i in range(2):
            p.apply_async(Task.io_bound_task, args=(self,4, i+1))
        p.close()
        p.join()
        end = time.time()
        print(f"耗时{end - start}秒")


if __name__=='__main__':
    proce = TestProcess()
    proce.multiprocess_cpu_bound()
    proce.multiprocess_io_bound()

