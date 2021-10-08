#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/5 15:27
# @Author:  haiyong
# @File:    test_alert.py
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

class TestAlert():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_alert(self):
        """
        1、打开网页 https: //www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        2、操作窗口右侧页面,将元素1拖拽到元素2
        3、点击弹框中的确定
        4、点击运行
        5、关闭网页
        """
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        sleep(2)
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()
        # self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)
