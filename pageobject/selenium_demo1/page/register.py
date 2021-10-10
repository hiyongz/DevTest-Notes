#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/5 16:24
# @Author:  haiyong
# @File:    register.py
from selenium.webdriver.common.by import By

from pageobject.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID, "corp_name").send_keys("test1")
        self.find(By.ID, "manager_name").send_keys("test2")
        return True
