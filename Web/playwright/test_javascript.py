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
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def teardown(self):
        # self.browser.close()
        pass

    def test_case1(self):
        self.page.goto("https://www.baidu.com/")
        # 获取浏览器语言
        lan = self.page.evaluate("window.navigator.language;")
        assert lan == "zh-CN"

        # 获取当前浏览器标题："百度一下，你就知道"
        title = self.page.evaluate("document.title;")
        assert title == self.page.title()

        self.page.evaluate('document.getElementById("kw").value = "test"') # 搜索框输入“test”
        text = self.page.evaluate("document.getElementById('kw').value") # 读取输入的值
        assert text == "test"

        self.page.evaluate('document.getElementById("su").click()')  # 点击 【百度一下】；page.click("text=百度一下")
        self.page.click("#page >> text=2")

        time.sleep(5)

    def test_case2(self):
        self.page.goto("https://www.baidu.com/")

        # 搜索框输入“test”
        input_handle = self.page.query_selector("id=kw")
        input_handle.evaluate('node => node.value = "test"')

        text = input_handle.evaluate('node => node.value') # 读取输入的值
        print(text)
        assert text == "test"

        # 点击 【百度一下】
        submit_handle = self.page.query_selector("id=su")
        submit_handle.evaluate('node => node.click()')
        time.sleep(10)
