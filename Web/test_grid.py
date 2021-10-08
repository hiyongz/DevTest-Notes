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



class TestGrid:
    def test_edge(self):
        self.driver = webdriver.Edge(executable_path=(r'D:\\testing_tools\\edgedriver89\\msedgedriver.exe'))
        self.driver.get("https://www.baidu.com/")

    @pytest.mark.parametrize("node", ["firefox","chrome"])
    def test_grid(self,node):
        start = time.time()
        if node == "firefox":
            capability = DesiredCapabilities.FIREFOX.copy()
        elif node == "chrome":
            capability = DesiredCapabilities.CHROME.copy()

        self.driver = Remote(command_executor="http://localhost:4444/wd/hub",
                        desired_capabilities=capability)
        self.driver.get("https://www.baidu.com/")
        time.sleep(5)
        end = time.time()
        print(f"耗时{end - start}秒")

    def test_parallel(self):
        node_list = ["firefox","chrome"]
        thread_list = []
        start = time.time()
        for browser in node_list:
            t = threading.Thread(target=self.test_grid, args=(browser,))
            thread_list.append(t)

        for t in thread_list:
            t.start()

        for t in thread_list:
            t.join()
        end = time.time()
        print(f"耗时{end - start}秒")
