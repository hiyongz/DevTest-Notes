#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/25 15:11
# @Author:  haiyong
# @File:    base_page.py
import logging
from typing import List

import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _black_list = [
        (MobileBy.XPATH, "//*[@text='确定']"),
        (MobileBy.XPATH, "//*[@text='允许']")
    ]
    _error_num = 0
    _error_max = 3
    _param = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        logging.info(locator)
        logging.info(value)
        try:
            return self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator, value)
        except Exception as e:
            if self._error_num > self._error_max:
                raise e
            self._error_num += 1
            # 处理弹框
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    self.find(locator, value)

            raise e

    def steps(self, file):
        with open(file,encoding="utf-8") as f:
            steps: List[dict] = yaml.safe_load(f)
            element: WebElement
            for step in steps:
                logging.info(step)
                if 'by' in step.keys():
                    myby = step['by']

                    if myby == 'id':
                        element = self.find(step['by'], step['locator'])
                    if myby == 'xpath':
                        element = self.find(MobileBy.XPATH, step['locator'])
                if 'action' in step.keys():
                    action = step['action']
                    if action == 'find':
                        pass
                    elif action == 'click':
                        element.click()

                    elif action == 'send':
                        pass
