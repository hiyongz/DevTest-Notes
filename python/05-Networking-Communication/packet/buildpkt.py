#!/usr/bin/python3
#coding=utf-8

import os,sys
import datetime
import time
import getopt
import re
from scapy.all import *

class ArgParser():
    def usage(self):
        Usage = """
        Usage: python /var/tendatest/TDT/script/buildpkt.py [OPTION...]\n \n \
        Options:\n \
        -P, --Protocol \t-- IPv6协议名称\n \
        -p, --package \t\t-- 报文文件，默认/tmp/packet.pcap
        -m, --message \t\t-- 报文类型\n \
        -l, --layer \t\t-- 报文层名称\n \
        -o, --option \t\t-- 报文选项options\n \
        -I, --iface \t\t-- 报文发送接口\n \
        -c, --count \t\t-- 发送报文数，默认发送一个报文\n \
        -h, --help \t\t-- 帮助信息\n \n\
        eg: \
            -P dhcpv6 -m solicit  -I eth1 -l ether,dst='33:33:00:01:00:02',src="00:0c:29:d9:98:c7" -l ipv6,src='fe80::20c:29ff:fed9:98c7',dst='ff02::1:2' 构建DHCPv6 Solicit报文，从eth1接口发出
        """
        print(Usage)

    def arg_parser(self):
        try:
            opts,args = getopt.getopt(sys.argv[1:],"P:p:m:l:o:I:c:h",["Protocol=","package=","message=","layer=","option=","help"])
        except getopt.GetoptError as e:
            print(e)
            self.usage()
            sys.exit()
        print(sys.argv[0] + ' '+ ' '.join(sys.argv[1:]))
        for op,value in opts:  
            if op in ("-P","--Protocol"):
                self.protocol = value.lower()

            elif op in ("-m","--message"):
                self.message_type=value.lower()

            elif op in ("-p","--package"):
                self.package=value

            elif op in ("-l","--layer"):        
                values = value.split(",", 1)               
                if len(values) == 1:
                    self.layer[values[0]] = '1'
                else:
                    if self.layer.setdefault(values[0]):
                        self.layer[values[0]] = self.layer.setdefault(values[0],'') +',' + values[1]
                    else:  
                        self.layer[values[0]] = values[1]

            elif op in ("-o","--option"):
                values = value.split(",", 1)
                if len(values) == 1:
                    self.option[values[0]] = '1'
                else:
                    if self.option.setdefault(values[0]):
                        self.option[values[0]] = self.option.setdefault(values[0],'') +',' + values[1]
                    else:  
                        self.option[values[0]] = values[1]     

            elif op in ("-I","--iface"):
                self.iface = value.strip("'")

            elif op in ("-c","--count"):
                self.count = int(value)

            elif op in ('-h','--help'):
                self.usage()
                sys.exit()

        if self.protocol == '' or self.message_type == '':
            print("Error: 请输入协议类型和报文类型！")
            self.usage()
            sys.exit()

