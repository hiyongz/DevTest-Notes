#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/18 20:02
# @Author:  haiyong
# @File:    demo.py
import requests
from jsonpath import jsonpath
from hamcrest import *

class TestDemo():
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 300

    def test_query(self):
        payload = {
            "level": 1,
            "name": "testing"
        }

        r = requests.get('http://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "testing"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200
    def test_header(self):
        r = requests.post('http://httpbin.testing-studio.com/post', headers={"h":"header"})
        print(r.text)
        assert r.status_code == 200
        assert r.json()['headers']['H'] == "header"

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "testing"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

    def test_hogwarts_json(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        print(jsonpath(r.json(), '$..name'))
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == "霍格沃兹测试学院公众号"
        assert jsonpath(r.json(),'$..name')[0] == "霍格沃兹测试学院公众号"

    def test_hamcrest(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        # print(r.text)
        print(r.json())
        print(jsonpath(r.json(), '$..name'))
        assert_that(r.json()['category_list']['categories'][0]['name'],equal_to("霍格沃兹测试学院公众号"))

    def test_token_get(self):
        url = "http://192.168.5.128:8000/api/blade-auth/oauth/token"
        heards = {
            "Accept":
            "application/json, text/plain, */*",
            "Accept-Encoding":
            "gzip, deflate",
            "Accept-Language":
            "zh-CN,zh;q=0.9",
            "Authorization":
            "Basic c2FiZXI6c2FiZXJfc2VjcmV0",
            "Captcha-Code":'',
            "Captcha-Key":
            "f8c54023fda07f1cd206fb8775d03a0f",
            "Connection":
            "keep-alive",
            "Content-Length":'0',
            "Dept-Id": '',
            "Host":
            "192.168.5.128:8000",
            "Origin":
            "http: // 192.168.5.128:8000",
            "Referer":
            "http: // 192.168.5.128:8000/login",
            "Role-Id":'' ,
            "Tenant-Id": '000000',
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        paylod = {
            'tenantId': 000000,
            'username': 18684650130,
            'password': 'e10adc3949ba59abbe56e057f20f883e',
            'grant_type': 'captcha',
            'scope': 'all',
            'type':'account'
        }
        res = requests.post(url=url, headers=heards,params=paylod)
        print(res.text)
        token = res.json()['access_token']
        print(token)
        return token

    def test_post(self):
        url = "http://192.168.5.128:8000/api/blade-ethic/project/save"
        payload = {
            'formId':3408620468473692161,
            'version': 2,
            'committeeId': 1706990327537123329,
            'committeeName': '长沙先领医药科技有限公司',
            'saveType': 1,
            'content': '{"newProFlag":"","highRiskProjectFlag":"0","proName":"测试项目","proNo":"","proCategoryCode":"","expectedExperimentStartTime":"","expectedExperimentEndTime":"","a169519911344582544":null,"a169519968147946860":"","a169519960435983670":[],"a169519971832083007":null,"a169520004037676210":[],"a169519963869793487":"","a169519965064462255":"","a169520004037697118":"","a169520004037643732":"","clinicalInstitutionCode":"1668132637217230849","professionInfoList":[],"undertakeMajorId":"","piName":"","piContactNumber":"","a169520083764898558":"","piProfessionalTitle":"","a169520091347294435":"","a169520091347211280":"","a16952009134726984":"","sponsorInfoList":[],"clinicalInspectorInfoList":[],"sponsorName":"","sponsorContactName":"","sponsorContactNumber":"","clinicalInspectorName":"","clinicalInspectorContactNumber":"","applicantName":"","applicantContactNumber ":"","clinicalInstitutionName":"三木临床研究机构C","$clinicalInstitutionCode":"三木临床研究机构C","$clinicalInstitutionCode_id":"1668132637217230849","$highRiskProjectFlag":"否","$highRiskProjectFlag_id":"0","proCategoryName":"","proCategoryId":"","$proCategoryCode_id":"","clinicalInstitutionId":"1668132637217230849"}'
          }
        token = self.test_token_get()
        print(token)
        headers = {
            "Accept": "application/json,text/plain,*/*",
            "Accept-Encoding":
            "gzip,deflate",
            "Accept-Language":
            "zh-CN,zh;q=0.9",
            "Authorization":
            "Basic c2FiZXI6c2FiZXJfc2VjcmV0",
            "Blade-Auth":
            "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiIwMDAwMDAiLCJ1c2VyX25hbWUiOiIxODY4NDY1MDEzMCIsInJlYWxfbmFtZSI6IueUs-ivt-S6uiIsImF2YXRhciI6IiIsImF1dGhvc",
            "Connection":
            "keep-alive",
            "Content-Length":
            '1515',
            "Content-Type": "application/json",
            "Cookie": token,
            "Host":
            "192.168.5.128:8000",
            "Origin":
            "http://192.168.5.128:8000",
            "Referer":
            "http://192.168.5.128:8000/myhome/applicant",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }
        res = requests.post(url=url,json=payload,headers=headers)
        print(res.text)
        print(res.json())
        assert res.json()['code'] == 200


if __name__=='__main__':
    r = TestDemo()
    r.test_get()














