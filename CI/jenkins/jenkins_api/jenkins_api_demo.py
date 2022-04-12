#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2022/2/20 16:52
# @Author:  hiyongz
# @File:    jenkins_api_demo.py

import datetime
from jenkinsapi.jenkins import Jenkins

class JenkinsApiDemo:
    def __init__(self, job_name, chose='jenkins'):
        self.jenkins_host = '192.168.30.8'
        self.jenkins_port = '8080'
        self.username = 'admin'
        self.pwd = 'admin'
        self.jenkins_url = f"http://{self.jenkins_host}:{self.jenkins_port}"
        self.job_name = job_name
        self.jenkins_server = Jenkins(self.jenkins_url, username=self.username, password=self.pwd, useCrumb=True)

    def GetJenkinsVersion(self):
        print(self.jenkins_server.version)
        return self.jenkins_server.version

    def jobBuild(self):
        if self.jenkins_server.has_job(self.job_name):
            myjob = self.jenkins_server.get_job(self.job_name)
            if not myjob.is_queued_or_running():
                self.jenkins_server.build_job(self.job_name)

    def disableJob(self):
        """Disable a Jenkins job"""
        if self.jenkins_server.has_job(self.job_name):
            job_instance = self.jenkins_server.get_job(self.job_name)
            job_instance.disable()
            print('Job %s Is Enabled ?:%s' % (self.job_name, job_instance.is_enabled()))

    def enableJob(self):
        """Disable a Jenkins job"""
        if self.jenkins_server.has_job(self.job_name):
            job_instance = self.jenkins_server.get_job(self.job_name)
            job_instance.enable()
            print('Job %s Is Enabled ?:%s' % (self.job_name, job_instance.is_enabled()))

    def getJobInfo(self):
        if self.jenkins_server.has_job(self.job_name):
            myjob = self.jenkins_server.get_job(self.job_name)
            if not myjob.is_queued_or_running():
                last_buildnumber = myjob.get_last_buildnumber()
                print("last_buildnumber: ", last_buildnumber)

                last_build = myjob.get_build(last_buildnumber)
                # 获取开始时间
                start_time = last_build.get_timestamp() + datetime.timedelta(hours=8)
                print("start_time: ", start_time)
                print("status: ", last_build.get_status())
                print("build_url: ", last_build.get_build_url())
                print("duration: ", last_build.get_duration())
                print("causes: ", last_build.get_causes()[0]["shortDescription"])
                print("change: ", last_build.get_changeset_items())
                print("console_log: ", last_build.get_console())
            else:
                print(self.job_name + " is running")
        else:
            print("没有 " + self.job_name + " 这个job")

    def get_plugin_details(self):
        for plugin in self.jenkins_server.get_plugins().values():
            print("Short Name:%s" % (plugin.shortName))
            print("Long Name:%s" % (plugin.longName))
            print("Version:%s" % (plugin.version))
            print("URL:%s" % (plugin.url))
            print("Active:%s" % (plugin.active))
            print("Enabled:%s" % (plugin.enabled))
    def demo(self):
        self.jenkins_server.create_job(jobname, xml)
        self.jenkins_server.copy_job(jobname, newjobname)
        self.jenkins_server.create_node(name)
        self.jenkins_server.delete_job(jobname)
        self.jenkins_server.delete_node(nodename)
        self.jenkins_server.safe_restart()
        self.jenkins_server.shutdown()

if __name__ == '__main__':
    jobname = "RF-Pipeline-Demo"
    jk = JenkinsApiDemo(jobname)
    jk.GetJenkinsVersion()
    # jk.jobBuild()
    jk.disableJob()
    jk.enableJob()
    jk.getJobInfo()
    jk.get_plugin_details()
