#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/5 16:31
# @Author:  haiyong
# @File:    login.py
from selenium.webdriver.common.by import By

from pageobject.page.base_page import BasePage
from pageobject.page.register import Register


class Login(BasePage):
    def scan(self):
        pass

    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self._driver)
