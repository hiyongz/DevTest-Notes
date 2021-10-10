#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/25 15:30
# @Author:  haiyong
# @File:    contactaddpage.py
from appium.webdriver.common.mobileby import MobileBy
from test_appium_wechatwork.page.base_page import BasePage


class ContactAddPage(BasePage):
    def input_name(self, username):
        self.find(MobileBy.XPATH,
                  "//*[contains(@text, '姓名')]/..//*[@resource-id='com.tencent.wework:id/ase']").send_keys(username)
        return self

    def set_gender(self, gender):

        self.find(MobileBy.XPATH,
                  "//*[@text='性别']/..//*[@resource-id='com.tencent.wework:id/at7']").click()
        # 选择性别
        if gender == '男':
            self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("男")').click()
        else:
            self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("女")').click()

        return self

    def input_phone(self, phonenum):
        # 输入手机号
        self.find(MobileBy.ID, "com.tencent.wework:id/emh").send_keys(phonenum)
        return self

    def click_save(self):
        from test_appium_wechatwork.page.memberinvitepage import MemberInvitePage
        # 点击 保存
        self.find(MobileBy.ID, "com.tencent.wework:id/gq7").click()
        return MemberInvitePage(self._driver)
