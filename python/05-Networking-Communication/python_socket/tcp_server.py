#-*-coding:utf-8-*-
import socket
import os
import time
#创建套接字
# host = '172.22.41.221'
host = '125.81.58.246'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("localhost", 8888))
server.bind((host, 139))
server.listen(0)
while True:
    connection, address = server.accept()
    print(connection, address)
    recv_str=connection.recv(1024)[0:5]
    #recv_str=str(recv_str)  这样不行带有了b''
    recv_str=recv_str.decode("ascii")
    if len(recv_str)>0:
        # a = bytes("test: %s" % recv_str,encoding="ascii")
        connection.send(bytes(1))
        print recv_str,len(recv_str)
    # else:
    #     connection.close()
    #     print('----------')
    #     break

    # connection.send( bytes("test: %s" % recv_str,encoding="ascii") )
    time.sleep( 0.5 )
connection.close()

