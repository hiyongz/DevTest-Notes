#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/5 10:20
# @Author:  haiyong
# @File:    test_frame.py
from time import sleep
from selenium import webdriver

# 多窗口切换
class TestFrame():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        # self. driver. switch_to_frame"iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        # 回到parent_frame
        # self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text) #点击运行
