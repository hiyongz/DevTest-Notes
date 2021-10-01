#!/usr/bin/python3
# -*-coding:utf-8-*-

from scapy.all import *
pkts = rdpcap('packet_request.pcap')
# pkts = sniff(offline='packet_request.pcap')
pkts[18].show() # 序号为19的报文为DHCPv6 Request报文（通过wireshark查看）

print(repr(pkts[18]))