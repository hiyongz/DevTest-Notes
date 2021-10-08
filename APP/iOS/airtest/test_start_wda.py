#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/9/26 14:00
# @Author:  haiyong
# @File:    test_start_wda.py

# 后台启动wda

import os
import time

class StartWDA():
    def check_wda_port(self, port):
        """检查是否启动wda
        :return:
        """
        pid = os.popen("netstat -nao | findstr %s"%port)
        pids = pid.read()
        if len(pids) == 0:
            print("no process with port %s"%port)
            return False
        else:
            pids2 = pids.split("\n")
            for p in pids2:
                p1 = p.split(" ")
                new_pid = [x for x in p1 if x != '']
                process = os.popen("tasklist | findstr %s"%new_pid[4]).read()
                if "python" in process:
                    return True

    def start_wda(self,udid,wda_id,port):
        os.system(f'start_wda.vbs "start_wda.bat" " {udid}" " {wda_id}" " {port}"')
        for l in range(3):
            time.sleep(3)
            if self.check_wda_port(port):
                print("WebDriverAgent start successfully")
                return
        print("wda started failed")

    def stop_wda(self,port):
        pid = os.popen("netstat -nao | findstr %s"%port)
        pids = pid.read()
        if len(pids) == 0:
            print("no process with port %s"%port)
            return True
        else:
            pids2 = pids.split("\n")
            for p in pids2:
                p1 = p.split(" ")
                new_pid = [x for x in p1 if x != '']
                process = os.popen("tasklist | findstr %s"%new_pid[4]).read()
                if "python" in process:
                    res = os.popen("taskkill -pid %s -f -t"%new_pid[4]).read()
                    if "SUCCESS" in res:
                        print(res)
                        return True
            return False

if __name__ == '__main__':
    wda = StartWDA()
    wda.start_wda("00008101-000255021E08001E", "com.facebook.WebDriverAgent.tendatest6.xctrunner", "8100")
    wda.stop_wda("8100")

