#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/18 17:38
# @Author:  haiyong
# @File:    test_browser_language.py
"""
设置浏览器语言
"""
from time import sleep
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def get_webdriver(attempts=3, timeout=60, locale='en-us'):

    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("intl.accept_languages", locale)
    firefox_profile.update_preferences()
    driver = webdriver.Firefox(firefox_profile=firefox_profile)
    driver.get('about:preferences')
    driver.implicitly_wait(5)
    driver.find_element_by_id('manageBrowserLanguagesButton').click()
    sleep(5)
    driver.switch_to.frame("iframeResult")
    # driver.find_element_by_id('in-menulist').click()
    # browser-languages-window
    driver.find_element_by_xpath('//*[@id="availableLocales"]').click()
    # driver.find_element(By.CSS_SELECTOR, '.available-locales-list').click()

    # 实例化一个Select类的对象
    selector = Select(driver.find_element_by_id("in-menulist"))
    # 下面三种方法用于选择"篮球运动员"
    selector.select_by_value("ia")  # 通过value属性值进行选择



get_webdriver(locale='en-US')












