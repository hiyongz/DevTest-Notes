#!/usr/bin/python2
#-*-coding:utf-8-*-
# @Time:    2020/3/26 11:01
# @Author:  hiyongz
# @File:    test2.py
# from pywinauto import application
# app = application.Application.start("notepad.exe")
#
import time
from pywinauto.application import Application

app = Application(backend="win32").start("notepad.exe")
app.Notepad.menu_select(u'帮助->关于记事本')
time.sleep(.5)
#这里有两种方法可以进行定位“关于记事本”的对话框
#top_dlg = app.top_window_() 不推荐这种方式，因为可能得到的并不是你想要的
about_dlg = app.window(title_re = u"关于“记事本”", class_name = "#32770")#这里可以进行正则匹配title
#about_dlg.print_control_identifiers()
app.window(title_re = u'关于“记事本”').window(title_re = u'确定').click()
# app.Notepad.menu_select(u'帮助->关于记事本')
time.sleep(.5) #停0.5s 否则你都看不出来它是否弹出来了！
# ABOUT = u'关于“记事本”'
# OK = u'确定'
# #about_dlg[OK].Click()
# #app[ABOUT][OK].Click()
# app[u'关于“记事本”'][u'确定'].click()
time.sleep(.5)
app.Notepad.type_keys(u"杨彦星")
dig = app.Notepad.menu_select(u"编辑(E)->替换(R)")
Replace = u'替换'
Cancle = u'取消'
time.sleep(.5)
app[Replace][Cancle].click()
Cancle = u'取消'
dialogs = app.windows()








