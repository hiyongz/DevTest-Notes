import configparser
import datetime
import logging
import os
import re

from jenkinsapi.jenkins import Jenkins

jk = Jenkins('http://192.168.30.8:8080', username='admin', password='admin', useCrumb=True)
# print(jk.keys())
job_name = 'demo'
if jk.has_job(job_name):
    my_job = jk.get_job(job_name)
    if not my_job.is_queued_or_running():
        try:
            last_build = my_job.get_last_buildnumber()
        except:
            last_build = 0
        build_num = last_build + 1

        # 启动任务
        try:
            jk.build_job(job_name)
        except Exception as e:
            print(str(e))
        while True:
            if not my_job.is_queued_or_running():
                print("Finished")
                print(f"build_num：{build_num}")
                break
        # 获取最新一次打包信息