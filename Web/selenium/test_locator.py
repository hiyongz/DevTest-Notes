#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/9/1 15:34
# @Author:  haiyong
# @File:    test_locator.py
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestLocator():
    def setup(self):
        # self.driver = webdriver.Chrome(executable_path=(r'D:/testing_tools/chromedriver85/chromedriver.exe'))
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_id(self):
        self.driver.get("https://www.baidu.com/")
        element = self.driver.find_element_by_id("kw")
        element.send_keys("test")
        element.send_keys(Keys.BACK_SPACE)
        # self.driver.find_element(By.ID,"kw").send_keys("test")
        sleep(5)
        assert element.get_attribute("value") == "test"

    def test_name(self):
        element = self.driver.find_element_by_name("wd")
        element.send_keys("test")
        assert element.get_attribute("value") == "test"

    def test_linktext(self):
        self.driver.get("https://www.baidu.com/")
        element = self.driver.find_element_by_link_text("学术")
        element.click()
        sleep(5)

    def test_partial_link_text(self):
        self.driver.get("https://www.baidu.com/")
        element = self.driver.find_element_by_partial_link_text("123")
        element.click()
        sleep(5)

    def test_xpath(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("test")
        sleep(2)
        self.driver.find_element_by_id("su").click()
        sleep(2)
        element = self.driver.find_element_by_xpath('//*[@id="s_tab"]//a[1]')
        element.click()
        sleep(10)

    def test_xpaths(self):
        # 点击第二个标签
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_xpath('(//*[@id="s-top-left"]/a)[2]').click()
        sleep(10)

    def test_css(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("test")
        self.driver.find_element_by_id("su").click()
        element = self.driver.find_element_by_css_selector("#s_tab a:nth-child(2) + a")
        # element = self.driver.find_element_by_css_selector('#s_tab a:nth-last-child(9)')
        # element = self.driver.find_element_by_xpath('//*[@id="s_tab"]/descendant::a[1]')
        element.click()
        sleep(2)



    def test_css2(self):
        self.driver.get("http://sahitest.com/demo/linkTest.htm")
        # element = self.driver.find_element_by_xpath('//*[contains(@href,"Content")]')
        # element = self.driver.find_element_by_xpath('//*[starts-with(@href,"linkByC")]')
        # element = self.driver.find_element_by_xpath('//*[contains(text(),"Content")]')
        element = self.driver.find_element_by_xpath('//*[text()="linkByContent"]')
        element.click()

if __name__ == '__main__':
    pytest.main()
