#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/10/28 15:29
# @Author:  haiyong
# @File:    test_locator.py

from time import sleep

from playwright.sync_api import sync_playwright

class TestLocator():
    def setup(self):
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def teardown(self):
        self.browser.close()

    def test_text(self):
        self.page.goto("https://www.baidu.com/")
        # self.page.click("text=学术")
        self.page.click('"学术"')
        sleep(5)

    def test_id(self):
        self.page.goto("https://www.baidu.com/")
        # self.page.fill("id=kw", "test")
        # self.page.fill('css=[id="kw"]', "test")
        # self.page.fill('css=[class="s_ipt"]', "test")
        self.page.fill('[class="s_ipt"]', "test")
        # self.page.fill('css=[name="wd"]', "test")
        # self.page.click('css=[class="bg s_btn"] >> text=百度一下')
        self.page.click("id=su")
        sleep(5)

    def test_xpath(self):
        self.page.goto("https://www.baidu.com/")
        self.page.fill("id=kw", "test")
        self.page.click("id=su")
        sleep(2)
        self.page.click('//*[@id="s_tab"]//a[2]')
        # self.page.click('//*[@id="s_tab"]//a >> text=资讯')
        sleep(5)

    def test_css_selector(self):
        self.page.goto("https://www.baidu.com/")
        self.page.fill("id=kw", "test")
        self.page.click("id=su")
        sleep(2)
        self.page.click("#s_tab a:nth-child(2) + a")
        sleep(5)

    def test_css_has(self):
        self.page.goto("https://www.baidu.com/")
        self.page.click('#s-top-left:has(a) > a:nth-child(2)')
        # self.page.click('#s-top-left:has(a) >> text=hao123')
        sleep(5)

    def test_css_is(self):
        self.page.goto("https://www.baidu.com/")
        sleep(2)
        self.page.click(':is(a:has-text("新闻"), a:has-text("News"))')
        sleep(5)

    def test_layout(self):
        self.page.goto("https://www.baidu.com/")
        sleep(2)
        self.page.fill("id=kw", "test")
        self.page.click('input:right-of(#kw)')
        sleep(5)

    def test_nth_match(self):
        self.page.goto("https://www.baidu.com/")
        sleep(2)
        self.page.click(':nth-match(#s-top-left > a, 2)')
        sleep(5)