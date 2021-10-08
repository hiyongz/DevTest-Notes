#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/8/23 21:07
# @Author:  hiyongz
# @File:    test_allure_link_issue.py

import allure

@allure.link("http://www.baidu.com", name="baidu link")
def test_with_link():
    pass

TEST_CASE_LINK = 'https://github.com'
@allure.testcase(TEST_CASE_LINK, 'Test case title')
def test_with_testcase_link():
    pass

# --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
@allure.issue("140","this is a issue")
def test_with_issue_link():
    pass