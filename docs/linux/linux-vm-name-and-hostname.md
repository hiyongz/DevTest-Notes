# 配置Linux主机名
为了方便区分局域网中的多个Linux主机，可以为每台机器设置主机名，本文介绍hostname配置方法。

<!--more-->


## 1. 配置Linux hostname
下面配置两台centos7 虚拟机，主机名分别配置为client和server，它们主机IP 地址分别为192.168.30.8和192.168.30.9。

### 配置client主机
```sh
[root@client ~]# vi /etc/sysconfig/network
```
添加如下内容，保存：
```text
# Created by anaconda
NETWORKING=yes
hostname=client
```
重启网络：
```sh
[root@client ~]# systemctl restart network
[root@client ~]# hostname
client
[root@client ~]# 
```
如果不生效可以使用如下命令：
```sh
[root@client ~]# hostnamectl set-hostname client
```
### 配置server主机
```sh
[root@server ~]# hostnamectl set-hostname server
```
重启网络：
```sh
[root@server ~]# systemctl restart network
[root@server ~]# hostname
server
[root@server ~]# uname -n
server
```

## 2. 配置hostname与IP映射
配置client和server的hosts文件
```sh
vi /etc/hosts
```
添加如下内容：
```text
192.168.30.8 client
192.168.30.9 server
```

## 3. 测试
通过ping hostname来测试是否配置成功：

client ping server：
```sh
[root@client ~]# ping server -c 3
PING server (192.168.30.9) 56(84) bytes of data.
64 bytes from server (192.168.30.9): icmp_seq=1 ttl=64 time=0.616 ms
64 bytes from server (192.168.30.9): icmp_seq=2 ttl=64 time=0.384 ms
64 bytes from server (192.168.30.9): icmp_seq=3 ttl=64 time=0.566 ms

--- server ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2001ms
rtt min/avg/max/mdev = 0.384/0.522/0.616/0.099 ms
[root@client ~]# 
```

server ping client：
```sh
[root@Server ~]# ping client -c 3
PING client (192.168.30.8) 56(84) bytes of data.
64 bytes from client (192.168.30.8): icmp_seq=1 ttl=64 time=0.502 ms
64 bytes from client (192.168.30.8): icmp_seq=2 ttl=64 time=0.678 ms
64 bytes from client (192.168.30.8): icmp_seq=3 ttl=64 time=0.323 ms

--- client ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 0.323/0.501/0.678/0.144 ms
[root@Server ~]# 
```

配置hostname与IP映射后，可以直接ping主机名而不用ping IP地址了。

## 4. 配置windows hosts
配置windows hosts，以便在windows下面能通过主机名进行访问。

编辑 C:\Windows\System32\drivers\etc\hosts文件，添加如下内容：
```sh
192.168.30.8 client
192.168.30.9 server
```
保存

## 5. windows测试

```sh
C:\Users\10287>ping client -n 3

正在 Ping client [192.168.30.8] 具有 32 字节的数据:
来自 192.168.30.8 的回复: 字节=32 时间<1ms TTL=64
来自 192.168.30.8 的回复: 字节=32 时间<1ms TTL=64
来自 192.168.30.8 的回复: 字节=32 时间<1ms TTL=64

192.168.30.8 的 Ping 统计信息:
    数据包: 已发送 = 3，已接收 = 3，丢失 = 0 (0% 丢失)，
往返行程的估计时间(以毫秒为单位):
    最短 = 0ms，最长 = 0ms，平均 = 0ms
```



