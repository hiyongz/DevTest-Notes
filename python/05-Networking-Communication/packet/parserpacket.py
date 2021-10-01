#!/usr/bin/python3
#coding=utf-8

import os,sys
import datetime
import time
import getopt
import re
from collections import Counter
from subprocess import Popen ,PIPE
from scapy.all import *
import copy

class ArgParser():
    # 预处理输入参数
    def usage(self):
        Usage = """
        Usage: python /var/tendatest/TDT/script/parserpacket.py [OPTION...]\n \n \
        Options:\n \
        -P, --Protocol \t-- 协议名称，eg:DHCPv6、ICMPv6\n \
        -p, --package \t\t-- 报文文件，default: /tmp/packet.pcap\n \
        -m, --message \t\t-- 报文类型\n \
        -F, --field \t\t-- 报文字段，多个条件使用","分隔，用于scapy方法解包\n \
        -f, --filter \t\t-- 报文字段过滤，多个条件使用","分隔\n \
        -Y, --display-filter \t-- 报文过滤条件，只处理符合条件的报文，多个条件使用","分隔\n \
        -c, --count \t\t-- 预期匹配数，default: 1\n \
        -r, --return_flag \t\t-- 是否返回字段值，default: 0\n \
        -h, --help \t\t-- 帮助信息\n \n\
        eg: \n\
            1. -P dhcpv6 -m solicit -F dst='ff02::1:2' 查找目的MAC地址为ff02::1:2的DHCPv6_Solicit报文\n\
            2. -f ipv6.dst=ff02::1:2 -Y dhcpv6.msgtype==1 查找目的MAC地址为ff02::1:2的DHCPv6_Solicit报文\n\
            3. -f ipv6.dst=ff02::1:2 查找目的MAC地址为ff02::1:2的报文
        """
        print(Usage)

    def arg_parser(self):
        try:
            opts,args = getopt.getopt(sys.argv[1:],"P:p:F:f:Y:m:c:r:h",["Protocol=","package=","field=","filter=","display-filter=","message=","count=","return_flag=","help"])
        except getopt.GetoptError as e:
            print(e)
            self.usage()
            sys.exit()        
        print(sys.argv[0] + ' '+ ' '.join(sys.argv[1:]))

        for op, value in opts:  
            if op in ("-P", "--Protocol"):
                self.protocol = value.lower()

            elif op in ("-m","--message"):
                self.message_type = value.lower()

            elif op in ("-p","--package"):
                self.package = value.lower()

            elif op in ("-f","--filter"):                
                self.filters = value
            
            elif op in ("-F","--field"):
                self.fields = [field.replace("'", '') for field in value.split(',')]  
            
            elif op in ("-Y","--display-filter"):
                self.display_filter = [field.replace("'", '') for field in value.split(',')]

            elif op in ("-c","--count"):
                self.count = int(value)

            elif op in ("-r","--return_flag"):
                self.return_flag = int(value)

            elif op in ('-h','--help'):
                self.usage()
                sys.exit()


