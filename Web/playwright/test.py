#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/11/17 14:57
# @Author:  haiyong
# @File:    test.py

from playwright.sync_api import sync_playwright
# from robot.api import logger

class RobotPlaywright():
    """类说明：Facebook WebDriverAgent Python Client Library

    facebook-wda安装：pip3 install -U facebook-wda

    github地址: https://github.com/openatx/facebook-wda
    """

    def __init__(self):
        self.playwright = sync_playwright().start()

    def new_browser_playwright(self, browser="chromium", headless=False):
        """打开一个浏览器实例

        :browser: 打开指定的浏览器，默认为chromium

        :headless: 无头模式，默认关闭

        举例:
        | open browser playwright | chromium |
        """

        if browser == "chromium":
            self.browser = self.playwright.chromium.launch(channel="chrome", headless=headless)
        elif browser == "edge":
            self.browser = self.playwright.chromium.launch(channel="msedge", headless=headless)
        elif browser == "firefox":
            self.browser = self.playwright.firefox.launch(headless=headless)
        elif browser == "webkit":
            self.browser = self.playwright.webkit.launch(headless=headless)

    def new_context_playwright(self, locale="zh-CN"):
        """打开一个浏览器上下文

        :locale: 浏览器语言，默认为zh-CN


        举例:
        | new context playwright | en-US |
        """
        self.context = self.browser.new_context(locale=locale)

    def new_page_playwright(self, url):
        """打开一个页面

        :url: URL地址


        举例:
        | new page playwright | en-US |
        """
        self.page = self.context.new_page(url)

    def go_to_playwright(self, url):
        """进入一个页面

        :url: URL地址


        举例:
        | go to playwright | https://www.baidu.com/ |
        """
        self.page.goto(url)

    def execute_javascript_playwright(self, js):
        """执行javascript脚本

        :js: js命令


        举例:
        | execute javascript playwright | window.navigator.language; |
        """
        res = self.page.evaluate(js)
        return res

    def get_text_playwright(self, locator):
        """获取文本

        :js: js命令


        举例:
        | execute javascript playwright | window.navigator.language; |
        """
        try:
            attr_value = self.page.get_attribute(locator, "value")
            return attr_value
        except Exception as e:
            log_data = '元素不存在'
            raise RuntimeError(log_data)

p = RobotPlaywright()
p.new_browser_playwright()
