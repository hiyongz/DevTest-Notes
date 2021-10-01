# -*- coding: utf-8 -*-
from socket import *
from time import ctime

HOST = '127.0.0.1'                   #主机名
PORT =  6001               #端口号
BUFSIZE = 1024              #缓冲区大小1K
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)       #绑定地址到套接字

while True:                 #无限循环等待连接到来
    try:
        print 'Waiting for message ....'
        data, addr = udpSerSock.recvfrom(BUFSIZE)          #接受UDP
        print 'Get client msg is: ', data
        udpSerSock.sendto('[%s] %s' %(ctime(),data), addr) #发送UDP
        print 'Received from and returned to: ',addr

    except Exception,e:
        print 'Error: ',e
udpSerSock.close()          #关闭服务器