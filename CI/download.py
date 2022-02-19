#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2022/2/18 11:58
# @Author:  haiyong
# @File:    download.py

import sys
import os
import re

# print(sys.argv)

# print(sys.argv[1])

log_cmd = "D:/pythonproj/DevTest-Notes/CI/ftp_download.bat /release/ugw6.0/ugw6.0_dailybuild/dev_ugw6.0_main/latest_version/RX27pro/ D:\\pythonproj\\DevTest-Notes\\CI\\jenkins"
log = os.system(log_cmd)
# logs = log.read()
# if len(logs) == 0:
#     print("No changes")
# else:
#     logs2 = logs.split("\n")
#     print(logs)






