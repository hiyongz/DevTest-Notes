#coding=utf-8
# from __future__ import print_function
import ctypes, sys
import os
cmd = 'netsh interface ip set address name="eth1" source=static address=192.168.10.1 mask=255.255.255.0'
print("argv[1]:", sys.argv[1])
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    # os.popen('netsh interface ip set address name="eth1" source=static address=5.1.1.1 mask=255.255.255.0')
    os.popen(sys.argv[1])
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable, __file__, None, 1)