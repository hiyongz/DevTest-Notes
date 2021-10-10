#!/usr/bin/python3
# -*-coding:utf-8-*-

# @File:    test_unittest_img.py
import os
import unittest
from BeautifulReport import BeautifulReport
from selenium import webdriver


class UnittestCaseSecond(unittest.TestCase):
    """ 测试代码生成与loader 测试数据"""
    def setUp(self):
        print("开始测试")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com/")
    def tearDown(self):
        print("结束测试")
        self.driver.close()

    def save_img(self, img_name):  #错误截图方法，这个必须先定义好
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}\\{}.png'.format(os.path.abspath(r"D:\\pythonproj\\TestingDemo\\test_unittest\\img"), img_name))

    @BeautifulReport.add_test_img('UnittestCaseSecond_test_equal')
    def test_equal(self):
        """
            test 1==1
        :return:
        """
        import time
        time.sleep(1)
        self.save_img('UnittestCaseSecond_test_equal')
        self.assertTrue(1 == 1)

    # @BeautifulReport.add_test_img('UnittestCaseSecond_test_is_none')
    # def test_is_none(self):
    #     """
    #         test None object
    #     :return:
    #     """
    #     self.save_img('UnittestCaseSecond_test_is_none')
    #     self.assertTrue(1 == 2)

# if __name__ == '__main__':
#     unittest.main()
if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('../test_unittest', pattern='test_unittest_img.py')

    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')