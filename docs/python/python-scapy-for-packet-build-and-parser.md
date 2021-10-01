---
title: Python Scapy 报文构造和解析
date: 2021-02-17 12:12:00
author: hiyo
copyright: true
tags:
	- wireshark
	- tcpdump
	- scapy
	- Python
categories: 
	- [计算机网络]
	- [编程语言,python]
---

Scapy是一款强大的交互式数据包处理工具、数据包生成器、网络扫描器、网络发现、攻击工具和包嗅探工具。能灵活地构造各种数据包、发送数据包、包嗅探、应答和反馈匹配等功能。它可以实现Nmap扫描工具、tcpdump抓包工具 、 tshark工具、Netdiscover网络扫描工具的功能。

Nmap、Netdiscover、tcpdump和tshark介绍可参考：
- Nmap：[Nmap扫描工具介绍](https://blog.csdn.net/u010698107/article/details/115256618)
- tcpdump和tshark：[tcpdump抓包及tshark解包方法介绍](https://blog.csdn.net/u010698107/article/details/112727035)
- Netdiscover：[Netdiscover网络扫描工具](https://blog.csdn.net/u010698107/article/details/115288643)

本文主要介绍Scapy进行报文构造，报文发送和报文解析。
<!--more-->

# 下载安装
官网：[https://scapy.net/](https://scapy.net/)
github地址：[https://github.com/secdev/scapy](https://github.com/secdev/scapy)
官方文档：[https://scapy.readthedocs.io/en/latest/](https://scapy.readthedocs.io/en/latest/)

```python
pip install scapy
```
![png](scapy.png)

# Scapy 的使用
lsc() 命令：列出scapy通用的操作方法，常用的函数包括：
- arpcachepoison（用于arp毒化攻击，也叫arp欺骗攻击）
- arping（用于构造一个ARP的who-has包）
- send：发送3层报文（ 如TCP/UDP 协议），不接收数据包
- sendp：发送2层报文(通过mac地址转发)，不接收
- sniff：用于网络嗅探，类似Wireshark和tcpdump抓包
- sr：发送，接收3层报文，返回有回应的数据包和没有回应的数据包。
- sr1：发送，只接收1个响应包
- srp：发送，接收2层报文
- srp1：发送，只接收1个响应包
- rdpcap：读取报文
- wrpcap：保存报文



```bash
>>> lsc()
arpcachepoison      : Poison target's cache with (your MAC,victim's IP) couple
arping              : Send ARP who-has requests to determine which hosts are up
chexdump            : Build a per byte hexadecimal representation
ls                  : List  available layers, or infos on a given layer class or name.
send                : 
sendp               : 
sendpfast           : Send packets at layer 2 using tcpreplay for performance
sniff               : 
split_layers        : Split 2 layers previously bound.
sr                  : 
sr1                 : 
sr1flood            : Flood and receive packets at layer 3 and return only the first answer
srp                 : 
srp1                : 
```

ls()：查看支持的协议
![png](scapy-ls.png)

ls(IP)：查看IP包的默认参数
![png](scapy-ls-ip.png)


# 报文嗅探
## sniff() 函数参数
Scapy使用 sniff() 函数进行报文嗅探， sniff() 方法有以下参数：
```python
def _run(self,
            count=0, store=True, offline=None,
            quiet=False, prn=None, filter=None, lfilter=None,
            L2socket=None, timeout=None, opened_socket=None,
            stop_filter=None, iface=None, started_callback=None,
            session=None, session_args=[], session_kwargs={},
            *arg, **karg):
```
部分参数定义：
- count：抓包数量，默认为0，表示无限制
- store：是否保存抓取的数据包
- offline：读取 pcap 文件
- quiet：设置为True时，会丢弃stderr进程
- prn：对对每个数据包进行某个操作的函数。例如：prn = lambda x: x.summary()；
- filter：BPF(Berkeley Packet Filter)过滤规则，wireshark过滤也使用的是BPF过滤器。
- timeout：指定嗅探时间
- stop_filter：定义一个函数，在抓到指定数据包后停止抓包
- iface：抓包的接口 

filter参数的BPF语法可参考
1. [https://biot.com/capstats/bpf.html](https://biot.com/capstats/bpf.html) 
2. [https://www.tcpdump.org/manpages/pcap-filter.7.html](https://www.tcpdump.org/manpages/pcap-filter.7.html)

BPF语法示例：
- `dst host 192.168.0.1`：目的IP为192.168.0.1的报文
- `host 192.168.0.1`：IP地址为192.168.0.1的报文
- `tcp port 80`：TCP端口号为80的报文（HTTP报文）
- `tcp and not port 80`：除了80端口的TCP报文
- `tcp portrange 1-25`：TCP端口范围1-25的报文
- `not broadcast`：排除广播报文
- `!arp`：排除arp报文

## sniff() 抓包
```python
from scapy.all import *

package = sniff(iface='WLAN', timeout=10)
wrpcap("test.pcap", package)  # 将抓取的包保存为test.pcap文件
```

查看保存的报文：
```python
>>> pkts = sniff(offline='test.pcap')
>>> pkts[17].show()
###[ Ethernet ]###
  dst= ff:ff:ff:ff:ff:ff
  src= fc:4d:d4:f8:84:f8
  type= ARP
###[ ARP ]###
     hwtype= 0x1
     ptype= IPv4
     hwlen= 6
     plen= 4
     op= who-has
     hwsrc= fc:4d:d4:f8:84:f8
     psrc= 192.168.101.156
     hwdst= 00:00:00:00:00:00
     pdst= 192.168.101.1
###[ Padding ]###
        load= '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

```

过滤报文：
```python
>>> sniff(iface='WLAN', timeout=10, filter="tcp port 80", prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%}"))
183.232.231.174 -> 192.168.0.167
192.168.0.167 -> 183.232.231.174
<Sniffed: TCP:2 UDP:0 ICMP:0 Other:0>
```

除了使用scapy抓包外，也可以使用tcpdump（Linux）和tshark（Windows）进行抓包。

# DHCPv6报文构造
我们首先用Scapy打开一个真实抓到的DHCPv6 Request报文，查看一下报文结构：
```python
from scapy.all import *
pkts = rdpcap('packet.pcap')
pkts[1021].show() # 序号为1022的报文为DHCPv6 Request报文（通过wireshark查看）
```
报文打印如下：
![png](scapy-dhcpv6-1.png)
![png](scapy-dhcpv6-2.png)


下面开始构造每一层报文：
```python
from scapy.all import *
ethernet = Ether(dst='00:0c:29:47:f3:2f',src='c8:3a:35:09:ef:a1',type=0x86dd)
ip = IPv6(src ='2001:db8:3333::16',dst='ff02::2')
udp =UDP(sport=546,dport=547)
# dhcpv6 = DHCP6(msgtype = 1)
dhcpv6 = DHCP6_Solicit()
cid = DHCP6OptClientId()
iana = DHCP6OptIA_NA()
iapd_p = DHCP6OptIAPrefix()
iapd = DHCP6OptIA_PD(iapdopt=[iapd_p])
packet = ethernet/ip/udp/dhcpv6/cid/iana/iapd
packet.show()
```
注意DHCP6 Option - IA Prefix option 的构造方法， IA Prefix选项是包含在IAPD选项内的，所以要赋值给iapdopt，多个option字段用逗号隔开。

其中，字段名称通过 `ls()` 命令查看：
```python
ls(DHCP6OptIA_PD)
ls(DHCP6OptIA_NA)
```
![png](scapy-ls-opts.png)

运行上面程序，打印构造的报文：
![png](scapy-packet.png)
构造成功！

# 发送报文
## 1. 只发不收
- send：发送3层报文（ 如TCP/UDP 协议），不接收数据包
- sendp：发送2层报文(通过mac地址转发)，不接收
```python
send(packet, iface='eth1', count=2) 
sendp(packet, iface='eth0')
```
count，发送报文数，默认发送一个报文
iface，指定接口

## 2. 发且收
- sr：发送，接收3层报文，返回有回应的数据包和没有回应的数据包。
- sr1：发送，只接收1个响应包
- srp：发送，接收2层报文
- srloop()：循环发送
- srp1：发送，只接收1个响应包
- srploop：循环发送
```python
sr(packet, iface='eth1')
```

# 报文过滤
在网络协议的测试中，我们需要检测某个报文字段是否存在，对抓取到的报文进行解析，可以使用tshark命令解析报文解析(参考文章[tcpdump抓包及tshark解包方法介绍](https://blog.csdn.net/u010698107/article/details/112727035))。

当然，Scapy也可以解析数据包，下面查找DHCPv6 Solicit报文，且目的MAC为00:0c:29:d9:98:c7
```python
from scapy.all import *
import re

package = "package.pcap"
field = 'dst=00:0c:29:d9:98:c7'
pkts = rdpcap(package)
for packet in pkts:    
    if packet.haslayer('DHCP6_Solicit'):        
        packet_text = repr(packet)        
        if re.search(field, packet_text, re.IGNORECASE):
            print("666")
```
其中，repr内置函数用于返回对象的 string 格式。除了rdpcap()方法读取报文文件外，也可以使用嗅探函数sniff()：
```python
pkts = sniff(offline='packet_solicit.pcap')
```

如果不知道目标字段写法，可以先打印一下：
```sh
>>> from scapy.all import *
>>> pkts = rdpcap('packet_solicit.pcap')
>>> pkts[3]
<Ether  dst=ff:ff:ff:ff:ff:ff src=00:0c:29:d9:98:c7 type=IPv6 |<IPv6  version=6 tc=0 fl=0 plen=46 nh=UDP hlim=64 src=fe80::20c:29ff:fed9:98c7 dst=ff02::1:2 |<UDP  sport=dhcpv6_client dport=dhcpv6_server len=46 chksum=0x764d |<DHCP6_Solicit  msgtype=SOLICIT trid=0x0 |<DHCP6OptClientId  optcode=CLIENTID optlen=14 duid=<DUID_LLT  type=Link-layer address plus time hwtype=Ethernet (10Mb) timeval=Sat, 01 Jan 2000 00:00:00 +0000 (946684800) lladdr=00:0c:29:d9:98:c7 |> |<DHCP6OptIA_NA  optcode=IA_NA optlen=12 iaid=0x0 T1=0 T2=0 |>>>>>>
```

<center><b>--THE END--<b></center>