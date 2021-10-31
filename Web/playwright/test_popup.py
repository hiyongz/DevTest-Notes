#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/10/31 16:57
# @Author:  hiyongz
# @File:    test_popup.py

from time import sleep

from playwright.sync_api import sync_playwright

class TestDemo():
    def setup(self):
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def teardown(self):
        self.browser.close()

    def test_frame(self):
        self.page.goto("https://sahitest.com/demo/confirmTest.htm")
        sleep(2)
        self.page.click('[name="b1"]')
        self.page.on("dialog", lambda dialog: dialog.accept())
        # self.page.click("button")
        sleep(5)

        with self.page.expect_popup() as popup_info:
            self.page.click('[name="b1"]')
        popup = popup_info.value

        popup.wait_for_load_state()
        print(popup.title())

    def test_dialog(self):
        self.page.goto("https://sahitest.com/demo/confirmTest.htm")
        self.page.click('[name="b1"]') # 默认取消对话框

        # 接受对话框
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.click('[name="b1"]')
        sleep(5)
