#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/25 15:27
# @Author:  haiyong
# @File:    memberinvitepage.py
from appium.webdriver.common.mobileby import MobileBy
from test_appium_wechatwork.page.base_page import BasePage


class MemberInvitePage(BasePage):

    def click_menualadd(self):
        from test_appium_wechatwork.page.contactaddpage import ContactAddPage
        self.find(MobileBy.ID, "com.tencent.wework:id/c56").click()

        return ContactAddPage(self._driver)

    def click_back(self):
        from test_appium_wechatwork.page.addresslistpage import AddressListPage
        return AddressListPage(self._driver)

    def veriy_toast(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")
        return self
