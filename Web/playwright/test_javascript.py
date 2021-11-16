#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/11/16 14:17
# @Author:  haiyong
# @File:    test_javascript.py

from playwright.sync_api import sync_playwright
import time

class TestJs():
    def setup(self):
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(headless=False)
        # self.context = self.browser.new_context()
        # self.page = self.context.new_page()

    def teardown(self):
        self.browser.close()

    def test_case1(self):
        context = self.browser.new_context()
        page = context.new_page()
        page.goto("https://www.baidu.com/")
        lan = page.evaluate("window.navigator.language;")
        print(lan)
        assert lan == "zh-CN"

        title = page.evaluate("document.title;")
        print(title)
        assert title == "zh-CN"


        print(page.title())

    def test_input_text(self):
        context = self.browser.new_context()
        page = context.new_page()
        page.goto("https://www.baidu.com/")

        page.evaluate('document.getElementById("kw").value = "test"')
        text = page.evaluate("document.getElementById('kw').value")
        assert text == "test"

        page.evaluate('document.getElementById("su").click()') # page.click("text=百度一下")
        page.click("#page >> text=2")



        # browser.close()
        time.sleep(30)