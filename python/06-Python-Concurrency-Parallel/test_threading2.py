#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/22 20:56
# @Author:  haiyong
# @File:    test_threading.py


import _thread
import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)
loops = [2,4]
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def run(self):
        self.func(*self.args)

def loop(nloop, nsec):
    logging.info("start loop " + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop " + str(nloop) + " at " + ctime())

def main():
    logging.info("start all at " + ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t= MyThread(loop, (i,loops[i],loop.__name__))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()

    logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()