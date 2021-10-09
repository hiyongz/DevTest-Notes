#!/usr/bin/python2
#-*-coding:utf-8-*-
# @Time:    2020/3/26 9:20
# @Author:  haiyong
# @File:    test_wingui.py
import time
from pywinauto.application import Application
app = Application().start("D:/tftpd32.exe")## 启动tftpd32并创建一个实例对象
# app = Application().connect(process=14992)
app = Application().connect(path="D:/tftpd32.exe")
# app.Notepad.menu_select(u'帮助->关于记事本')
time.sleep(.5)
##########edit#########
app.window(title='Tftpd32 by Ph. Jounin').window(class_name='Edit').type_keys(u"D:/pythonproj/testing") # 输入文件存放路径
time.sleep(1)
##########ComboBox#########
about_dlg = app.window(title='Tftpd32 by Ph. Jounin').window(class_name='ComboBox', found_index=1)
about_dlg.click() # 点击Server interface输入框
flag = 0
ips = about_dlg.texts()[1:]  # 获取下拉框的所有内容
ip_num = len(ips)
def combobox_select(num,arrow,target):
    flag = 0
    for _ in range(num):
        server_ip = about_dlg.window_text()  # 返回当前窗口内容 https://stackoverflow.com/questions/38346783/pywinauto-to-get-messagebox-message-content/38347175#38347175
        # about_dlg.print_control_identifiers() # 打印当前窗口内容
        # items = about_dlg.items()
        if server_ip == target:
            return True
        else:
            flag = flag + 1
            app.window(title='Tftpd32 by Ph. Jounin').type_keys("{%s}"%arrow)
            time.sleep(1)
    if flag == num:
        return False

flag_down = combobox_select(ip_num,'DOWN','192.168.5.130')
if not flag_down:
    flag_up = combobox_select(ip_num, 'UP', '192.168.5.130')
    if flag_up:
        print("success!!!")
    else:
        print("fail!!!")
else:
    print("success!!!")

about_dlg.click()
# app.kill()
