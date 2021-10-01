#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/4/30 16:23
# @Author:  haiyong
# @File:    test_getopt.py

# python命令行参数解析 getopt
import getopt

from scapy.all import *
import sys

class ArgParser():
    # 预处理输入参数
    def usage(self):
        Usage = """
        Usage: python test_getopt [OPTION...]\n \n \
        Options:\n \
        -f, --field \t\t-- 字段\n \
        -Y, --display-filter \t-- 条件\n \
        -c, --count \t\t-- 计数\n \
        -h, --help \t\t-- 帮助信息\n \n\
        """
        print(Usage)

    def arg_parser(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:], "f:Y:c:h", ["field=","display-filter=", "count=","return_flag=", "help"])
        except getopt.GetoptError as e:
            print(e)
            self.usage()
            sys.exit()
        print(sys.argv[0] + ' ' + ' '.join(sys.argv[1:]))
        if opts == []:
            self.usage()
            sys.exit()
        for op, value in opts:
            if op in ("-f", "--field"):
                self.filters = value
                print(f"filter: {value}")
            elif op in ("-Y", "--display-filter"):
                self.display_filter = value
                print(f"display-filter: {value}")
            elif op in ("-c", "--count"):
                self.count = int(value)
                print(f"count: {value}")
            elif op in ('-h', '--help'):
                self.usage()
                sys.exit()

if __name__ == "__main__":
    arg = ArgParser()
    arg.arg_parser()