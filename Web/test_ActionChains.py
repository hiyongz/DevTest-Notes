#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/4 18:20
# @Author:  hiyongz
# @File:    test_ActionChains.py
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=(r'D:/testing_tools/chromedriver85/chromedriver.exe'))
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()
    def teardown(self):
        pass
        # self.driver.quit()

    # @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("//*[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//*[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//*[@value='right click me']")
        action= ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)
        action. perform()
        sleep(3)

    # @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element_by_link_text("新闻")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.click()
        action.perform()
        sleep(3)

    # @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_ele = self.driver.find_element_by_id("dragger")
        Item1 = self.driver.find_element_by_xpath("/htmL/body/div[2]")
        Item2 = self.driver.find_element_by_xpath("/html/body/div[3]")
        Item3 = self.driver.find_element_by_xpath("/html/body/div[4]")
        action= ActionChains(self.driver)
        action.drag_and_drop(drag_ele, Item1).pause(1)
        action.click_and_hold(drag_ele).release(Item2).pause(1)
        action.click_and_hold(drag_ele).move_to_element(Item3).release()
        action.perform()
        sleep(3)

    # @pytest.mark.skipe
    # Item 1
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele1 = self.driver.find_element_by_xpath("/htmL/body/label[1]/input")
        ele2 = self.driver.find_element_by_xpath("/html/body/label[2]/table/tbody/tr/td[2]/input")
        ele1.click()
        action= ActionChains(self.driver)
        action.send_keys("testing").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("1").pause(1)
        action.send_keys(Keys.BACK_SPACE)
        action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
        action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)
        action.key_down(Keys.CONTROL,ele2).send_keys('v').key_up(Keys.CONTROL)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

    def click_locxy(self, x, y, left_click=True):
        '''每次移动都是在上一次坐标的基础上（即坐标值是累积的）,所以在每次点击后抵消累积
        dr:浏览器
        x:页面x坐标
        y:页面y坐标
        left_click:True为鼠标左键点击，否则为右键点击
        '''
        if left_click:
            ActionChains(self.driver).move_by_offset(x, y).click().perform()
        else:
            ActionChains(self.driver).move_by_offset(x, y).context_click().perform()
        ActionChains(self.driver).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前
    def test_click_pixel(self):
        """
        通过像素坐标点击
        :return:
        """
        self.driver.get('http://www.baidu.com')
        self.click_locxy(200, 100)  # 鼠标左键点击， 200为x坐标， 100为y坐标
        self.click_locxy(100, 100, left_click=False)  # 鼠标右键点击
        sleep(10)
# if __name__ == '__main__':
#     pytest.main(['-v', '-s', 'test_ActionChains.py'])
#     sleep(3)


















