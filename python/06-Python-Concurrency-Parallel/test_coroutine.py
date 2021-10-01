#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/6/13 16:10
# @Author:  hiyongz
# @File:    test_coroutine.py

import asyncio
import time


async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(2)
    print('worker_1 done')

async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(1)
    print('worker_2 done')

async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    tasks = [task1,task2]

    await asyncio.sleep(1) # 超时取消
    task1.cancel()

    print('before await')
    res = await asyncio.gather(*tasks, return_exceptions=True)
    print(res)
    # for task in tasks:
    #     await task
    #     print(task._state)




start=time.time()
asyncio.run(main())
end=time.time()
print('Running time: %s Seconds'%(end-start))
