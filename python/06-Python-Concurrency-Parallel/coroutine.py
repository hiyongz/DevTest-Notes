#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/5/24 20:28
# @Author:  hiyongz
# @File:    calc_coroutine.py
# Python协程
import asyncio
import os
import time

class TestCoroutine():
    async def cpu_bound_task(self,n,i):
        print(f'子进程: {os.getpid()} - 任务{i}')
        # await asyncio.sleep(1)
        while n > 0:
            n -= 1

    async def io_bound_task(self,n,i):
        print(f'子进程: {os.getpid()} - 任务{i}')
        print(f'IO Task{i} start')
        # time.sleep(n)
        await asyncio.sleep(n)
        print(f'IO Task{i} end')


    def asyncio_cpu_bound(self):
        start = time.time()
        loop = asyncio.get_event_loop()
        tasks = [self.cpu_bound_task(100000000,i) for i in range(2)]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
        end = time.time()
        print(f"耗时{end - start}秒")

    def asyncio_io_bound(self):
        start = time.time()
        loop = asyncio.get_event_loop()
        tasks = [self.io_bound_task(4, i) for i in range(20)]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
        end = time.time()
        print(f"耗时{end - start}秒")


if __name__ == '__main__':
    proce = TestCoroutine()
    # proce.asyncio_cpu_bound()
    proce.asyncio_io_bound()
