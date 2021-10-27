#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/10/22 14:37
# @Author:  haiyong
# @File:    test_playwright_async_api.py

import asyncio
import time

from playwright.async_api import async_playwright

async def demo():
    print('worker_1 start')
    async with async_playwright() as p:
        for br in [p.chromium, p.firefox, p.webkit]:
            browser = await br.launch(headless=False)
            page = await browser.new_page()
            await page.goto("https://www.baidu.com/")
            print(await page.title())
            await page.fill("input[name=\"wd\"]", "test")
            await page.click("text=百度一下")
            await page.click("#page >> text=2")
            await browser.close()

    print('worker_1 done')

start = time.time()
# asyncio.run(demo())
asyncio.get_event_loop().run_until_complete(demo())
end = time.time()
print('Running time: %s Seconds'%(end-start))