class ParserPacketMethod():
    def arg_display_filter(self):
        """
        处理display-filter参数
        """
        ######  1、处理报文过滤条件，对应tshark命令的-Y参数 ###### 
        display_field = '' 
        display_filt = ''       
        if self.display_filter != '':
            display_filt = copy.copy(self.display_filter) # 浅拷贝
            # print("display_filt:", display_filt)
            for filter_i, value in enumerate(self.display_filter):
                if "==" not in value:
                    print("\tError: 请使用'=='符号连接字段和value值")
                    self.usage()
                    sys.exit() 
                self.display_filter[filter_i]  = value
            display_field = " ".join(self.display_filter)
        # 将多个过滤条件用and连接起来，如果不用and连接，只有最后一个过滤条件生效
        display_field = " and ".join(self.display_filter)
        display_field = '-Y "%s"'%display_field
        return display_field,display_filt
    
    def parser_time_epoch(self):
        """
        读取报文时间戳
        """
        display_field, display_filt = self.arg_display_filter()
        cmd = ["tshark -r %s -T fields -e frame.time_epoch" %(self.package)] # 过滤结果使用缩进分隔
        cmd.append(display_field)
        print("cmd:"," ".join(cmd))
        display_ret = 0
        if display_field != '':
            display_result = os.popen(" ".join(cmd))
            display_ret = display_result.read()
        if display_ret == '':
            print(u"没有匹配到%s"%(','.join(display_filt)))
            if self.count == 0:
                print("PASS")
            else:
                print("FAIL")
            return
        else:            
            for element in display_ret.split("\n")[:-1]:
                print("EPOCH-TIME:%s"%element)

    def parser_tshark_packet(self):     
        display_field,display_filt = self.arg_display_filter()
        ###### 2、处理字段过滤条件 ：分别提取字段field和对应的值value，对应tshark命令的-e参数 ###### 
        filter_list = self.filters.split(",")        
        field_list = []
        value_list = []
        value = ''
        for filt in filter_list:
            if "==" in filt:
                separator = "=="
            else:
                separator = "="
            fields = filt.split(separator, 1)
            # print("fields:",fields)
            value = ''
            try:
                field = fields[0]
                value = fields[1]
            except:                
                pass
            field_list.append(field)
            value_list.append(value)

            # 处理需要返回报文字段值的情况：这种情况下，过滤条件为需要查找的字段，且只允许一个条件，也就是一次仅允许查一个字段
            # 另外，为了更精确的查找到目标报文的字段值，需要使用多个过滤条件（-Y参数），只查找指定报文。
            if self.return_flag == 1 and len(field_list) > 1:
                print(u"仅允许查找一个字段~")
                sys.exit()

        # print("field_list:",field_list)
        # print("value_list:",value_list)

        ###### 3、tshark命令报文过滤 ######
        # tshark命令解析数据包是否包含字段
        cmd = ["tshark -r %s -E separator=/t" %(self.package)] # 过滤结果使用缩进分隔
        cmd.append(display_field)
        # print("cmd:", " ".join(cmd)+" " + " ".join(field_list))
        display_ret = 0
        if display_field != '':
            display_result = os.popen(" ".join(cmd))
            display_ret = display_result.read()
        if display_ret == '':
            print(u"没有匹配到%s"%(','.join(display_filt)))
            if self.count == 0:
                print("PASS")
            else:
                print("FAIL")
            return
        else:
            location = []
            sumlocation = []
            cmd = ["tshark -r %s -T fields -E separator=/t" %(self.package)] 
            cmd.append(display_field)

            for index, field in enumerate(field_list):            
                cmd.append("-e %s" %(field))
                result = os.popen(" ".join(cmd))
                ret = result.read()
                print("cmd:", " ".join(cmd))
                # 解析tshark过滤结果
                fieldvalue = []
                for i, element in enumerate(ret.split("\n")):
                    values = element.split('\t')
                    values2 = element.split(',')
                    if element == '\t' or element == '':
                        continue
                    if self.return_flag == 1:
                        fieldvalue = element
                    # print("FieldValue:", element)
                    if value_list[index] == '':
                        if values != '':
                            location.append(i)                
                    else:
                        if value_list[index] in values:
                            location.append(i)
                        elif value_list[index] in values2:
                            location.append(i)
                if self.return_flag == 1:
                    print("FieldValue:", fieldvalue)
                sumlocation.append(location)
                # print("sumlocation:",sumlocation)
                location = []
                cmd = ["tshark -r %s -T fields -E separator=/t" %(self.package)]
                cmd.append(display_field)
        
        ###### 4、统计过滤结果 ###### 
        for group_i, message_num in enumerate(sumlocation):
            if len(message_num) == 0:
                print(u"字段 %s 没有匹配"%filter_list[group_i])         
            else:
                print(u"字段 %s 匹配成功%d次"%(filter_list[group_i],len(message_num)))

        # 统计所有条件都满足的报文数
        sums = 0
        try:
            intersect_location = list(reduce(lambda x,y : set(x) & set(y), sumlocation))
            sums = len(intersect_location)
            print(u"所有字段匹配成功%s次"%sums)
        except:
            print(u"没有匹配到任何字段")
            pass
        
        if self.count <= sums and sums != 0 and self.count != 0:
            print("PASS")
        elif self.count == 0 and self.count == sums:
            print("PASS")
        else:
            print("FAIL")

    def parser_scapy_packet(self):
        """scapy解包
        在指定报文内检查字段
        """
        # pkts = rdpcap(self.package)
        pkts = sniff(offline=self.package)
        # pkts = rdpcap('d:/packet-solicit.pcap')
        message_counter = 0        
        field_counter = {} 
        location = []
        sumlocation = []      
        message = self.protocol + '_' + self.message_type
        message_type = self.ipv6_message.setdefault(message)
        pkt_ind = 0
        for packet in pkts:
            pkt_ind += 1
            
            if packet.haslayer(message_type):
                message_counter += 1
                packet_text = repr(packet)
                if self.fields != '':
                    packet_text = repr(packet)
                    for field_i in range(len(self.fields)):
                        field = self.fields[field_i]
                        if re.search(field, packet_text, re.IGNORECASE):                            
                            field_counter.setdefault(field_i,[]).append(pkt_ind)
                        else:
                            field_counter.setdefault(field_i,[])
                
        print(u"%s 报文匹配%s次"%(message,message_counter))

        for field_i, counters in field_counter.items():           
            sumlocation.append(counters)
            if len(counters) == 0:
                print(u"字段 %s 没有匹配"%self.fields[field_i])         
            else:
                print(u"字段 %s 匹配成功%d次"%(self.fields[field_i],len(counters)))

        # 统计所有字段匹配次数（都满足过滤条件的报文）
        sums = 0
        try:
            intersect_location = list(reduce(lambda x,y : set(x) & set(y), sumlocation))
            sums = len(intersect_location)
            print(u"所有字段匹配成功%s次"%sums)
        except:
            print(u"没有匹配到任何字段")
            pass
        if self.count <= sums and sums != 0 and self.count != 0:
            print("PASS")
        elif self.count == 0 and self.count == sums:
            print("PASS")
        else:
            print("FAIL")


