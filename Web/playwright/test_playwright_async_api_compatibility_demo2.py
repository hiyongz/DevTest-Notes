#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/10/22 14:37
# @Author:  haiyong
# @File:    test_playwright_async_api.py

import asyncio
import time

from playwright.async_api import async_playwright

async def worker_1():
    print('worker_1 start')
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.baidu.com/")
        print(await page.title())
        await page.fill("input[name=\"wd\"]", "test")
        await page.click("text=百度一下")
        await page.click("#page >> text=2")
        await browser.close()
    print('worker_1 done')

async def worker_2():
    print('worker_2 start')
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.baidu.com/")
        print(await page.title())
        await page.fill("input[name=\"wd\"]", "test")
        await page.click("text=百度一下")
        await page.click("#page >> text=2")
        await browser.close()
    print('worker_2 done')

async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    tasks = [task1,task2]
    print('before await')
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
end = time.time()
print('Running time: %s Seconds'%(end-start))
