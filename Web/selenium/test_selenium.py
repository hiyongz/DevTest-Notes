#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/1 22:27
# @Author:  haiyong
# @File:    test_demo1.py
import json
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class TestWeixin:
    def setup(self):
        # 1.复用已有的浏览器
        # chrome_opts = webdriver.ChromeOptions()
        # chrome_opts.debugger_address = "127.0.0.1:8123"
        # self.driver = webdriver.Chrome(options=chrome_opts)

        # 2. 使用cookie登录
        self.driver = webdriver.Chrome()
        # self.driver.get("https://www.baidu.com/")
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(10)
    def teardown_method(self):
        self.driver.quit()

    def test_weixin(self):
        # 百度搜索测试
        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("test")
        # self.driver.find_element(By.ID,'kw').send_keys("test")
        # self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("test")
        # self.driver.find_element(By.CSS_SELECTOR,'id=kw').send_keys("test")
        # self.driver.find_element(By.ID, 'su').click()

        # 企业微信
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_item_title').click()# 点击添加成员

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # with open("cookies.txt",'w') as f:
        #     json.dump(cookies,f)
        with open("cookies.txt",'r') as f:
            # cookies = json.load(f)
            cookies:List[Dict] = json.load(f)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_item_title').click()# 点击添加成员
