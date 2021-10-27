#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/10/22 14:37
# @Author:  haiyong
# @File:    test_playwright_async_api.py

import asyncio
import time

from playwright.async_api import async_playwright

async def testcase1():
    print('testcase1 start')
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.baidu.com/")
        print(await page.title())
        await page.fill("input[name=\"wd\"]", "test")
        await page.click("text=百度一下")
        await page.click("#page >> text=2")
        await browser.close()
    print('testcase1 done')

async def testcase2():
    print('testcase2 start')
    async with async_playwright() as p:
        browser2 = await p.chromium.launch(headless=False)
        page2 = await browser2.new_page()
        await page2.goto("https://www.sogou.com/")
        print(await page2.title())
        await page2.fill("input[name=\"query\"]", "test")
        await page2.click("text=搜狗搜索")
        await page2.click("#sogou_page_2")
        await browser2.close()
    print('testcase2 done')

async def main():
    task1 = asyncio.create_task(testcase1())
    task2 = asyncio.create_task(testcase2())
    tasks = [task1,task2]
    print('before await')
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
end = time.time()
print('Running time: %s Seconds'%(end-start))
