#!/usr/bin/python2
#-*-coding:utf-8-*-
# @Time:    2020/3/26 15:42
# @Author:  haiyong
# @File:    test.py
import time
from pywinauto.application import Application
app = Application().start("D:/tftpd32.exe")## 启动tftpd32并创建一个实例对象
# app = Application().connect(process=14992)
app = Application().connect(path="D:/tftpd32.exe")
# about_dlg = app.window(title='Tftpd32 by Ph. Jounin')
about_dlg = app.window(title='Tftpd32 by Ph. Jounin').window(class_name='ComboBox', found_index=1)
about_dlg.print_control_identifiers()