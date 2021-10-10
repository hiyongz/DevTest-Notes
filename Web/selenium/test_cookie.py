#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/1/23 18:40
# @Author:  haiyong
# @File:    test_cookie.py

#!/usr/bin/python3
# -*-coding:utf-8-*-

import json
import time
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import random


class TestCsdn:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="D:/testing_tools/chromedriver86/chromedriver.exe")
        self.driver.get("https://blog.csdn.net/u010698107")
        self.driver.implicitly_wait(10)
    def teardown_method(self):
        self.driver.quit()
        # pass

    def test_brow(self):
        with open("csdn_cookies.txt",'r') as f:
            # cookies = json.load(f)
            cookies:List[Dict] = json.load(f)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        articles = self.driver.find_elements(By.XPATH, '//*[@class="article-item-box csdn-tracking-statistics"]//a')
        time.sleep(3)
        href = []
        for article in articles:
            href.append(article.get_attribute('href'))
        random.shuffle(href)

        for link in href:
            timeout = random.randint(20,120)
            print(timeout)
            print(link)
            self.driver.get(link)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(timeout)

    def test_cookie(self):
        # time.sleep(60)
        # cookies = self.driver.get_cookies()
        # with open("csdn_cookies.txt",'w') as f:
        #     json.dump(cookies,f)
        with open("csdn_cookies.txt",'r') as f:
            # cookies = json.load(f)
            cookies:List[Dict] = json.load(f)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_item_title').click()# 点击添加成员
