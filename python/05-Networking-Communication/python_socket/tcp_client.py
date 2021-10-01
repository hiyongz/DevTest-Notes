#-*-coding:utf-8-*-
import socket
from socket import *
from time import ctime

# HOST = '127.0.0.1' #服务器IP地址
# HOST = '192.168.29.1' #服务器IP地址
HOST = '125.81.58.246'
POST = 49760
BUFSIZ = 1024
serverAddr  = (HOST, POST)

#创建套接字
tcpCliSock = socket(AF_INET, SOCK_STREAM)
#链接服务器
tcpCliSock.connect(serverAddr )
# #sock.send('Test\n')
# tcpCliSock.send(raw_input("Please input : "))


while True:
    # 发送数据
    # sendData = raw_input('please input the send message:')
    sendData = 'Hello/n'
    if len(sendData) > 0:
        tcpCliSock.send(sendData)
    else:
        break
    # 接收数据
    recvData = tcpCliSock.recv(BUFSIZ)
    if not recvData:
        break
    print("[%s]: %s" % (ctime(), recvData.decode()))
# 关闭套接字
tcpCliSock.close()
