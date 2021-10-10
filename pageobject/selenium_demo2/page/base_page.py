#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/5 16:13
# @Author:  haiyong
# @File:    base_page.py
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    _base_url = ""

    def __init__(self, reuse=False):
        # 把driver提取出来
        # self.driver = None
        if reuse == True:
            # 1.复用已有的浏览器
            chrome_opts = webdriver.ChromeOptions()
            chrome_opts.debugger_address = "127.0.0.1:8123"
            self._driver = webdriver.Chrome(options=chrome_opts)
        else:
            self._driver = webdriver.Chrome()

        self._driver.implicitly_wait(5)
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    # 显式等待
    def wait_for(self, fun):
        # 如果fun返回了True,那么就退出显式等待
        WebDriverWait(self._driver, 10).until(fun)
