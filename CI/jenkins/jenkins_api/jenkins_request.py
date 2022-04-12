#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/6/28 15:20
# @Author:  haiyong
# @File:    jenkins_request.py
import json
import requests

class JenkinsApiDemo():
    def __init__(self):
        self.jenkins_host = '192.168.30.8'
        self.jenkins_port = '8080'
        self.username = 'admin'
        self.pwd = 'admin'
        self.api_token = '11f8790b23a9983c0a218ba125aa855f61'
        self.jenkins_url = f"http://{self.jenkins_host}:{self.jenkins_port}"

    def jenkinsRestart(self):
        url = f"{self.jenkins_url}/restart"
        ret = requests.post(url, auth=(self.username, self.api_token), verify=False)
        print(ret.text)

    def jenkinsSafeRestart(self):
        url = f"{self.jenkins_url}/safeRestart"
        ret = requests.post(url, auth=(self.username, self.api_token), verify=False)
        print(ret.text)

    def getbuildNumber(self):
        url = f"{self.jenkins_url}/job/RF-Pipeline-Demo/lastBuild/buildNumber"
        ret = requests.get(url)
        print(ret.text)

    def getRFResults(self):
        url = f"{self.jenkins_url}/view/demo/job/RF-Pipeline-Demo/3/api/json"
        ret = requests.get(url)
        res = ret.json()
        print(res["actions"][3]["failCount"])
        print(json.dumps(ret.json(),indent=2))

    def checkBuilding(self,jobname):
        # 查看当前job是否正在构建
        url = f"{self.jenkins_url}/job/{jobname}"
        url = f"{self.jenkins_url}/job/{jobname}/api/json?tree=lastCompletedBuild[number],lastBuild[number]"
        res = requests.get(url)
        res = res.json()
        if res["lastBuild"]["number"] == res["lastCompletedBuild"]["number"]:
            return False
        else:
            print(f"{jobname}正在构建中...")
            return True

    def triggerBuild(self,jobname):
        url = f"{self.jenkins_url}/view/demo/job/{jobname}/build"
        # url = "http://192.168.30.8:8080/view/demo/job/RF-Pipeline-Demo/build"
        if not self.checkBuilding(jobname):
            res = requests.post(url, auth=(self.username, self.api_token), verify=False)
            print(res.text)

    def triggerBuildWithParameters(self,jobname):
        jenkins_params = {'param1': 'value11',
                          'param2': 'value22'}
        url = f"{self.jenkins_url}/view/demo/job/{jobname}/buildWithParameters"
        if not self.checkBuilding(jobname):
            res = requests.post(url, auth=(self.username, self.api_token), params=jenkins_params, verify=False)
            print(res.text)

    def deletelastBuild(self,jobname):
        url = f"{self.jenkins_url}/view/demo/job/{jobname}/4/doDelete"
        if not self.checkBuilding(jobname):
            res = requests.post(url, auth=(self.username, self.api_token), verify=False)

    def demo(self):
        url = "http://admin:admin@192.168.30.8:8080/job/demo/build"

        # payload = {'Jenkins-Crumb': 'a43dfa440dc045a49757a93454bbd335c27fbaa90cf65e6d79ef6d6833386e7d'}
        header = {'Jenkins-Crumb': '0a49b192a3388815e1bfbb2b7ca88faf0a5e883d9a98195a427e508aa1d08cbf'}

        # ret = requests.post(url,json=payload)
        ret = requests.post(url=url,headers=header)
        # ret = requests.post(url=url,cookies=header)

        # print(ret.text)


        # url = "http://admin:admin@192.168.30.8:8080/job/demo/lastBuild/buildNumber"
        # ret = requests.get(url)
        # print(ret.text)

        # url = "http://admin:admin@192.168.30.8:8080/job/demo/17/api/json"
        # ret = requests.get(url)
        # print(json.dumps(ret.json(),indent=2))

if __name__ == '__main__':
    jk_api = JenkinsApiDemo()
    jobname = "RF-Pipeline-Demo"
    # jobname = "demo"
    # jk_api.jenkinsRestart()
    # jk_api.getbuildNumber()
    # jk_api.getRFResults()
    # jk_api.checkBuilding(jobname)
    # jk_api.triggerBuild(jobname)
    # jk_api.triggerBuildWithParameters(jobname)
    jk_api.deletelastBuild(jobname)