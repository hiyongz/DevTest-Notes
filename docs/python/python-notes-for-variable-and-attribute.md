---
title: Python笔记：属性值设置和判断变量是否存在
date: 2021-02-16 12:22:00
author: hiyo
copyright: true
tags:
	- setattr
	- Python
categories: 
	- [编程语言,python]
---

介绍Python设置属性值方法setattr()和判断变量是否存在的方法
<!--more-->

# 以属性名为变量的方式给一个对象添加属性
使用 setattr 方法
```python
obj = SomeClass()
key = 'key_name'
val = 'key_value'
setattr(obj, key, val)
print(obj.key_name) 
```
示例：给报文字段赋值
```python
from scapy.all import *
layer = {"ether":"dst='33:33:00:01:00:02',src='00:0c:29:d9:98:c7'"}
Ethernet_field = layer.setdefault('ether')
ethernet = Ether(type=0x86dd)
fields = dict(((lambda a:(a[0].strip("'"),a[1].strip("'"))) (field.split('=')) for field in Ethernet_field.split(',')))
for key, val in fields.items():
    setattr(ethernet, key, val) 
ethernet.show()
```
out:
```python
>>> ethernet.show()
###[ Ethernet ]###
  dst       = 33:33:00:01:00:02
  src       = 00:0c:29:d9:98:c7
  type      = IPv6
```

# 判断变量是否存在
三种方法：
* locals().keys()
* dir()
* vars()

```python
ethernet = 'Ether'
dhcpv6 = 'dhcpv6_solicit'
message = ['ethernet','ip','udp','dhcpv6']
del_message = []
for layer_i, value in enumerate(message):             
    if message[layer_i] not in locals().keys():
        del_message.append(value)
for m in del_message:
    message.remove(m)
print(f'message:{message}')
```
运行结果：
```python
C:\Users\DELL>python3 test_locals.py
message:['ethernet', 'dhcpv6']
```



<center><b>--THE END--<b></center>