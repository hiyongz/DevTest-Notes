#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/10/28 11:20
# @Author:  haiyong
# @File:    test_browser_context.py
import asyncio

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

        context = await browser.new_context()
        page2 = await context.new_page()
        await page2.goto("https://www.sogou.com/")
        print(await page2.title())
        await page2.fill("input[name=\"query\"]", "test")
        await page2.click("text=搜狗搜索")
        await page2.click("#sogou_page_2")
    print('testcase1 done')

async def testcase2():
    print('testcase2 start')
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page1 = await context.new_page()
        await page1.goto("https://www.sogou.com/")
        print(await page1.title())
        await page1.fill("input[name=\"query\"]", "test")
        await page1.click("text=搜狗搜索")
        await page1.click("#sogou_page_2")

        page2 = await context.new_page()
        await page2.goto("https://www.baidu.com/")
        print(await page2.title())
    print('testcase2 done')


# asyncio.run(testcase1())
asyncio.run(testcase2())