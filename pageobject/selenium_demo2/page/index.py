#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/5 16:31
# @Author:  haiyong
# @File:    index.py
import time

from selenium.webdriver.common.by import By

from pageobject2.page.add_member import AddMember
from pageobject2.page.base_page import BasePage



class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    def goto_add_member(self):
        # self._driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.find(By.CSS_SELECTOR, ".index_service_cnt_item").click()
        self.find(By.ID, "menu_contacts").click()
        def wait(driver):
            ele_len = len(self.finds(By.ID,"username"))
            if ele_len < 1:
                self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member").click()
            return ele_len >=1
        self.wait_for(wait)
        return AddMember(reuse=True)
    def goto_import_address(self):
        pass
    def goto_member_join(self):
        pass