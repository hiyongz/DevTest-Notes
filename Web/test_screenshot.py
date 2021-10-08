#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/9/2 11:25
# @Author:  haiyong
# @File:    test_screenshot.py

# coding:utf-8
from time import sleep
from PIL import Image
from selenium import webdriver


class TestScreenshot:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_screenshot(self):
        self.driver.get("https://www.baidu.com")
        sleep(2)
        self.driver.save_screenshot('baidu.png')  # 截取当前页面全图
        # self.driver.get_screenshot_as_file('D:\\baidu.png')
        element = self.driver.find_element_by_id("su")  # 百度一下的按钮
        # element.screenshot('D:\\test.png')
        print("获取元素坐标：")
        location = element.location
        print(location)

        print("获取元素大小：")
        size = element.size
        print(size)
        # 计算出元素上、下、左、右 位置
        left = element.location['x']
        top = element.location['y']
        right = element.location['x'] + element.size['width']
        bottom = element.location['y'] + element.size['height']

        im = Image.open('baidu.png')
        im = im.crop((left, top, right, bottom))
        im.save('D:\\baidu.png')

