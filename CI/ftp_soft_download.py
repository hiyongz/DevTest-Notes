#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2022/2/18 15:41
# @Author:  haiyong
# @File:    ftp_soft_download.py

'''
FTP批量下载数据
'''
import os
import sys
from ftplib import FTP

class FtpDownloadCls:
    def __init__(self, ftpserver, port, usrname, pwd):
        self.ftpserver = ftpserver # ftp主机IP
        self.port = port          # ftp端口
        self.usrname = usrname  # 登陆用户名
        self.pwd = pwd          # 登陆密码
        self.ftp = self.ftpConnect()

    # ftp连接
    def ftpConnect(self):
        ftp = FTP()
        try:
            ftp.connect(self.ftpserver, self.port)
            ftp.login(self.usrname, self.pwd)
        except:
            raise IOError('\n FTP login failed!!!')
        else:
            print(ftp.getwelcome())
            print('\n+------- FTP connection successful!!! --------+\n')
            return ftp

    # 单个文件下载到本地
    def downloadFile(self, ftpfile, localfile):
        bufsize = 1024
        with open(localfile, 'wb') as fid:
            self.ftp.retrbinary('RETR {0}'.format(ftpfile), fid.write, bufsize)
        return True

    # 下载整个目录下的文件,包括子目录文件
    def downloadFiles(self, ftpath, localpath):
        print('FTP PATH: {0}'.format(ftpath))
        if not os.path.exists(localpath):
            os.makedirs(localpath)
        self.ftp.cwd(ftpath)
        print('\n+----------- downloading!!! -----------+\n')
        for i, file in enumerate(self.ftp.nlst()):
            print('{0} <> {1}'.format(i, file))
            local = os.path.join(localpath, file)
            if os.path.isdir(file): # 判断是否为子目录
                if not os.path.exists(local):
                    os.makedirs(local)
                self.downloadFiles(file, local)
            else:
                self.downloadFile(file, local)
        self.ftp.cwd('..')
        return True

    # 退出FTP连接
    def ftpDisConnect(self):
        self.ftp.quit()

# 程序入口
if __name__ == '__main__':
    # 输入参数
    ftpserver = '172.16.30.75' # ftp主机IP
    port = 21                                  # ftp端口
    usrname = 'pingtai'       # 登陆用户名
    pwd = 'pingtai'       # 登陆密码
    # ftpath = '/release/ugw6.0/ugw6.0_dailybuild/dev_ugw6.0_main/latest_version/RX27pro/'  # 远程文件夹
    # localpath = 'D:\\pythonproj\\DevTest-Notes\\CI'
    ftpath = sys.argv[1]
    localpath = sys.argv[2]

    Ftp = FtpDownloadCls(ftpserver, port, usrname, pwd)
    Ftp.downloadFiles(ftpath, localpath)
    Ftp.ftpDisConnect()
    os.chdir(localpath) 
    data=""
    for k in os.listdir(localpath):
        if '.bin' in k:
            data="soft_path=RX27pro"
            break
    filename = '../rf_include.ini'
    if os.path.exists(filename):
        os.remove(filename)
    fd = open(filename, 'a+')
    fd.write(data)
    fd.flush()
    fd.close()
    print("\n+-------- OK!!! --------+\n")