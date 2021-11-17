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
        context = self.browser.new_context(locale="zh-CN") # zh-CN、en-GB
        page = context.new_page()
        page.goto("https://www.baidu.com/")
        lan = page.evaluate("window.navigator.language;")
        page.goto("https://www.ip-com.com.cn/")
        time.sleep(3)
        print(lan)
        assert lan == "zh-CN"
        print(page.title())

    def test_edge(self):
        self.browser = self.playwright.chromium.launch(channel="msedge", headless=False)
        context = self.browser.new_context(locale="de-DE")
        page = context.new_page()
        page.goto("https://www.baidu.com/")
        lan = page.evaluate("window.navigator.language;")
        page.goto("https://www.ip-com.com.cn/")
        time.sleep(3)
        print(lan)
        assert lan == "zh-CN"
        print(page.title())

    def test_firefox(self):
        self.browser = self.playwright.firefox.launch(headless=False)
        context = self.browser.new_context(locale="de-DE")
        page = context.new_page()
        page.goto("https://www.baidu.com/")
        lan = page.evaluate("window.navigator.language;")
        page.goto("https://www.ip-com.com.cn/")
        time.sleep(3)
        print(lan)
        assert lan == "zh-CN"
        print(page.title())

    def test_webkit(self):
        self.browser = self.playwright.webkit.launch(headless=False)
        context = self.browser.new_context(locale="de-DE")
        page = context.new_page()
        page.goto("https://www.baidu.com/")
        lan = page.evaluate("window.navigator.language;")
        page.goto("https://www.ip-com.com.cn/")
        time.sleep(3)
        print(lan)
        assert lan == "zh-CN"
        print(page.title())  