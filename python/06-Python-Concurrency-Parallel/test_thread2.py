#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/22 20:48
# @Author:  haiyong
# @File:    test_threading2.py

import _thread
import logging
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)
loops = [2,4]
def loop(nloop, nsec, lock):
    logging.info("start loop " + str(nloop) + "at " + ctime())
    sleep(nsec)
    logging.info("end loop " + str(nloop) + "at " + ctime())
    lock.release()

def main():
    logging.info("start all at " + ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop, (i,loops[i],locks[i]))
    for i in nloops:
        while locks[i].locked():pass
    logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()