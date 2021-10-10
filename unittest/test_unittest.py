#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/8/23 10:01
# @Author:  haiyong
# @File:    test_unittest.py
# https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner
import unittest


class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        print("setupclass")

    @classmethod
    def tearDownClass(self) -> None:
        print("teardownclass")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
