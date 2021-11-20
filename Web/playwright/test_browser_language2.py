#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/11/18 21:48
# @Author:  hiyongz
# @File:    test_browser_language2.py

import asyncio
import time

from playwright.async_api import async_playwright


async def test_chrome():
    print('test_chrome start')
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(locale="en-US")  # zh-CN、en-GB
        page = await context.new_page()
        await page.goto("https://www.baidu.com/")
        lan = await page.evaluate("window.navigator.language;")
        assert lan == "en-US"
        await browser.close()
    print('test_chrome done')


async def test_edge():
    print('test_edge start')
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="msedge", headless=False)
        context = await browser.new_context(locale="en-US")  # zh-CN、en-GB
        page = await context.new_page()
        await page.goto("https://www.baidu.com/")
        lan = await page.evaluate("window.navigator.language;")
        assert lan == "en-US"
        await browser.close()
    print('test_edge done')


async def test_firefox():
    print('test_firefox start')
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        context = await browser.new_context(locale="en-US")  # zh-CN、en-GB
        page = await context.new_page()
        await page.goto("https://www.baidu.com/")
        lan = await page.evaluate("window.navigator.language;")
        assert lan == "en-US"
        await browser.close()
    print('test_firefox done')


async def test_webkit():
    print('test_webkit start')
    async with async_playwright() as p:
        browser = await p.webkit.launch(headless=False)
        context = await browser.new_context(locale="en-US")  # zh-CN、en-GB
        page = await context.new_page()
        await page.goto("https://www.baidu.com/")
        lan = await page.evaluate("window.navigator.language;")
        assert lan == "en-US"
        await browser.close()
    print('test_webkit done')


async def main():
    task1 = asyncio.create_task(test_chrome())
    task2 = asyncio.create_task(test_edge())
    task3 = asyncio.create_task(test_firefox())
    task4 = asyncio.create_task(test_webkit())
    tasks = [task1, task2, task3, task4]
    print('before await')
    await asyncio.gather(*tasks)


start = time.time()
asyncio.run(main())
end = time.time()
print('Running time: %s Seconds' % (end - start))
