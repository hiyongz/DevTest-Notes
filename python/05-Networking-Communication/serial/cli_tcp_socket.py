#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/5/29 11:43
# @Author:  haiyong
# @File:    cli_tcp_socket.py

import socket

def catch_exception(func):
    def wrapper(self, *args, **kwargs):
        try:
            self.socket_connect()
            self.login()
            self.close()
            # self.waitTime(2)
            self.socket_connect()
            u = func(self, *args, **kwargs)
            self.close()
            return u
        except Exception as e:
            return False
    return wrapper

class MyClient():
    def __init__(self, **kargs):
        print('kargs=', kargs)
        if kargs.has_key('expe'):
            self.expe = kargs['expe']
        else:
            self.expe = 'pass'

        if kargs.has_key('baudrate'):
            self.baudrate = kargs['baudrate']
        else:
            self.baudrate = 115200

        if kargs.has_key('port'):
            self.port = kargs['port']
        else:
            self.port = 'COM1'

        if kargs.has_key('PORT'):
            self.PORT = kargs['PORT']
            self.PORT = int(self.PORT)
            print("PORT=", self.PORT)
        else:
            self.PORT = 12345

        ip_port = ('127.0.0.1', self.PORT)
        self.ip_port = ip_port
        try:
            self.socket_connect()
        except Exception as e:
            print("not open socket")
        print("-------connect success-------")

        self.close()

    def socket_connect(self):
        sk = socket.socket()
        self.sk = sk
        self.sk.connect_ex(self.ip_port)
        return self.sk

    @catch_exception
    def login(self):
        # 循环三次进行登录判断
        def revlog():
            self.waitTime(4)
            logindata = self.readfromcom()
            print("logindata", logindata)
            if logindata.find("~ #") >= 0:
                print(u"登录成功")
                return True
            else:
                print(u"第%d次登录失败" % (i))

        for i in range(4):
            try:
                self.mpp_passwd = 'Fireitup' + '\n'
                self.send_cmd(self.mpp_passwd)
                if revlog():
                    return True
            except:
                pass
        return False

    def close(self):
        self.sk.close()
        # print "close  suc!"
        return True

    @catch_exception
    def sendCmd(self,cmd):
        # print "cmd",cmd
        try:
            self.sk.send(cmd)
            # alldata=self.sk.recv(4096)
            return True
        except socket.error as e:
            print("error",e)
            return False
    def recv_cmd(self):
        alldata=""
        try:
            alldata=self.sk.recv(4096)
            # print "alldata",alldata
            return alldata
        except socket.error as e:
            print("error",e)
    def readfromcom(self):
        alldata=""
        while True:
            data=self.recv_cmd()
            if data:
                alldata = "".join(data)
                break
        print("alldata=",alldata)
        return alldata