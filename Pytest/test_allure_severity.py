#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/8/23 21:33
# @Author:  hiyongz
# @File:    test_allure_severity.py

import allure
import pytest


def test_with_no_severity_label():
    pass


@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
class TestclassWithNormalSeverity(object):
    def test_inside_the_normalseverity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_overriding_critical_severity(self):
        pass


if __name__ == '__main__':
    pytest.main()
