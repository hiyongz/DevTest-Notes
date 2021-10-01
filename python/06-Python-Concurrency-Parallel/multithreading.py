#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/23 16:06
# @Author:  haiyong
# @File:    calc_multithreading.py

# Python多线程

import os
import threading
import time
from multi_process.mytask import Task

class TestThread():

    def multithread_cpu_bound(self):
        start = time.time()
        print(f'主线程: {os.getpid()}')
        thread_list = []
        for i in range(1, 3):
            t = threading.Thread(target=Task.cpu_bound_task, args=(self,100000000,i))
            thread_list.append(t)

        for t in thread_list:
            t.start()

        for t in thread_list:
            t.join()

        end = time.time()
        print(f"耗时{end - start}秒")




    def multithread_io_bound(self):
        start = time.time()
        print(f'主线程: {os.getpid()}')
        thread_list = []
        for i in range(1, 3):
            t = threading.Thread(target=Task.io_bound_task, args=(self,4, i))
            thread_list.append(t)

        for t in thread_list:
            t.start()

        for t in thread_list:
            t.join()

        end = time.time()
        print(f"耗时{end - start}秒")



if __name__=='__main__':
    proce = TestThread()
    proce.multithread_cpu_bound()
    proce.multithread_io_bound()

