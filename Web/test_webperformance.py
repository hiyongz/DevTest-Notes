#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/26 20:15
# @Author:  haiyong
# @File:    test_webperformance.py
from selenium import webdriver


class TestWebPerformance():
    def test_web_performance(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")
        print(driver.execute_script("return JSON.stringify(window.performance.timing)"))
        print(driver.execute_script("return JSON.stringify(window.performance.timing.responseEnd-window.performance.timing.responseStart)"))