#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/25 15:36
# @Author:  haiyong
# @File:    testcontact.py
import pytest
import yaml

from test_appium_wechatwork.page.app import App


class TestAddContact():

    def setup(self):
        self.main = App().start().main()
        print(self.main)

    def teardown(self):
        pass

    @pytest.mark.parametrize("username, gender, phonenum",yaml.safe_load(open("../data/contact.yml",encoding="utf-8")))
    def test_addcontact(self, username, gender, phonenum):
        self.main.goto_addresslist().\
            click_addmember().click_menualadd().\
            input_name(username).set_gender(gender).input_phone(phonenum).click_save().veriy_toast().click_back()














