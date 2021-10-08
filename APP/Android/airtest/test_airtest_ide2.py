# -*- encoding=utf8 -*-
__author__ = "Haiyong"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


from airtest.cli.parser import cli_setup
connect_device('Android:///127.0.0.1:7555')
start_app("com.xueqiu.android")
touch(Template(r"tpl1624888768960.png", record_pos=(-0.128, 0.835), resolution=(720, 1280)))


touch(Template(r"tpl1624888778303.png", record_pos=(0.211, -0.781), resolution=(720, 1280)))



text("123")

print(device())

# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)