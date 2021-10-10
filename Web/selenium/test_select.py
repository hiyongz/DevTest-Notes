#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/26 19:09
# @Author:  haiyong
# @File:    test_select.py
# 操作select标签
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select


class TestSelect():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_select(self):
        self.driver.get("http://sahitest.com/demo/selectTest.htm")
        ele = self.driver.find_element_by_id('s3Id')
        # print(ele.text)
        ele.send_keys("o2val")
        # print(ele.get_attribute("value"))
        selected_element = Select(ele)  # 实例化Select
        # for select in selected_element.options:
        #     print(select.text)

        selected_element.select_by_index(1)
        # for select in selected_element.all_selected_options:
        #     print(select.text)
        # print(selected_element.first_selected_option.text) # 打印当前选择的选项值
        sleep(1)
        selected_element.select_by_value("o2val")
        # print(selected_element.first_selected_option.text)
        sleep(1)
        selected_element.select_by_visible_text("o3")
        # print(selected_element.first_selected_option.text)
        sleep(1)

        ## 多选
        ele2 = self.driver.find_element_by_id('s4Id')
        selected_element2 = Select(ele2)  # 实例化Select
        selected_element2.select_by_index(1)
        selected_element2.select_by_index(2)
        selected_element2.select_by_index(3)
        print("######")
        for select in selected_element2.all_selected_options:
            print(select.text)

        print("######")
        selected_element2.deselect_by_index(1)
        for select in selected_element2.all_selected_options:
            print(select.text)

        print("######")
        selected_element2.deselect_by_value("o2val")
        for select in selected_element2.all_selected_options:
            print(select.text)
        print("######")
        selected_element2.deselect_by_visible_text("o3")
        for select in selected_element2.all_selected_options:
            print(select.text)