class LayerOptionBuild(ArgParser):
    """build/edit layer or options
    1、创建每一层
    2、创建Options选项
    """
    def layer_ethernet(self, flag=0, ethernet=''):
        ############# Ethernet II #############
        # flag=0 表示需要重新创建, flag=1，表示修改字段，注意如果要修改需要输入ethernet

        Ethernet_field = self.layer.setdefault('ether')
        if flag == 0:
            ethernet = Ether(type=0x86dd)
        if Ethernet_field: 
            ethernet = self.packet_build(ethernet, Ethernet_field)
        
        # ethernet.show()
        return ethernet

    def layer_ip(self, flag=0, ip=''):
        ############# IPv6 #############
        IPv6_field = self.layer.setdefault('ipv6')
        if flag == 0:
            ip = IPv6()
        if IPv6_field: 
            ip = self.packet_build(ip, IPv6_field)
        # ip.show()
        return ip

    def layer_udp(self, flag=0, udp=''):
        ############# UDP #############
        udp_field = self.layer.setdefault('udp')
        if flag == 0:
            udp = UDP(sport=546, dport=547)
        if udp_field: 
            udp = self.packet_build(udp, udp_field)
        # udp.show()
        return udp

    def layer_dhcpv6(self, flag=0, dhcpv6=''):
        ############# DHCP6 #############
        message_type = self.protocol + '_' + self.message_type
        try:
            dhcp6 = self.ipv6_message.setdefault(message_type)
            # print(f'dhcp6：{dhcp6}')
            if flag == 0:
                dhcpv6 = eval(dhcp6)()
        except:
            print("Error: 没有%s报文，请输入正确的报文类型"%message_type)
            self.usage()
            sys.exit()
        # dhcpv6.show()
        dhcpv6_field = self.layer.setdefault('dhcpv6')
        if dhcpv6_field:
            dhcpv6 = self.packet_build(dhcpv6, dhcpv6_field)
        
        return dhcpv6
    
    def layer_icmpv6(self, flag=0, icmpv6=''):
        ############# ICMPv6 #############
        message_type = self.protocol + '_' + self.message_type
        try:
            icmpv6 = self.ipv6_message.setdefault(message_type)
            # print(f'dhcp6：{dhcp6}')
            if flag == 0:
                icmpv6 = eval(icmpv6)()
        except:
            print("Error: 没有%s报文，请输入正确的报文类型"%message_type)
            self.usage()
            sys.exit()
        # dhcpv6.show()
        icmpv6_field = self.layer.setdefault('icmpv6')
        if icmpv6_field:
            icmpv6 = self.packet_build(icmpv6, icmpv6_field)
        
        return icmpv6


    def option_cid(self,ethernet, flag=0, cid='', duid=''):
        ############# DHCP6OptClientId  #############
        # DHCP6 Client Identifier Option  
        
        # DUID类型
        duid_type = ''
        try:
            for key, val in self.option.items():            
                if re.match('DUID',key, re.IGNORECASE):
                    duid_type = key
        except:
            pass
        if duid_type == '':
            duid_type = 'duid_llt'
        
        DUID = self.ipv6_message.setdefault(duid_type)
        if flag == 0:
            duid = eval(DUID)()            
        duid_field = self.option.setdefault('duid_type')
        if duid_field: 
            duid = self.packet_build(duid, duid_field)        

        # ClientId
        cid_field = self.option.setdefault('clientid')
        if cid_field: 
            duid = self.packet_build(duid, cid_field)

        if flag == 0:
            cid = DHCP6OptClientId(duid=duid)
        if cid_field and flag:
            cid.duid = duid
        # cid.show()
        return cid

    def option_sid(self, flag=0, sid='', duid_llt=''):
        ############# DHCP6OptServerId  #############
        # DHCP6 Server Identifier Option
        if sid != '':
            duid_llt = sid[DHCP6OptServerId][DUID_LLT]

        sid_field = self.option.setdefault('serverid')
        if flag == 0:
            duid_llt = DUID_LLT()

        if sid_field: 
            duid_llt = self.packet_build(duid_llt, sid_field)
        
        if flag == 0:
            sid = DHCP6OptServerId(duid=duid_llt)
        if sid_field and flag:
            sid.duid = duid_llt
        # cid.show()
        return sid

    def option_iana(self, flag=0, sid=''):
        ############# DHCP6OptIA_NA  #############
        #  DHCP6 Identity Association for Non-temporary Addresses Option
        if sid != '':
            iana = sid[DHCP6OptIA_NA]
        iana_field = self.option.setdefault('ia_na')
        if flag == 0:
            iana = DHCP6OptIA_NA()
        if iana_field: 
            iana = self.packet_build(iana, iana_field)
        
        if sid != '':
            sid[DHCP6OptIA_NA] = iana
            return sid
        else:
            return iana

    def option_iaaddr(self, flag=0, sid='', iana=''):
        ############# IA Address option ##############
        if sid != '':
            iana = sid[DHCP6OptIA_NA]
            ia_addr = sid[DHCP6OptIA_NA][DHCP6OptIAAddress]

        ia_addr_field = self.option.setdefault('iaaddress')
        if ia_addr_field: 
            if flag == 0:
                ia_addr = DHCP6OptIAAddress()
            ia_addr = self.packet_build(ia_addr, ia_addr_field)
            iana.ianaopts=ia_addr
        
        if sid != '':
            sid[DHCP6OptIA_NA].ianaopts=ia_addr
            return sid
        else:
            return iana

    def option_dns(self, flag=0, sid='',dns=''):
        ############# DHCP6OptDNSServers  #############
        #  DHCP6 Option - DNS Recursive Name Server
        if sid != '':
            dns = sid[DHCP6OptDNSServers]
        dns_field = self.option.setdefault('dns')       
        if dns_field: 
            if flag == 0:
                dns = DHCP6OptDNSServers()
            dns = self.packet_build(dns, dns_field)

        if sid != '':
            sid[DHCP6OptDNSServers] = dns
            return sid
        else:
            return dns

    def option_optreq(self, flag=0, optreq=''):
        ############# DHCP6OptOptReq #############
        # DHCP6 Option Request Option
        optreq_field = self.option.setdefault('optreq')       
        if optreq_field: 
            if flag == 0:
                optreq = DHCP6OptOptReq()
            optreq = self.packet_build(optreq, optreq_field)

        return optreq
    def option_rapidcommit(self, flag=0, rapidcommit=''):
            ############# DHCP6OptRapidCommit #############
            #  DHCP6 Rapid Commit Option
            rapidcommit_field = self.option.setdefault('rapidcommit')       
            if rapidcommit_field: 
                if flag == 0:
                    rapidcommit = DHCP6OptRapidCommit()
                rapidcommit = self.packet_build(rapidcommit,rapidcommit_field)

            return rapidcommit


    def option_lla(self, flag=0, lla=''):
        ############# ICMPv6NDOptLLA #############
        # ICMPv6 Neighbor Discovery - Link-Layer Address (LLA) Option (FH for MIPv6)
        lla_field = self.option.setdefault('lla')       
        if lla_field: 
            if flag == 0:
                lla = ICMPv6NDOptLLA()
            lla = self.packet_build(lla, lla_field)

        return lla


