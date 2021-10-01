#!/usr/bin/python2
#-*-coding:utf-8-*-
# @Time:    2020/3/30 16:42
# @Author:  haiyong
# @File:    test_scapy.py
from scapy.all import rdpcap
pcaps = rdpcap("packet.pcap")
for data in pcaps:
    if 'UDP' in data:
        s = repr(data)
        print(data.show())
        print(s)
        print(data['Ethernet'].dst)
        break
