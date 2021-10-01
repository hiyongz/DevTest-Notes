#!/usr/bin/python3
# -*-coding:utf-8-*-

from scapy.all import *
import re

package = "packet_request.pcap"
field = 'src=00:0c:29:d9:98:c7'
pkts = rdpcap(package)
for packet in pkts:
    if packet.haslayer('DHCP6_Request'):
        packet_text = repr(packet)
        if re.search(field, packet_text, re.IGNORECASE):
            print("666")