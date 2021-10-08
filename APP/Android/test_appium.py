#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/10 21:39
# @Author:  haiyong
# @File:    test_appium.py
import os
import time

from appium import webdriver
# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )
# print(PATH)
desired_caps = {}
# desired_caps['recreateChromeDriverSessions'] = True
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
# desired_caps['deviceName'] = 'WTKDU16813012502'
desired_caps['deviceName'] = 'SNHVB20C18002195'
# desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appPackage'] = 'com.tenda.router.app'
desired_caps['automationName'] = 'Uiautomator2'
# desired_caps['app'] = PATH('D:/testing_tools/tendawifi.apk')
# desired_caps['appActivity'] = '.common.MainActivity'
desired_caps['appActivity'] = '.activity.Anew.Splash.SplashActivity'
desired_caps['newCommandTimeout']=3000
# desired_caps['unicodeKeyboard'] = True
# desired_caps['noReset'] = 'true'
# desired_caps['dontStopAppOnReset'] = 'true'
# desired_caps['skipDeviceInitialization'] = 'true'

# #"adb kill-server",
# cmdlst = ["taskkill /f /im node.exe","taskkill /f /im adb.exe","""start /b node "C:\\Program Files\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js" --address 127.0.0.1 --port 4723 --session-override --no-reset""","adb shell am force-stop "+desired_caps['appPackage']]
# # cmdlst = ["taskkill /f /im node.exe","adb shell am force-stop "+desired_caps['appPackage']]
# #每次运行前先判断屏幕是否点亮,然后再进行操作
# os.system("adb shell input keyevent 26")
# os.system("adb shell input swipe 550 1200 550 375")
# for cmd in cmdlst:
#     os.system(cmd)
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(15)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("京东")
driver.back()
driver.back()

driver.quit()