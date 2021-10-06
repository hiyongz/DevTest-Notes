# Docker搭建持续集成平台Jenkins
本文介绍使用docker来安装Jenkins服务的步骤。

<!--more-->
## Docker搭建Jenkins
### 1. 安装
Jenkins docker hub地址: [https://hub.docker.com/r/jenkins/jenkins](https://hub.docker.com/r/jenkins/jenkins)
```docker
docker pull jenkins/jenkins
```
```sh
[root@server /]# docker pull jenkins/jenkins
Using default tag: latest
latest: Pulling from jenkins/jenkins
3192219afd04: Already exists 
17c160265e75: Already exists 
cc4fe40d0e61: Already exists 
9d647f502a07: Already exists 
d108b8c498aa: Already exists 
1bfe918b8aa5: Already exists 
dafa1a7c0751: Already exists 
c69d355c63ac: Pull complete 
b15898bb1800: Pull complete 
a51ccfc981f7: Pull complete 
49f46bd4bf74: Pull complete 
efa670fd97de: Pull complete 
1565294bcba3: Pull complete 
4c51bcfbed1e: Pull complete 
49f4fafbfbf2: Pull complete 
28a75541fa5f: Pull complete 
c3c03c2d5564: Pull complete 
ace64d1af7cf: Pull complete 
f1960af3b8ab: Pull complete 
6fd1a5a6d017: Pull complete 
Digest: sha256:e4630b9084110ad05b4b51f5131d62161881216d60433d1f2074d522c3dcd6dc
Status: Downloaded newer image for jenkins/jenkins:latest
docker.io/jenkins/jenkins:latest
```

### 2. 创建docker的文件影射卷
创建docker的文件影射卷，用于存储数据
```docker
[root@server tmp]# docker volume create jenkins_test
[root@server tmp]# docker volume inspect jenkins_test
[
    {
        "CreatedAt": "2020-07-18T10:49:17+08:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/jenkins_test/_data",
        "Name": "jenkins_test",
        "Options": {},
        "Scope": "local"
    }
]
[root@server tmp]# 
```

### 3. 运行: 创建实例
创建一个挂载目录jenkins，添加可执行权限：`chmod 777 jenkins`

```docker
docker run --name=jenkins -d -p 8080:8080 -p 50000:50000 -v jenkins_test:/var/jenkins_home jenkins/jenkins
```

运行：
```sh
[root@server /]# docker run --name=jenkins -d -p 8080:8080 -p 50000:50000 -v jenkins_test:/var/jenkins_home jenkins/jenkins
c7fb87aec99402febd95edddda5cf1dc7ad15437f674bf71a09692d93369ccb9
[root@server /]# 
[root@server /]# docker ps
CONTAINER ID   IMAGE             COMMAND                  CREATED         STATUS         PORTS                                              NAMES
c7fb87aec994   jenkins/jenkins   "/sbin/tini -- /usr/…"   9 minutes ago   Up 9 minutes   0.0.0.0:8080->8080/tcp, 0.0.0.0:50000->50000/tcp   jenkins
```
浏览器输入电脑IP地址+端口号：http://192.168.0.103:8080/

![](container-docker-for-jenkins-install/jenkins-8080.png)

`docker logs -f jenkins`  查看输出日志
![](container-docker-for-jenkins-install/jenkins-init-pwd.png)

注意：jenkins默认启动后的时区为美国，通过以下命令启动中国时区：
```sh
# 先删除已经构建的jenkins实例
docker rm -f jenkins
# 重新创建实例并设置时区
docker run --name=jenkins -d -p 8080:8080 -p 50000:50000 -v jenkins_test:/var/jenkins_home -e JAVA_OPTS=-Duser.timezone=Asia/Shanghai jenkins/jenkins
```
### 4. 查看默认密码

```docker
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```
![](container-docker-for-jenkins-install/jenkins-default-pwd.png)

### 5. 输入密码
等待初始化完成后，输入密码
![](container-docker-for-jenkins-install/jenkins-input-pwd.png)

### 6. 安装推荐的插件
![](container-docker-for-jenkins-install/jenkins-plugins1.png)

### 7. 设置用户名密码
![](container-docker-for-jenkins-install/jenkins-username-pwd.png)

### 8. Jenkins URL配置
![](container-docker-for-jenkins-install/jenkins-url.png)

配置成功后，进入欢迎界面
![](container-docker-for-jenkins-install/jenkins-home-page.png)

## Windows安装Jenkins
war文件启动方法

下载地址：[https://www.jenkins.io/download/](https://www.jenkins.io/download/)
![](container-docker-for-jenkins-install/jenkins-war.png)

进入war包所在路径执行命令：
```sh
java -jar jenkins.war --httpPort=8081
```

可以直接下载jenkins.msi文件安装
![](container-docker-for-jenkins-install/jenkins-windows.png)

配置方法和Linux类似





