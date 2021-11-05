#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/11/4 15:02
# @Author:  haiyong
# @File:    test_img.py

from airtest.aircv.aircv import *
from airtest.aircv.template_matching import *
from PIL import Image
from PIL import ImageChops
import math

class TestImgMatch():
    def __init__(self):
        self.im_source_path = "selenium-screenshot-12.png"
        # self.im_source_path = "selenium-screenshot-14.png"
        # self.im_source_path = "selenium-screenshot-6.png"
        self.im_target_path = "selenium-screenshot-13.png"


    def test_airtest_kaze(self):

        im_source = imread(self.im_source_path)
        im_target = imread(self.im_target_path)
        tem = TemplateMatching(im_target, im_source)
        # res = tem.find_all_results()
        best_match = tem.find_best_result()
        # print(best_match)
        return best_match['confidence'] if best_match is not None else None


    def test_rms(self, thre = 30):
        im_source_obj = Image.open(self.im_source_path).convert('RGB')
        im_target_obj = Image.open(self.im_target_path).convert('RGB')

        try:
            diff = ImageChops.difference(im_source_obj, im_target_obj)
            if diff.getbbox() is None:
                # 图片间没有任何不同则直接退出
                print("We are the same!")
                return True
            else:
                h = diff.histogram()
                sq = (value * ((idx % 256) ** 2) for idx, value in enumerate(h))
                sum_of_squares = sum(sq)
                rms = math.sqrt(sum_of_squares / float(im_source_obj.size[0] * im_source_obj.size[1]))
                print("rms:", rms)
                if rms < thre:
                    diff.show()
                    print("We are the same!")
                    return True
                else:
                    print("we are not same")
                    diff.show()
                    return False
        except ValueError as e:
            print(e)
            return False

    def test_pil(self):
        im_source_obj = Image.open("selenium-screenshot-14.png")
        im_source_obj2 = Image.open("selenium-screenshot-14.png").convert('RGB')
        print(im_source_obj.mode)

im = TestImgMatch()
confidence = im.test_airtest_kaze()
print(confidence)
# im.test_pil()
# im.test_rms()