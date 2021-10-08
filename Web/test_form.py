#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/4 19:53
# @Author:  haiyong
# @File:    test_form.py

from selenium import webdriver
from time import sleep


class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=r'D:/testing_tools/chromedriver85/chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown_method(self):
        pass
        # self.driver.quit()

    def test_form_login(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("123")
        self.driver.find_element_by_id("user_password").send_keys("password")
        self.driver.find_element_by_id("user_remember_me").click()
        # self.driver.find_elements_by_xpath('//*[@id="new_user"]/div[4]/input').click()
        sleep(5)
