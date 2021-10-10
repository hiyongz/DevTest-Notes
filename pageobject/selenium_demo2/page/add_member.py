#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/5 17:21
# @Author:  haiyong
# @File:    add_member.py
from selenium.webdriver.common.by import By

from pageobject2.page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self):
        self.find(By.ID, "username").send_keys("test1")
        self.find(By.ID, "memberAdd_acctid").send_keys("test2")
        self.find(By.ID, "memberAdd_phone").send_keys("12345678910")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()

    def get_first(self):
        # return self.find(By.CSS_SELECTOR, "#member_list tr:nth-child(1) td:nth-child(2)").get_attribute("title")
        elems = self.finds(By.CSS_SELECTOR,"td:nth-child(2)")
        arrs = []
        for ele in elems:
            arrs.append(ele.get_attribute("title"))
        return arrs