class ParserPacket(ArgParser,ParserPacketMethod):
    def __init__(self):
        self.protocol = ''
        self.message_type = ''
        self.filters = ''
        self.display_filter = ''
        self.return_flag = 0
        self.fields = ''
        self.count = 1
        self.package = '/tmp/packet.pcap'
        self.message = ['ethernet','ip','udp','dhcpv6','cid','sid','iana','dns']
        self.ipv6_message = {'dhcpv6_solicit': 'DHCP6_Solicit','dhcpv6_request': 'DHCP6_Request',\
            'dhcpv6_reply': 'DHCP6_Reply','dhcpv6_renew': 'DHCP6_Renew','dhcpv6_release': 'DHCP6_Release',\
            'dhcpv6_relayreply': 'DHCP6_RelayReply','dhcpv6_relayforward': 'DHCP6_RelayForward','dhcpv6_reconf': 'DHCP6_Reconf',\
            'dhcpv6_rebind': 'DHCP6_Rebind','dhcpv6_inforequest': 'DHCP6_InfoRequest','dhcpv6_decline': 'DHCP6_Decline',\
            'dhcpv6_confirm': 'DHCP6_Confirm','dhcpv6_advertise': 'DHCP6_Advertise'}   

    def parser_packet(self):
        # 解析数据包，两种方法：
        # 1、tshark解包：过滤规则可以通过wireshark获取
        # 2、scapy工具解包：用于查找某指定协议报文字段
        # print("self.filters:",self.filters)
        # 判断报文文件是否存在
        if not os.path.isfile(self.package):
            print("文件 %s 不存在, 请检查-p参数是否正确"%self.package)
            print("FAIL")
            sys.exit()
            
        if self.filters != '' and self.filters != 'frame.time_epoch':
            # 方法1
            self.parser_tshark_packet()
        elif self.filters == 'frame.time_epoch':
            self.parser_time_epoch()
        else:
            if self.protocol == '' or self.message_type == '':
                print("\tError: 1、请输入协议类型和报文类型。2、或者输入过滤条件：-f 参数")
                self.usage()
                sys.exit()
            # 方法2
            self.parser_scapy_packet()

if __name__ == "__main__":
    pkt = ParserPacket()
    pkt.arg_parser()
    pkt.parser_packet()

    

