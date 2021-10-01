#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/5/25 9:42
# @Author:  haiyong
# @File:    test_serial.py

import serial
from serial import *
import serial.tools.list_ports


class TestSerial():
    def __init__(self,com):
        self.serialName = com

        plist = list(serial.tools.list_ports.comports())
        # python -m serial.tools.list_ports
        if len(plist) <= 0:
            print("没有发现端口!")
            sys.exit()
        else:
            for s in plist:
                if self.serialName == s.name:

                    break
            print(f"没有发现{self.serialName}端口!")
            sys.exit()

        serialFd = serial.Serial(self.serialName, 115200, timeout=60)

        print("可用端口名>>>", serialFd.name)

        if serialFd.isOpen():
            print("open success")
        else:
            print("open failed")

if __name__ == '__main__':
    plist = serial.tools.list_ports.comports()
    for s in plist:
        print(s.name)

    serialFd = serial.Serial("COM4", 115200, timeout=60)
    if serialFd.isOpen():
        print("open success")
    else:
        print("open failed")

    # ser = TestSerial("COM4")