#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/5 16:13
# @Author:  haiyong
# @File:    base_page.py
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver


class BasePage():
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        self._driver = ""
        if driver is None:
            self._driver = webdriver.Chrome(executable_path=(r'D:/testing_tools/chromedriver93/chromedriver.exe'))
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)
