#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/10/31 15:22
# @Author:  hiyongz
# @File:    test_frame.py

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
        self.page.goto("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        sleep(2)

        fr = self.page.query_selector('id=iframeResult')
        frame = fr.content_frame()

        # src = self.page.query_selector('id=draggable')
        # dst = self.page.query_selector('id=droppable')
        src = fr.query_selector('id=draggable')
        dst = fr.query_selector('id=droppable')
        print(fr.content_frame())
        print(src)
        print(dst)
        # frame = self.page.frame('iframeResult')
        # frame_element_handle = self.page.query_selector('id=iframeResult')
        # frame = frame_element_handle.content_frame()

    def test_frame2(self):
        self.page.goto("https://sahitest.com/demo/iframesTest.htm")
        frame_element = self.page.query_selector('frame')
        print(frame_element.content_frame())
        frame_element.click()
