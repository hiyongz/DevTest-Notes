#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2022/1/6 14:54
# @Author:  haiyong
# @File:    svn_check.py
import os
import re

log_cmd = "svn log -l1 -v https://192.168.100.21/svn/attrobot-testcase/MX_release"
log = os.popen(log_cmd)
logs = log.read()
if len(logs) == 0:
    print("No changes")
else:
    logs2 = logs.split("\n")
    tag = ''
    user = ''
    time = ''
    software_path = ''
    for l in logs2:
        print(l)
        if "|" in l:
            m = l.split(" | ")
            user = m[1]
            time = m[2]
            reg = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
            time = re.findall(reg, time)[0]
            date = time.split(" ")[0]
            print(time)

        if "/MX_release/" in l:
            if software_path == '':
                changed_paths = l.strip()
                software_path = f"/MX_release/release-{date}"

        if "tag" in l:
            tags = re.findall(r"(?<=tag:).*?(?=$)", l)  # 匹配时间和单位
            try:
                tag = tags[0]
            except:
                tag = ''
            print(tag)

    with open("rf_include.ini", 'w') as f:
        f.write('tag=%s\n' % tag)
        f.write('user=%s\n' % user)
        f.write('time=%s\n' % time)
        f.write('software_path=%s\n' % software_path)




