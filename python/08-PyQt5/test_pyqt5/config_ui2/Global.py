#coding=utf8
import os,sys
import time
import datetime
from configobj import ConfigObj
import configparser
global ConfigFile
def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]   #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path.decode('gbk')
     elif os.path.isfile(path):
         return os.path.dirname(path).decode('gbk')
#打印结果
def gettime():
    timestr=time.strftime(u"%Y-%m-%d_%H%M%S",time.localtime())
    return timestr
def gettime2():
    timestr=time.strftime(u"%Y-%m-%d %H:%M:%S",time.localtime())
    return timestr
def myDate(date1, date2):
    date1 = time.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2 = time.strptime(date2, "%Y-%m-%d %H:%M:%S")
    startTime = time.strftime("%Y-%m-%d %H:%M:%S", date1)
    endTime = time.strftime("%Y-%m-%d %H:%M:%S", date2)
    startTime = datetime.datetime.strptime(startTime,"%Y-%m-%d %H:%M:%S")
    endTime = datetime.datetime.strptime(endTime,"%Y-%m-%d %H:%M:%S")
    date = endTime- startTime
    return date
def timeDiff(date1,date2):
    second=myDate(date1,date2).seconds
    secon=int(second)
    timesss=format("%02d:%02d:%02d"%(secon/3600,secon%3600/60,secon%3600%60))
    return timesss
def ParserCfg(filename):
    kargs={}
    cf = configparser.ConfigParser()
    cf.read(filename.replace("\\","/"))
    for opt in cf.sections():
        if opt:
            kargs[opt]={}
    for opt in kargs.keys():
        for k,v in cf.items(opt):
            kargs[opt][k]=v
    return kargs





