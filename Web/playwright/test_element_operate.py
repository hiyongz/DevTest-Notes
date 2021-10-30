#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/10/30 9:41
# @Author:  haiyong
# @File:    test_element_operate.py

from time import sleep

from playwright.sync_api import sync_playwright
from playwright.sync_api import Playwright
from playwright.sync_api import Page

class TestInput():
    def setup(self):
        # playwright = sync_playwright().start()
        # self.browser = playwright.chromium.launch(headless=False)
        # self.context = self.browser.new_context()
        # self.page = self.context.new_page()
        self.page = Page


    def teardown(self):
        # self.browser.close()
        pass

    def test_click(self):
        self.page.goto("https://sahitest.com/demo/clicks.htm")
        self.page.click('"click me"')
        self.page.dblclick('"dbl click me"')
        self.page.click('"right click me"', button='right')
        self.page.click('"right click me"', modifiers=["Shift"])
        self.page.hover('"Clear"')
        self.page.hover('"Clear"')
        self.page.click('"Clear"', position={'x': 0, 'y': 0})
        sleep(5)

    def test_checkbox_radio(self):
        self.page.goto("https://sahitest.com/demo/clicks.htm")

        # checkbox
        self.page.click('[type="checkbox"][value="Click me"]') # 点击checkbox
        self.page.check('[type="checkbox"][value="Click me"]') # 勾选checkbox

        assert self.page.is_checked('[type="checkbox"][value="Click me"]') is True
        self.page.uncheck('[type="checkbox"][value="Click me"]') # 取消勾选checkbox

        # radio
        self.page.check(':nth-match([type="radio"], 1)') # 勾选radio
        sleep(2)
        self.page.click(':nth-match([type="radio"], 2)') # 点击radio
        sleep(5)

    def test_select(self):
        self.page.goto("http://sahitest.com/demo/selectTest.htm")

        self.page.select_option('select#s3Id', 'o1val') # 单选，通过value选择
        self.page.select_option('select#s3Id', label='o2') # 单选，通过label选择
        self.page.select_option('select#s4Id', value=['o1val','o2val','o3val'])
        self.page.select_option('select#s4Id', label=['o1','o2','o3'])
        sleep(5)

    def test_type(self):
        self.page.goto("https://www.baidu.com/")
        # self.page.type("id=kw", "playwright")
        self.page.type("id=kw", "playwright", delay=100)
        sleep(5)

    def test_press(self):
        self.page.goto("https://www.baidu.com/")
        self.page.type("id=kw", "playwright")
        self.page.press("id=kw", '@')
        self.page.press("id=kw", 'Control+A')
        self.page.press("id=kw", 'Delete')
        self.page.press("id=kw", "Control+Z")
        self.page.press('id=kw', 'Enter')
        sleep(5)

    def test_press2(self):
        self.page.goto("https://keycode.info/")
        self.page.press("body", '@')
        sleep(2)
        self.page.press("body", 'Control+A')
        sleep(2)
        self.page.press('body', 'Enter')
        sleep(5)

    def test_upload_files(self):
        # self.page.goto("https://image.baidu.com/")
        # self.page.click("id=sttb")
        # self.page.click("id=uploadImg")
        # self.page.set_input_files('id=stfile', 'd://test.jpg')
        sleep(5)

