#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/9/4 16:48
# @Author:  haiyong
# @File:    test_radio.py

from selenium import webdriver

class TestCheckbox:
    def checkbox_switch(self,switch="ON"):
        self.driver = webdriver.Chrome()
        sw = self.driver.find_element_by_id('id_of_checkbox').is_selected()
        flag = False
        if switch == "ON":
            flag = True
        if sw^flag:
            self.driver.find_element_by_id('id_of_checkbox').click()
        self.driver.quit()