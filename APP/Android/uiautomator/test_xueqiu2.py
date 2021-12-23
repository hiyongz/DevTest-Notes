#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/5/18 17:40
# @Author:  haiyong
# @File:    test_tendawifi3.py
import cv2
import uiautomator2 as u2
from airtest.aircv.aircv import *
from airtest.aircv.template_matching import *

class TestU2():
    def setup(self):
        self._device = '127.0.0.1:7555'
        self._appPackage = 'com.xueqiu.android'
        self._appActivity = '.common.MainActivity'

        self.d = u2.connect_usb(self._device)
        self.d.set_new_command_timeout(300)
        self.d.app_start(self._appPackage, self._appActivity)

    def teardown(self):
        # self.d.app_stop(self._appPackage)
        pass

    def test_uiautomator2(self):
        self.d(className="android.widget.TextView", text="行情").click()
        search_ele = self.d(resourceId="com.xueqiu.android:id/action_search").wait(timeout=3.0)
        assert search_ele == True
        self.d(resourceId="com.xueqiu.android:id/action_search").click()
        self.d(resourceId="com.xueqiu.android:id/search_input_text").set_text("招商银行")  # set the text


        self.d.xpath('//*[@text="03968"]').wait(3).click()
        wait_price = self.d(resourceId="com.xueqiu.android:id/current_price")[0].wait(timeout=3.0)
        if not wait_price:
            current_price = self.d(resourceId="com.xueqiu.android:id/current_price")[0].get_text()
            assert float(current_price) < 60
        else:
            assert False

    def test_image(self):
        imdata = "target.png"
        self.d.image.match(imdata)
        self.d.image.click(imdata, timeout=20.0)

    def test_airtest_image(self):
        imdata = "target.png"
        self.match_img(imdata)
        self.touch_img(imdata)

    def match_img(self, img, threshold=0.8):
        """获取当前页面中传入图片的相似度以及位置
        :img: 图片，APP中截取的图片
        :threshold: 阈值
        """
        best_match = self._img_matching(img, threshold=threshold)
        try:
            similarity = best_match["confidence"]
            print("相似度: %s" % similarity)
            return similarity
        except Exception as e:
            raise RuntimeError(e)

    def touch_img(self, img, threshold=0.8):
        """根据图片点击某处
        :img: 图片，APP中截取的图片
        :threshold: 阈值
        """
        best_match = self._img_matching(img, threshold=threshold)
        try:
            self.d.click(*best_match['result'])
        except Exception as e:
            raise RuntimeError(e)

    def _img_matching(self, img, threshold=0.8):
        """在当前页面匹配目标图片
        :img: 目标图片
        :threshold: 相似度阈值
        :return 返回相似度大于阈值的图片信息，例如: {'result': (177, 2153), 'rectangle': ((89, 2079), (89, 2227), (265, 2227), (265, 2079)), 'confidence': 0.7662398815155029, 'time': 0.08855342864990234}
        """
        im_source = self.d.screenshot(format='opencv')
        im_target = imread(img)
        temp = TemplateMatching(im_target, im_source)
        setattr(temp, 'threshold', threshold)
        best_match = temp.find_best_result()
        if best_match is None:
            raise AssertionError("没有匹配到目标图片")
        # logger.info("similarity: %s"%best_match["confidence"])
        return best_match

    def test_key_event(self):
        self.d.press("home")  # 点击home键；也可以使用keycode：d.press(0x03) 效果一样
        self.d.press("back")  # 返回；d.press(0x04)


