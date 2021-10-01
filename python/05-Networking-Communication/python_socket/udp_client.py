# -*- coding: utf-8 -*-
from socket import *
# HOST = 'localhost'  # 主机名
# PORT = 6001  # 端口号 与服务器一致
HOST = '192.168.87.1'  # 主机名
PORT = 139  # 端口号 与服务器一致
BUFSIZE = 1024  # 缓冲区大小1K
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:  # 无限循环等待连接到来
    try:
        data = raw_input('>')
        if not data:
            break
        udpCliSock.sendto(data, ADDR)  # 发送数据
        data, ADDR = udpCliSock.recvfrom(BUFSIZE)  # 接受数据
        if not data:
            break
        print 'Server : ', data

    except Exception, e:
        print 'Error: ', e

udpCliSock.close()  # 关闭客户端