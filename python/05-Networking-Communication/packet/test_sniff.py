#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/4/25 11:23
# @Author:  haiyong
# @File:    test_sniff.py

from scapy.all import *

# package = sniff(iface='WLAN', timeout=10)
package = sniff(iface='WLAN', timeout=10, filter="tcp port 80", prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%}"))
wrpcap("test.pcap", package)  # 将抓取的包保存为test.pcap文件
pkts = rdpcap('test.pcap')
pkts[18].show()









