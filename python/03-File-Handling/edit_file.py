#!/usr/bin/python2
# -*-coding:utf-8-*-
# @Time:    2020/4/1 8:43
# @Author:  haiyong
# @File:    test_edit_file2.py
# file = 'test.py'
file = 'admin_exec.py'
def changetext(a, b):
    with open(file, 'r') as f:
        lines = []  # 创建了一个空列表，里面没有元素
        for line in f.readlines():
            if line != '\n':
                lines.append(line)
        f.close()
    # f = open('test.py', "r")
    flag = 0
    with open(file, 'w') as f:
        for line in lines:
            if a in line:
                flag = flag + 1
                line1 = b
                if flag == 1:
                    f.write('%s\n' % line1)
                else:
                    f.write('%s' % line)
            else:
                f.write('%s' % line)


changetext('address', 'address="192.168.10.2"')
changetext('name', 'name="eth2"')
