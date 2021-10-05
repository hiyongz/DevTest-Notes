# Linux常用命令：网络命令
本文简要介绍Linux网络配置命令，包括 ip 地址、路由查看、配置等
<!--more-->

## ping
ping: 测试网络连接情况
* `-c`：回应的次数
* `-i`：每次ping的时间间隔
* `-I`：网卡名
* `-t`：ttl 数值
* `-s`：数据包的大小

```bash
# ping ipv6地址
ping -6 -I eth1 2001:db8::10
# ping ipv4地址
ping -I eth1 192.168.0.1 
```


## 网络信息查询

### netstat
netstat: 打印 Linux网络系统的状态信息
* -t 列出所有tcp
* -u 列出所有udp
* -l 只显示监听端口
* -n 以数字形式显示地址和端口号
* -p 显示进程的pid和名字
```bash
netstat -t
netstat -ntlp
# 列出所有网络端口信息
netstat -a                      
# 列出所有tcp连接信息
netstat -at   
# 列出所有udp连接信息
netstat -au 
# 所有端口数据包统计信息 
netstat -s
# 显示核心路由信息 
netstat -r
# 或
route -n
route print # windows
# 显示网络接口列表
netstat -i
# 显示网络接口详细信息
netstat -ie
# 或
ifconfig
```
### 列出所有网卡信息
```bash
# 查看所有网卡信息
ifconfig  -a
ip link
netstat -i

# 查看某一个网卡
ifconfig 网卡名字 
```
## 路由配置
```bash
# ipv4
route add/del -net 192.168.0.0/24 netmask 255.255.255.0 gw 192.168.0.1
route add/del -host 192.168.1.1 dev eth1
route add -net 23.23.23.0 netmask 255.255.255.0 reject # 屏蔽一条路由
route add/del default gw 192.168.0.1 #增加/删除默认网关
# ipv6
ip -6 route add default via fe80::290:4cff:fe88:8888 dev eth1 # 配置默认网关
ip -6 route add 2001:db8:3333::/64 via fe80::ca3a:35ff:fe09:efa1 dev eth1 # 添加目的网络为2001:db8:3333::/64，下一跳网关为fe80::ca3a:35ff:fe09:efa1的静态路由
```

## 查看路由表
```bash
route -n
route -4 -n
route -6 -n
ip -6 route show default # 查看默认路由网关
```

## 禁用启用网卡
```bash
ifconfig eth1 up
ifconfig eth1 down
```

## 释放、更新地址
```bash
# ipv4
dhclient -r eth1
dhclient -v eth1
# ipv6
dhclient -6 -r eth1 //释放ipv6地址 
dhclient -6 //重新获取ipv6地址
```
重启网络：
```shell
systemctl restart network
```

## 添加、删除IP地址

```bash
# 添加IPv4地址
ifconfig eth1 192.168.1.200 netmask 255.255.255.0
ip addr add 192.168.1.200/24 dev eth1
# 添加IPv6地址
ip -6 addr add 2001:db8:1111::20 dev eth1
# 删除IPv6地址
ip -6 addr del 2001:db8:1111::20 dev eth1
ip addr del 192.168.1.200/24 dev eth1

# 激活/禁用设备
ifconfig eth0 up
ifconfig eth0 down
```

## 修改MAC地址
```bash
ifconfig eth1 hw ether MAC地址 up
```
## 设置MTU值
```bash
ifconfig eth1 mtu 1500 up
```
## 配置arp信息
```shell
# arp缓存
arp -a

# 删除arp
arp -d IP

# 添加arp
arp -s IP MAC       
```

## 设置无线网络
```bash
# 安装
sudo apt install wireless-tools
# 开启无线网卡wlan0
ifconfig wlan0 up
# 设置密码
iwconfig wlan0 key 12345678
# 设置SSID
iwconfig wlan0 essid "test"
# 加入无线网
iwconfig wlan0 ap auto
# 查看网卡信息
iwconfig wlan0
# 为无线网卡指定IP地址
ifconfig wlan0 192.168.1.30 netmask 255.255.255.0  
# 用dhclient或dhcpcd获取ip
dhclient wlan0
# 或
dhcpcd wlan0

```
iwconfig 的弊端是只支持WEP认证方式，要想支持WPA，需要wpa_supplicant工具，wpa_supplicant支持4种认证方式：OPEN，WEP，WPA，WPA2







