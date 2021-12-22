#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/6/28 11:21
# @Author:  haiyong
# @File:    test_airtest1.py

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(force_restart=False,use_airtest_input=True, screenshot_each_action=False)
connect_device('Android:///127.0.0.1:7555')

print(device())
install("path/to/your/apk") # 安装APK

start_app("com.xueqiu.android")

touch(Template("image_of_a_button.png"))
swipe(Template("slide_start.png"), Template("slide_end.png"))
assert_exists(Template("success.png"))
keyevent("BACK")
home()

sleep(1.0)

touch((341,297))

sleep(1.0)

swipe((341,297), vector=[0.0131, 0.2495])
text()
keyevent("back")
snapshot(msg="请填写测试点.")
wait()
exists()

assert_exists()
assert_not_exists()
assert_equal()
assert_not_equal()

################## poco ###################
poco.device.wake()
poco("android:id/tabs").child("android.widget.RelativeLayout")[1].offspring(text="行情").click()
poco(resourceId="com.tenda.router.app:id/far_awake_iv_work").sibling(name="android.widget.TextView").get_text()

ele = poco('name')
ele.swipe('up')
ele.swipe([0.2, -0.2])  # swipe sqrt(0.08) unit distance at 45 degree angle up-and-right
ele.swipe([0.2, -0.2], duration=0.5)

poco('name').wait_for_appearance() # 等待元素出现
poco("name").wait_for_disappearance() # 等待元素消失

ele1 = poco('name1')
ele2 = poco('name2')
poco.wait_for_all([ele1,ele2]) # 等待2个UI元素标签全部出现
poco.wait_for_any([ele1,ele2]) # 等待任意一个UI元素出现

sleep(9)
poco("com.acp.main:id/tvTabImg4").click()
poco.click([0.5, 0.5])  # click the center of screen
poco.long_click([0.5, 0.5], duration=3) # 长按

poco('element').set_text() # 向input元素输入文本
poco('element').setattr()


sleep(3)
poco("com.acp.main:id/tvAccount").click()
sleep(3)
poco("com.sinacp.ggaicai:id/etUserName").click()
poco("com.sinacp.ggaicai:id/etUserName").set_text('张三李四')
sleep(3)
poco("com.sinacp.ggaicai:id/etPwd").click()
poco("com.sinacp.ggaicai:id/etPwd").set_text('123UI895')
sleep(3)
poco("com.sinacp.ggaicai:id/tvLogin").click()
sleep(6)



keyevent("BACKSPACE")


from airtest.aircv.aircv import *
from airtest.aircv.template_matching import *
im_source = d.screenshot(format='opencv')
im_target = imread("连接设备.png")
tem = TemplateMatching(im_target, im_source)






