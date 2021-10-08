#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/3 12:00
# @Author:  haiyong
# @File:    test_grid.py
import threading
import time

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote
from selenium.webdriver.common.by import By


class TestGrid:
    def test_edge(self):
        self.driver = webdriver.Edge(executable_path=(r'D:\\testing_tools\\edgedriver89\\msedgedriver.exe'))
        self.driver.get("https://www.baidu.com/")

    def node_drivers(self,node):
        start = time.time()
        if node == "firefox":
            capability = DesiredCapabilities.FIREFOX.copy()
            driver_firefox = Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=capability)
            self.test_baidu(driver_firefox)
        elif node == "chrome":
            capability = DesiredCapabilities.CHROME.copy()
            driver_chrome = Remote(command_executor="http://localhost:4444/wd/hub",
                                         desired_capabilities=capability)
            self.test_qq(driver_chrome)

    # @pytest.mark.parametrize("node", ["firefox","chrome"])
    def test_baidu(self,driver):
        start = time.time()
        driver.get("https://www.baidu.com/")
        ele = driver.find_element(By.ID, 'kw')
        ele.send_keys("test")
        time.sleep(2)
        driver.find_element(By.ID, 'su').click()
        time.sleep(2)
        end = time.time()
        print(f"耗时{end - start}秒")

    def test_qq(self,driver):
        start = time.time()
        driver.get("https://www.qq.com/")
        ele = driver.find_element(By.ID, 'sougouTxt')
        ele.send_keys("qq")
        time.sleep(2)
        driver.find_element(By.ID, 'searchBtn').click()
        time.sleep(2)
        end = time.time()
        print(f"耗时{end - start}秒")

    def test_parallel(self):
        node_list = ["firefox","chrome"]
        thread_list = []
        start = time.time()
        for browser in node_list:
            t = threading.Thread(target=self.node_drivers, args=(browser,))
            thread_list.append(t)

        for t in thread_list:
            t.start()

        for t in thread_list:
            t.join()
        end = time.time()
        print(f"耗时{end - start}秒")
