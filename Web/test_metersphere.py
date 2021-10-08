#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/9/3 13:38
# @Author:  haiyong
# @File:    test_metersphere.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestProjectCreate():
    @pytest.fixture()
    def test_login(self):

        ele = self.driver.find_element_by_link_text("ID 或 邮箱")
        try:
            ele = self.driver.find_element_by_link_text("ID 或 邮箱")
            # self.driver.execute_script('document.getElementById("kw").value = "test"')
            ele.send_keys("admin")
            self.driver.find_element_by_link_text("密码").send_keys("metersphere")
            self.driver.find_element_by_link_text("登录").click()

        except:
            print("666")
            pass
        print("\n登录")

    def setup(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Chrome(executable_path="D:/testing_tools/chromedriver88/chromedriver.exe")
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        # self.driver.quit()
        pass

    def test_ProjectCreate(self):
        self.driver.get("http://192.168.98.21:8081/#/setting/project/all")
        ele_user = self.driver.find_element_by_xpath("//input[@class='el-input__inner' and @type='text']")
        ele_user.send_keys("admin")
        ele_pwd = self.driver.find_element_by_xpath("//input[@class='el-input__inner' and @type='password']")
        ele_pwd.send_keys("metersphere")
        ele_submit = self.driver.find_element_by_xpath("//button[@class='el-button submit el-button--primary']")
        ele_submit.click()
        # self.driver.execute_script('document.getElementById("kw").value = "test"')
        time.sleep(2)
        self.driver.get("http://192.168.98.21:8081/#/setting/project/all")

        self.driver.execute_script('document.getElementsByClassName("el-button el-button--mini is-plain")[0].click()')

        # ele_create = self.driver.find_element_by_xpath("(//button[@class='el-button el-button--mini is-plain'])[1]")
        # ele_create.click()
        ele_project = self.driver.find_element_by_xpath('//div[@aria-label="创建项目"]//input[@class="el-input__inner" and @type="text"]')
        ele_project.send_keys("project1")

        self.driver.find_element_by_xpath('(//div[@class="dialog-footer"]//button[@class="el-button el-button--primary"])[2]').click()

        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[contains(text(),'project1')]").click()
        self.driver.find_element_by_xpath("//*[contains(text(),'测试用例')]").click()
        time.sleep(2)
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(text(),'更多操作')]")))
        time.sleep(20)
        # self.driver.find_element_by_xpath("//*[contains(text(),'更多操作')]").click()
        self.driver.execute_script('document.getElementsByClassName("tip-font")[0].click()')
        self.driver.find_element_by_xpath("//*[contains(text(),'导入')]").click()

        time.sleep(20)
        # ele = self.driver.find_element(By.ID, 'kw')
        # time.sleep(2)
        # ele.send_keys("test")
        # time.sleep(2)
        # self.driver.find_element(By.ID, 'su').click()
        # time.sleep(2)
        # assert self.driver.title == 'test_百度搜索'








