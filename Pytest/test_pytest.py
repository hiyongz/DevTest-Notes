#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/3/23 22:03
# @Author:  hiyongz
# @File:    test_pytest.py
import pytest
from pytest import assume

def calc(a,b):
    return a + b

class TestDemo():
    def test_answer1(self):
        assert calc(1, 1) == 2

    def test_answer2(self):
        # assert calc(2, 1) == 4
        with assume: assert calc(2, 1) == 4
        with assume: assert calc(2, 1) == 3
        with assume: assert calc(2, 2) == 3
        # pytest.assume(1 == 2)
        # pytest.assume(True)
        # pytest.assume(False)

    @pytest.mark.answer3
    def test_answer3(self):
        assert calc(6, 6) == 12

if __name__=='__main__':
    pytest.main()