class PktBuild(LayerOptionBuild):
    """创建报文
    构建、组合报文
    发送报文
    """
    def __init__(self):
        self.protocol = ''
        self.message_type = ''
        self.layer = dict()
        self.option = dict()
        self.iface = 'eth1'
        self.count = 1
        self.package = '/tmp/packet.pcap'
        self.message = ['ethernet','ip','udp','dhcpv6','icmpv6','cid','sid','iana','dns','optreq','rapidcommit','lla']
        self.ipv6_message = {'dhcpv6_solicit': 'DHCP6_Solicit','dhcpv6_request': 'DHCP6_Request',\
            'dhcpv6_reply': 'DHCP6_Reply','dhcpv6_renew': 'DHCP6_Renew','dhcpv6_release': 'DHCP6_Release',\
            'dhcpv6_relayreply': 'DHCP6_RelayReply','dhcpv6_relayforward': 'DHCP6_RelayForward','dhcpv6_reconf': 'DHCP6_Reconf',\
            'dhcpv6_rebind': 'DHCP6_Rebind','dhcpv6_inforequest': 'DHCP6_InfoRequest','dhcpv6_decline': 'DHCP6_Decline',\
            'dhcpv6_confirm': 'DHCP6_Confirm','dhcpv6_advertise': 'DHCP6_Advertise',\
            'duid_en': 'DUID_EN','duid_ll': 'DUID_LL','duid_llt':'DUID_LLT',\
            'icmpv6_nd_na':'ICMPv6ND_NA','icmpv6_nd_ns':'ICMPv6ND_NS','icmpv6_nd_ra':'ICMPv6ND_RA','icmpv6_nd_rs':'ICMPv6ND_RS'}
 
    def packet_build(self,layer,packet_field):
        # 构建报文字段、options
        if packet_field != '1':
            fields = dict(((lambda a:(a[0].strip("'"),a[1].strip("'"))) (field.split('=')) for field in packet_field.split(',')))
            for key, val in fields.items():
                # 如果value全为数字，转换为int型
                if re.match('^[0-9]*$',val):
                    val = int(val)
                setattr(layer, key, val)
        return layer


    def dhcpv6_packet_edit(self, sid):
        """
        dhcpv6报文编辑
        """
        if self.option.setdefault('duid_llt'):            
            if sid[DHCP6OptServerId].haslayer("DUID_LLT"):                                
                sid = self.option_sid(1, sid, sid[DHCP6OptServerId][DUID_LLT])
            else:
                self.option_sid(0, sid[DHCP6OptServerId])
                sid = self.option_sid()

        if self.option.setdefault('ia_na'):            
            if sid.haslayer("DHCP6OptIA_NA"):                                
                sid = self.option_iana(1,sid)
            else:
                iana = self.option_iana()
                sid = sid/iana
        if self.option.setdefault('iaaddress'):
            if sid[DHCP6OptIA_NA].haslayer("DHCP6OptIAAddress"):                          
                sid = self.option_iaaddr(1,sid)
            else:
                iana = self.option_iaaddr(0, sid='',iana=iana)
                sid = sid/iana
        
        if self.option.setdefault('dns'):            
            if sid.haslayer("DHCP6OptDNSServers"):                                
                sid = self.option_dns(1,sid)
            else:
                dns = self.option_dns()
                sid = sid/dns
        try:
            del iana
        except:
            pass

        return sid

    def create_dhcpv6(self):
        # 创建dhcpv6报文
        ethernet = self.layer_ethernet()            
        ip = self.layer_ip()
        udp = self.layer_udp()
        dhcpv6 = self.layer_dhcpv6()
        cid = self.option_cid(ethernet)
        iana = self.option_iana()
        iana = self.option_iaaddr(flag=0, iana=iana)
        dns = self.option_dns()
        optreq = self.option_optreq()
        rapidcommit = self.option_rapidcommit()

        if self.message_type == 'request':
            # DHCPv6 Request请求需要服务器返回的Advertise报文（solicit报文的回应报文）
            # pkts = rdpcap(self.package)
            pkts = sniff(offline=self.package)
            for packet in pkts:
                if packet.haslayer("DHCP6_Advertise"):
                    sid = packet.getlayer(DHCP6OptServerId)
                    sid = self.dhcpv6_packet_edit(sid)
        if self.message_type == 'renew':
            pkts = sniff(offline=self.package)
            for packet in pkts:
                if packet.haslayer("DHCP6_Advertise"):                        
                    sid = packet.getlayer(DHCP6OptServerId)
                    sid = self.dhcpv6_packet_edit(sid)
                    try:
                        del iana
                    except:
                        pass
        
        if self.message_type == 'release':
            pkts = sniff(offline=self.package)
            for packet in pkts:
                if packet.haslayer("DHCP6_Advertise"):
                    sid = packet.getlayer(DHCP6OptServerId)
                    sid = self.dhcpv6_packet_edit(sid)

        if self.message_type == 'decline':
            pkts = sniff(offline=self.package)
            for packet in pkts:
                if packet.haslayer("DHCP6_Advertise"):
                    sid = packet.getlayer(DHCP6OptServerId)
                    sid = self.dhcpv6_packet_edit(sid)
            
            iana_field = self.option.setdefault('ia_na')
            if iana_field:
                iana = self.packet_build(iana, iana_field)
                iana = self.option_iaaddr(flag=0, iana=iana)

        if self.message_type == 'rebind':
            pkts = sniff(offline=self.package)
            for packet in pkts:
                if packet.haslayer("DHCP6_Advertise"):
                    sid = packet.getlayer(DHCP6OptServerId)  
                    if self.option.setdefault('ia_na'):            
                        if sid.haslayer("DHCP6OptIA_NA"):                                
                            sid = self.option_iana(1,sid)
                        else:
                            iana = self.option_iana()
                            sid = sid/iana   
                    try:
                        del iana
                    except:
                        pass
        if self.message_type == 'inforequest':                
            try:
                del iana
            except:
                pass            
        if self.message_type == 'reconf':
            try:
                del cid
            except:
                pass
            pkts = sniff(offline=self.package)
            for packet in pkts:
                if packet.haslayer("DHCP6OptIA_NA"):
                    sid = packet.getlayer(DHCP6OptIA_NA)
                    sid = self.dhcpv6_packet_edit(sid)


        ##### Stacking layers #####
        
        # check layer
        message = self.message
        del_message = []
        for layer_i, value in enumerate(message):             
            if message[layer_i] not in locals().keys() or eval(message[layer_i]) == '' or eval(message[layer_i]) is None:
                del_message.append(value)
        for m in del_message:
            message.remove(m)
                
        # 组合报文
        layers = "/".join(message)
        print(layers)
        packet = eval(layers)
        packet.show()
        return packet

    def create_icmpv6(self):
        # 创建icmpv6报文
        ethernet = self.layer_ethernet()
        ip = self.layer_ip()
        icmpv6 = self.layer_icmpv6()       
        lla = self.option_lla()

        if self.message_type == 'request':
            # DHCPv6 Request请求需要服务器返回的Advertise报文（solicit报文的回应报文）
            pkts = sniff(offline=self.package)
            for packet in pkts:
                if packet.haslayer("DHCP6_Advertise"):
                    sid = packet.getlayer(DHCP6OptServerId)
                    sid = self.dhcpv6_packet_edit(sid)
        
        if self.message_type == 'renew':
            pkts = sniff(offline=self.package)
            for packet in pkts:
                if packet.haslayer("DHCP6_Advertise"):                        
                    sid = packet.getlayer(DHCP6OptServerId)
                    sid = self.dhcpv6_packet_edit(sid)
                    try:
                        del iana
                    except:
                        pass
        
        if self.message_type == 'release':
            pkts = sniff(offline=self.package)
            for packet in pkts:
                if packet.haslayer("DHCP6_Advertise"):
                    sid = packet.getlayer(DHCP6OptServerId)
                    sid = self.dhcpv6_packet_edit(sid)

        if self.message_type == 'decline':
            pkts = sniff(offline=self.package)
            for packet in pkts:
                if packet.haslayer("DHCP6_Advertise"):
                    sid = packet.getlayer(DHCP6OptServerId)
                    sid = self.dhcpv6_packet_edit(sid)
            
            iana_field = self.option.setdefault('ia_na')
            if iana_field:
                iana = self.packet_build(iana, iana_field)
                iana = self.option_iaaddr(flag=0, iana=iana)

        if self.message_type == 'rebind':
            pkts = sniff(offline=self.package)
            for packet in pkts:
                if packet.haslayer("DHCP6_Advertise"):
                    sid = packet.getlayer(DHCP6OptServerId)  
                    if self.option.setdefault('ia_na'):            
                        if sid.haslayer("DHCP6OptIA_NA"):                                
                            sid = self.option_iana(1,sid)
                        else:
                            iana = self.option_iana()
                            sid = sid/iana   
                    try:
                        del iana
                    except:
                        pass
        if self.message_type == 'inforequest':                
            try:
                del iana
            except:
                pass

        ##### Stacking layers #####
        
        # check layer
        message = self.message
        del_message = []
        for layer_i, value in enumerate(message):             
            if message[layer_i] not in locals().keys() or eval(message[layer_i]) == '' or eval(message[layer_i]) is None:
                del_message.append(value)
        for m in del_message:
            message.remove(m)
                
        # 组合报文
        layers = "/".join(message)
        print(layers)
        packet = eval(layers)
        packet.show()
        return packet

    def create_pkt(self):
        # 创建报文
        if self.protocol == 'dhcpv6':
            packet = self.create_dhcpv6()
        if self.protocol == 'icmpv6':
            packet = self.create_icmpv6()
        
        return packet

    def send_pkt(self, packet): 
        # 发送报文       
        sendp(packet, iface=self.iface, count=self.count)

if __name__ == "__main__":
    pkt = PktBuild()
    pkt.arg_parser()
    packet = pkt.create_pkt()
    pkt.send_pkt(packet)
    

