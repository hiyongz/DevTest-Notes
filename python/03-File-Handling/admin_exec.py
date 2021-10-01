#coding=utf-8
# from __future__ import print_function
import ctypes, sys
import os
name="eth2"
address="192.168.10.2"
mask = '255.255.255.0'
cmd = 'netsh interface ip set address name=%s source=static address=%s mask=%s'%(name,address,mask)
print cmd
# print "argv[1]:",argv[1]
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
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)