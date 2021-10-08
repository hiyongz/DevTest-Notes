#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/8/23 21:52
# @Author:  hiyongz
# @File:    test_allure_attach.py
import allure
import pytest


def test_attach_text():
    allure.attach("纯文本", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一段htmlbody块</body>", "html页面", attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file("test.jpg", name="图片", attachment_tye=allure.attachment_type.JPG)
