#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/5 14:52
# @Author:  haiyong
# @File:    test_file.py
from selenium import webdriver
from time import sleep

class TestFile():
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=(r'D:/testing_tools/chromedriver85/chromedriver.exe'))
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys(u"D:/ProgramWorkspace/TestingDemo/test_selenium/img/百度图片.png")
        sleep(3)
