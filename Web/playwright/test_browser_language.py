#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/11/16 9:41
# @Author:  haiyong
# @File:    test_browser_language.py


from playwright.sync_api import sync_playwright
import time

class TestBrowser():

    def setup(self):
        self.playwright = sync_playwright().start()

    def teardown(self):
        self.browser.close()

    def test_chrome(self):
        self.browser = self.playwright.chromium.launch(channel="chrome", headless=False)
        # context = self.browser.new_context(locale="es")
        # context = self.browser.new_context(locale="en-GB")
        # context = self.browser.new_context(locale="es")
        context = self.browser.new_context(locale="zh-CN")
        page = context.new_page()
        page.goto("https://www.baidu.com/")
        lan = page.evaluate("window.navigator.language;")
        page.goto("https://www.ip-com.com.cn/")
        time.sleep(3)
        print(lan)
        assert lan == "zh-CN"
        print(page.title())

    def test_edge(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="msedge", headless=False)
            # context = browser.new_context(locale="zh-CN")
            # context = browser.new_context(locale="en-GB")
            context = browser.new_context(locale="de-DE")
            page = context.new_page()
            page.goto("https://www.baidu.com/")
            print(page.title())

    def test_firefox(self):
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.baidu.com/")
            print(page.title())

    def test_webkit(self):
        with sync_playwright() as p:
            browser = p.webkit.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.baidu.com/")
            print(page.title())