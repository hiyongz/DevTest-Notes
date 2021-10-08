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
    def setup(self):
        self.nodes = {"node1":"http://192.168.20.100:44228/wd/hub","node2":"http://192.168.20.100:16743/wd/hub"}

    def teardown(self):
        self.driver_node1.close()
        self.driver_node2.close()


    def node_drivers(self,node):
        start = time.time()
        capability = DesiredCapabilities.CHROME.copy()
        if node == "node1":
            driver_node1 = Remote(command_executor=self.nodes[node], desired_capabilities=capability)
            self.driver_node1= driver_node1
            self.test_baidu(driver_node1)
        elif node == "node2":
            driver_node2 = Remote(command_executor=self.nodes[node],
                                         desired_capabilities=capability)
            self.driver_node2 = driver_node2
            self.test_qq(driver_node2)

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
        node_list = ["node1","node2"]
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
