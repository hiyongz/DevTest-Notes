from socket import *

HOST = '192.168.52.111'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input("Client>")
    if not data:
        break
    tcpCliSock.send(data)
    message = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print "="*20
    print "[From Servier]:",message

tcpCliSock.close()
