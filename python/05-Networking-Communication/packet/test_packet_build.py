#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/4/9 17:46
# @Author:  haiyong
# @File:    test_packet_build.py

from scapy.all import *
from scapy.layers.dhcp6 import DHCP6_Solicit, DHCP6OptClientId, DHCP6OptIA_NA, DHCP6OptIAPrefix, DHCP6OptIA_PD
from scapy.layers.inet import UDP
from scapy.layers.inet6 import IPv6
from scapy.layers.l2 import Ether

ethernet = Ether(dst='00:0c:29:47:f3:2f',src='c8:3a:35:09:ef:a1',type=0x86dd)
ip = IPv6(src ='2001:db8:3333::16',dst='ff02::2')
udp =UDP(sport=546,dport=547)
# dhcpv6 = DHCP6(msgtype = 1)
dhcpv6 = DHCP6_Solicit()
cid = DHCP6OptClientId()
iana = DHCP6OptIA_NA()
iapd_p = DHCP6OptIAPrefix()
iapd = DHCP6OptIA_PD(iapdopt=[iapd_p])
packet = ethernet/ip/udp/dhcpv6/cid/iana/iapd
packet.show()

