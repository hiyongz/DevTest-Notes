#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/3/14 7:53
# @Author:  haiyong
# @File:    test_client.py

# !/user/bin/env python
# -*- coding:utf-8 -*-

import socket

# 待建立连接HOST的ip/port
ip_port = ('127.0.0.1', 9999)
# 建立socket
s = socket.socket()
# 建立连接
s.connect(ip_port)
while (True):
    # 待发送的信息
    send_data = input('给对方发送信息：').strip()
    s.send(bytes(send_data, encoding='utf-8'))
    print('等待对方回复:')
    # 接收信息并显示
    recv_data = s.recv(1024)
    print('你有新的消息:', str(recv_data, encoding='utf-8'))
s.close()

