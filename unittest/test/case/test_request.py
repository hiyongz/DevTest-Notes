# -*- coding: utf-8 -*-
import re,sys,os
import json
import random
import time
import datetime
import unittest
from selenium import webdriver
from BeautifulReport import BeautifulReport
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import os, sys
sys.path.append('..')
from Process.Base import Delpng
from Process.Base import Element
ele = Element()
 
 
class Operation(unittest.TestCase):
   ''' 页面登录 '''
   @classmethod
   #打开浏览器
   def setUpClass(self):
    self.driver = webdriver.Chrome()
    self.driver.get("http://192.168.5.1/main.html")
    self.driver.maximize_window()#窗口最大化
   
   #退出登录，关闭浏览器
   @classmethod
   def tearDownClass(self):
     self.driver.quit()
 
   def setUp(self):
     res = ele.isElementPresent(self.driver,'id','login-password')
     if res is True:
        # ele.Element_Senkey(self.driver,'id','login-password','1dao9')
        print(self.driver.find_element(By.ID,"login-password"))
        self.driver.find_element(By.ID,"login-password").send_keys('1dao9')
        time.sleep(5)
        ele.Click_El(self.driver,'id','subBtn')
        ret = ele.isElementPresent(self.driver,'xpath','//*[@id="system-status"]/div[1]/span/a')
        self.assertEqual(ret,True)
 
   def tearDown(self):
     res = ele.isElementPresent(self.driver,'xpath','//*[@id="system-status"]/div[1]/span/a')
     if res is True:
       ele.Click_El(self.driver,'xpath','//*[@id="system-status"]/div[1]/span/a')

   @BeautifulReport.add_test_img(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
   def test_Login(self):
     print("Login Success")
 
 
 
if __name__ == '__main__' :
  unittest.main()