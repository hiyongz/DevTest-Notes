#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/10/22 14:37
# @Author:  haiyong
# @File:    test_playwright_async_api.py

import time
from playwright.sync_api import sync_playwright

def testcase1():
    print('testcase1 start')
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.baidu.com/")
        print(page.title())
        page.fill("input[name=\"wd\"]", "test")
        page.click("text=百度一下")
        page.click("#page >> text=2")
        browser.close()
    print('testcase1 done')

def testcase2():
    print('testcase2 start')
    with sync_playwright() as p:
        browser2 = p.chromium.launch(headless=False)
        page2 = browser2.new_page()
        page2.goto("https://www.sogou.com/")
        print(page2.title())
        page2.fill("input[name=\"query\"]", "test")
        page2.click("text=搜狗搜索")
        page2.click("#sogou_page_2")
        browser2.close()
    print('testcase2 done')

start = time.time()
testcase1()
testcase2()
end = time.time()
print('Running time: %s Seconds'%(end-start))
