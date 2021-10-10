#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/25 15:25
# @Author:  haiyong
# @File:    addresslistpage.py
from appium.webdriver.common.mobileby import MobileBy
from test_appium_wechatwork.page.base_page import BasePage


class AddressListPage(BasePage):

    def click_addmember(self):
        from test_appium_wechatwork.page.memberinvitepage import MemberInvitePage

        # 滚动查找 添加成员
        text = '添加成员'
        self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                                'scrollable(true).instance(0)).'
                                                                f'scrollIntoView(new UiSelector().text("{text}")'
                                                                '.instance(0));').click()
        return MemberInvitePage(self._driver)
