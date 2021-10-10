#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/25 15:20
# @Author:  haiyong
# @File:    main.py
from appium.webdriver.common.mobileby import MobileBy
from test_appium_wechatwork.page.addresslistpage import AddressListPage

from test_appium_wechatwork.page.base_page import BasePage


class Main(BasePage):
    def goto_message(self):
        pass

    def goto_addresslist(self):
        # self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.steps("../steps/mainsteps.yml")
        return AddressListPage(self._driver)

    def goto_workbench(self):
        pass

    def goto_profile(self):
        pass
