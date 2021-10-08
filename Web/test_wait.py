#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/31 13:57
# @Author:  haiyong
# @File:    test_wait.py

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class Testwait:
    def setup(self):
        self.driver=webdriver. Chrome()
        self.driver.get('https://testerhome.com/')
        self.driver.implicitly_wait(3) #隐式等待
    def test_wait(self):
        self.driver.find_element(By.XPATH,'/*[@title="归入各种类别的所有主题"]').click()
        def wait(x):
           return len(self.driver.find_elements(By.XPATH,'/*[@class="table-heading"]'))>1
        WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element(By.XPATH,'/*[@title="在最近的一年,一月,一周或一天最活跃的主题"]').click()
        ###
        self.driver.find_element(By.XPATH,'/*[@title="归入各种类别的所有主题"]').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@class="table-heading"]')))
        self. driver.find_element(By.XPATH,'*[@title=在最近的一年,一月,一周或一天最活跃的主题"]').click()
