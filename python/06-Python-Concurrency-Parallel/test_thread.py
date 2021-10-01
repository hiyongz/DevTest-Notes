#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/22 20:35
# @Author:  haiyong
# @File:    test_threading.py
import _thread
import logging
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)
loops = [2,4]
def loop0():
    logging.info("start loop0 at " + ctime())
    sleep(4)
    logging.info("end loop0 at " + ctime())
def loop1():
    logging.info("start loop1 at " + ctime())
    sleep(2)
    logging.info("end loop1 at " + ctime())

def main():
    logging.info("start all at " + ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)
    # loop0()
    # loop1()
    logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()