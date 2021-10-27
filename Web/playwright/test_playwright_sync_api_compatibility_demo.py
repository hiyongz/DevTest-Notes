#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/10/22 14:37
# @Author:  haiyong
# @File:    test_playwright_async_api.py

import time
from playwright.sync_api import sync_playwright

def worker_1():
    print('worker_1 start')
    with sync_playwright() as p:
        for br in [p.chromium, p.firefox, p.webkit]:
            browser = br.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.baidu.com/")
            print(page.title())
            page.fill("input[name=\"wd\"]", "test")
            page.click("text=百度一下")
            page.click("#page >> text=2")
            browser.close()
    print('worker_1 done')


start = time.time()
worker_1()
end = time.time()
print('Running time: %s Seconds'%(end-start))
