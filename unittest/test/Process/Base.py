# -*- coding: utf-8 -*-
import time, sys
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from BeautifulReport import BeautifulReport
import unittest
import re,sys,os

def print_a(str):
    #print(str)
    fd = open('../Detaillog.log','a+')
    fd.write(str)
    fd.write('\n')
    fd.flush()
    fd.close()

def Delpng(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".png"): # 填写规则
                os.remove(os.path.join(root, name))
                #print("Delete File: " + os.path.join(root, name))

class Element:
    def isElementPresent(self,driver,by,value):
        '''
        判断元素是否存在
        :param by: 方式
        :param value: 值
        :return: True or False
        '''
        try:
            driver.find_element(by=by,value=value)
        except NoSuchElementException as e:
            print(e)
            return False
        else:
            return True
    
    def Element_Senkey(self,driver,locator,value,data):
        for i in range(2): 
            try:
                if locator == 'id': 
                    time.sleep(5)
                    driver.find_element(By.ID,value).send_keys(data)
                    
                    print(driver.find_element(By.ID,value).is_displayed())                   
                    if driver.find_element(By.ID,value).is_displayed():
                        print("66666666666666666666666666")
                        driver.find_element(By.ID,value).send_keys(data)
                        break
                    else:
                        continue
                elif locator == 'name': 
                    if driver.find_element(By.NAME,value).is_displayed():
                        driver.find_element(By.NAME,value).send_keys(data)
                        break
                    else:
                        continue
                elif locator == 'link_text': 
                    if driver.find_element(By.LINK_TEXT,value).is_displayed():
                        driver.find_element(By.LINK_TEXT,value).send_keys(data)
                        break
                    else:
                        continue
                elif locator == 'xpath': 
                    if driver.find_element(By.XPATH,value).is_displayed():
                        driver.find_element(By.XPATH,value).send_keys(data)
                        break
                    else:
                        continue
                elif locator == 'class_name': 
                    if driver.find_element(By.CLASS_NAME,value).is_displayed():
                        driver.find_element(By.CLASS_NAME,value).send_keys(data)
                        break
                    else:
                        continue
                elif locator == 'tag_name': 
                    if driver.find_element(By.TAG_NAME,value).is_displayed():
                        driver.find_element(By.TAG_NAME,value).send_keys(data)
                        break
                    else:
                        continue
                elif locator == 'partial_link_text':
                    if driver.find_element(By.PARTIAL_LINK_TEXT,value).is_displayed():
                        driver.find_element(By.PARTIAL_LINK_TEXT,value).send_keys(data)
                        break
                    else:
                        continue
                elif locator == 'css_selector': 
                    if driver.find_element(By.CSS_SELECTOR,value).is_displayed():
                        driver.find_element(By.CSS_SELECTOR,value).send_keys(data)
                        break
                    else:
                        continue
                else:
                    print('not id')
            except:
                print('wait 0.5 s')
                driver.refresh()
                time.sleep(0.5)

    def Click_El(self,driver,locator,value):
        for i in range(1):   
            print("222222222222222222") 
            print(locator) 
            print("222222222222222222") 
            try:
                if locator == 'id':
                    if driver.find_element(By.ID,value).is_displayed():
                        driver.find_element(By.ID,value).click()
                        break
                    else:
                        continue
                elif locator == 'name': 
                    if driver.find_element(By.NAME,value).is_displayed():
                        driver.find_element(By.NAME,value).click()
                        break
                    else:
                        continue
                elif locator == 'link_text': 
                    if driver.find_element(By.LINK_TEXT,value).is_displayed():
                        driver.find_element(By.LINK_TEXT,value).click()
                        break
                    else:
                        continue
                elif locator == 'xpath': 
                    if driver.find_element(By.XPATH,value).is_displayed():
                        driver.find_element(By.XPATH,value).click()
                        break
                    else:
                        continue
                elif locator == 'class_name': 
                    if driver.find_element(By.CLASS_NAME,value).is_displayed():
                        driver.find_element(By.CLASS_NAME,value).click()
                        break
                    else:
                        continue
                elif locator == 'tag_name': 
                    if driver.find_element(By.TAG_NAME,value).is_displayed():
                        driver.find_element(By.TAG_NAME,value).click()
                        break
                    else:
                        continue
                elif locator == 'partial_link_text':
                    if driver.find_element(By.PARTIAL_LINK_TEXT,value).is_displayed():
                        driver.find_element(By.PARTIAL_LINK_TEXT,value).click()
                        break
                    else:
                        continue
                elif locator == 'css_selector': 
                    if driver.find_element(By.CSS_SELECTOR,value).is_displayed():
                        driver.find_element(By.CSS_SELECTOR,value).click()
                        break
                    else:
                        continue
                else:
                    print('not id')
            except:
                print('wait 0.5 s')
                driver.refresh()
                time.sleep(0.5)
            


