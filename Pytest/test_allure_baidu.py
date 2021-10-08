#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/8/23 22:12
# @Author:  hiyongz
# @File:    test_allure_baidu.py

import allure
import pytest
from selenium import webdriver
import time

@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome("D:/testing_tools/chromedriver85/chromedriver.exe")
        driver.get("http://www.baidu.com")

    with allure.step("搜索关键词"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)
        allure.attach('<head></head><body>首页</body>', 'Attach with HTML type', allure.attachment_type.HTML)

    with allure.step("退出浏览器"):
        driver.quit()
