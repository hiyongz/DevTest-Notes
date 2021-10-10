# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 下午3:10
# @Author  : YTQ
# @FileName: jenkins_utils.py
# @Software: PyCharm
import configparser
import datetime
import os
import re

from jenkinsapi.jenkins import Jenkins
from src.utils.log_utils import LogUtils

log = LogUtils()
def get_jk_config(chose):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.getcwd(), 'jenkins_server.ini'))
    username = config.get(chose, 'username')
    password = config.get(chose, 'password')
    host = config.get(chose, 'host')
    port = config.get(chose, 'port')
    url = "http://" + host + ":" + port
    return url,username,password

class JenkinsUtils:

    def __init__(self,th_id,job_name,chose = 'jenkins'):
        self.th_id = str(th_id)
        self.job_name = job_name
        config = get_jk_config(chose)
        self.jk = Jenkins(*config,useCrumb=True)

    def ts(self):
        # print(self.jk[self.jk.keys()[0]].get_config())
        # v_k = {i[0]: list(i[1].keys()) for i in self.jk.views.iteritems()}
        # print(v_k)
        # print(self.jk.keys())
        # for job in self.jk.keys():
        #     if "testdemo" in job:
        #         my_job = self.jk.get_job(job)
        #         print(my_job.get_build(34).get_console())
        pass

    def get_jobs(self):
        uat_job_list = []
        for _job in self.jk.keys():
            if "testzuche" in _job:
                uat_job_list.append(_job)
        return uat_job_list

    def get_job_from_keys(self):
        choose_list = []
        for my_job_name in self.get_jobs():
            if self.job_name in my_job_name:
                choose_list.append(my_job_name)
        return choose_list

    def job_build(self,my_job_name):
        if self.jk.has_job(my_job_name):
            my_job = self.jk.get_job(my_job_name)
            if not my_job.is_queued_or_running():
                try:
                    last_build = my_job.get_last_buildnumber()
                except Exception as e:
                    last_build = 0
                build_num = last_build +1
                # 开始打包
                try:
                    self.jk.build_job(my_job_name)
                except Exception as e:
                    log.error("线程" + self.th_id + str(e))

                # 循环判断Jenkins是否打包完成
                while True:
                    if not my_job.is_queued_or_running():
                        # 获取最新一次打包信息
                        count_build = my_job.get_build(build_num)
                        # 获取打包开始时间
                        start_time = count_build.get_timestamp() + datetime.timedelta(hours=8)
                        # 获取打包日志
                        console_out = count_build.get_console()
                        # 获取状态
                        status = count_build.get_status()
                        # 获取变更内容
                        change = count_build.get_changeset_items()
                        log.info("线程" + self.th_id + " " + str(
                            start_time) + " 发起的" + my_job_name + "构建已经完成，构建的状态为： " + status)
                        p2 = re.compile(r".*ERROR.*")
                        err_list = p2.findall(console_out)
                        if status == "SUCCESS":
                            if len(change) > 0:
                                for data in change:
                                    for file_list in data["affectedPaths"]:
                                        log.info("线程" + self.th_id + " 发起的" + my_job_name + " 变更的类： " + file_list)
                                    log.info("线程" + self.th_id + " 发起的" + my_job_name + " 变更的备注： " + data["msg"])
                                    log.info("线程" + self.th_id + " 发起的" + my_job_name + " 变更的提交人： " + data["author"][
                                        "fullName"])
                            else:
                                log.info("线程" + self.th_id + " 发起的" + my_job_name + " 本次构建没有变更内容！")
                            if len(err_list) > 0:
                                log.warning("线程" + self.th_id + " 构建的" + my_job_name + "构建状态为成功，但包含了以下错误：")
                                for error in err_list:
                                    log.error(error)
                        else:
                            if len(err_list) > 0:
                                log.warning("线程" + self.th_id + " 构建的" + my_job_name + "包含了以下错误：")
                                for error in err_list:
                                    log.error(error)
                        break
            else:
                log.warning("线程" + self.th_id +  " 发起的" + my_job_name + ' Jenkins is running')
        else:
            log.warning("线程" + self.th_id +  " 发起的" + my_job_name + ' 没有该服务')

    def jk_build_job(self):
        my_job_name = self.get_job_from_keys()
        if len(my_job_name) == 1:
            self.job_build(my_job_name[0])
        elif len(my_job_name) == 0:
            log.error("线程" + self.th_id + " 输入的job模糊名不正确！")
        else:
            index = int(input("线程" + self.th_id + "从列表中选择你要构建的任务："+ str(list(enumerate(my_job_name,start=1))) + "\n"))
            try:
                my_job_name = my_job_name[index - 1]
                self.job_build(my_job_name)
            except:
                log.error("线程" + self.th_id + " 选择不正确")

if __name__ == '__main__':
    jk = JenkinsUtils(1,"vehicle")
    # jk.jk_build_job()
    print(jk.get_jobs())