# 持续集成：Jenkins API简单使用
Jenkins具有丰富的API接口，可以通过调用API接口实现对Job的触发、删除、查看任务状态等操作，支持HTTP协议，支持用户名、密码认证，提供的这些接口可以实现对 Jenkins 的控制。下面介绍Jenkins API的使用实例。
<!--more-->


先创建一个有Job任务运行和状态查询权限的用户，可使用admin用户；新建一个项目（可参考[持续集成平台Jenkins介绍](https://blog.csdn.net/u010698107/article/details/113823608)）

## Jenkins API调用示例

### 远程调用 Jenkins API返回最新任务编号
GET请求
URL：http://username:password@hostname:port/job/任务名/lastBuild/buildNumber

```python
import requests

url = "http://admin:admin@192.168.30.8:8080/job/demo/lastBuild/buildNumber"
ret = requests.get(url)
print(ret.text)
```
输出：
```python
17
```
![](continuous-integration-for-jenkins-api/jenkins_api_lastbuild.png)


### 远程调用 Jenkins API查询任务状态
GET请求
URL：http://username:password@hostname:port/job/任务名/\<build number>/api/json

```python
import json
import requests
url = "http://admin:admin@192.168.30.8:8080/job/demo/17/api/json"
ret = requests.get(url)
print(json.dumps(ret.json(),indent=2))
```
返回的日志
```python
{
  "_class": "hudson.model.FreeStyleBuild",
  "actions": [
    {
      "_class": "hudson.model.CauseAction",
      "causes": [
        {
          "_class": "hudson.model.Cause$UserIdCause",
          "shortDescription": "Started by user anonymous",
          "userId": null,
          "userName": "anonymous"
        }
      ]
    },
    {},
    {
      "_class": "org.jenkinsci.plugins.displayurlapi.actions.RunDisplayAction"
    }
  ],
  "artifacts": [],
  "building": false,
  "description": null,
  "displayName": "#17",
  "duration": 109,
  "estimatedDuration": 222,
  "executor": null,
  "fullDisplayName": "demo #17",
  "id": "17",
  "keepLog": false,
  "number": 17,
  "queueId": 3,
  "result": "SUCCESS",
  "timestamp": 1615705287802,
  "url": "http://192.168.30.8:8080/job/demo/17/",
  "builtOn": "",
  "changeSet": {
    "_class": "hudson.scm.EmptyChangeLogSet",
    "items": [],
    "kind": null
  },
  "culprits": []
}
```
### 远程调用 Jenkins API启动任务
使用POST请求方法：
URL：http://username:password@hostname:port/job/任务名/build

```python
import requests
url = "http://admin:admin@192.168.30.8:8080/job/demo/build"
ret = requests.post(url)
print(ret.text)
```

![](continuous-integration-for-jenkins-api/jenkins_api_build.png)
Jenkins 跨站请求伪造保护采取 Crumb（碎片生成器），可以使用jenkinsapi库来调用api
## Python jenkinsapi库
jenkinsapi库封装了Jenkins api 的调用方法
安装：
```sh
$ pip install jenkinsapi
```
下面代码实现启动job名为demo的任务
```python
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
```
输出：
```python
Finished
build_num：20
```
![](continuous-integration-for-jenkins-api/jenkins_api_build2.png)



