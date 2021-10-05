# 使用SCP或Rsync实现Linux主机之间文件、目录的复制
我们知道Linux本机的文件拷贝可以使用`cp`命令，它不能在Linux主机之间拷贝数据。本文介绍SCP和Rsync这两种实现Linux主机间的数据拷贝工具。

<!--more-->


## SCP 和 Rsync区别

SCP(secure copy) 是基于ssh协议的安全拷贝，用于将文件/目录安全地从本地主机传输到远程主机。

Rsync (remote synchronize)也可以实现同步本地主机和远程主机的文件/目录，和SCP不同之处在于，首次复制时，Rsync会复制整个目录，在后面的复制中，不会复制相同的内容，只对差异文件做更新，scp是把所有文件都复制过去。Rsync广泛用于备份和镜像。

下面介绍它们的简单使用方法。

## SCP
一般情况下Linux服务器都有scp命令，如果没有，可通过如下方式安装：
```sh
yum -y install openssh-clients # centos
apt-get install openssh-client # Ubuntu
```

### 复制文件/目录到远程主机

```sh
scp source_file_name user@destination_host:destination_folder # 复制文件
scp -r source_directory user@destination_host:destination_folder # 复制目录
```
案例1：复制文件到远程主机
```sh
[root@Client ~]# scp text.txt root@192.168.20.40:/root
The authenticity of host '192.168.20.40 (192.168.20.40)' can't be established.
ECDSA key fingerprint is SHA256:tS6tueeKp9vBLDvxgsxIgCCaGMQWs9+5E167qz2ZB9c.
ECDSA key fingerprint is MD5:82:04:10:14:57:52:0a:05:d9:9b:ae:6e:3f:3f:68:98.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.20.40' (ECDSA) to the list of known hosts.
root@192.168.20.40's password: 
test.txt                                                                                                                     100%   12     6.0KB/s   00:00    
[root@Client ~]# 
```

### 从远程主机复制文件/目录
```sh
scp user@source_host:source_file_name local_destination_folder # 复制文件
scp -r user@source_host:source_file_name local_destination_folder # 复制目录
```

案例2：从远程主机复制文件
```sh
[root@Client ~]# scp root@192.168.20.40:/root/test40.txt /root
root@192.168.20.40's password: 
test40.txt                                                                                                                   100%   12     4.2KB/s   00:00    
[root@Client ~]# ll | grep test40.txt
-rw-r--r--   1 root    root          12 7月   6 09:41 test40.txt
[root@Client ~]# 
```


`-r`参数用于递归的复制整个目录，SCP更多的参数使用方法可参考：[https://manned.org/scp.1](https://manned.org/scp.1)

### 本地文件/目录复制
如果不指定远程主机地址，可以实现和`cp`目录一样的功能：
```sh
scp source_file destination_folder # 复制文件
scp -r source_directory destination_folder # 复制目录
```
案例3：本地文件复制
```sh
[root@Client ~]# mkdir test
[root@Client ~]# scp test40.txt /root/test
[root@Client ~]# ll /root/test/
总用量 4
-rw-r--r-- 1 root root 12 7月   6 09:49 test40.txt
[root@Client ~]# 
```


## Rsync


安装方法：
```sh
yum install rsync      # centos
apt-get install rsync  # Ubuntu
```

### 选项参数
Rsync可用的选项参数很多，下面介绍几个常用参数，更多参数使用方法可参考[https://manned.org/rsync.1](https://manned.org/rsync.1) ，或者使用`rsync -h`、`man rsync`命令查看文档说明。

| 选项 | 功能         |
| ---- | ------------ |
| -t   | 将源文件的修改时间(modify time)同步到目标机器  |
| -I | --ignore-times，不跳过时间和大小都匹配的文件，也就是不检查是否有改动，直接复制 |
| -r   | 递归，用于目录复制  |
| -a   | 递归同步，还可以同步元信息（比如修改时间、权限等）  |
| -v   | 打印复制过程 |
| -l   | 拷贝符号连接 |
| --delete | 删除目标目录中多余的文件，也就是保持两个目录相同，使得目标目录成为源目录的镜像副本 |

### 复制文件/目录到远程主机
如果复制的目标目录不存在，会自动创建，语法格式和SCP一样：
```
rsync source_file_name/ user@destination_host:destination_folder # 复制文件
rsync -r source_file_name/ user@destination_host:destination_folder # 复制目录
```

案例1：复制文件、目录到远程主机
```sh
[root@Client ~]# rsync test.txt root@192.168.20.40:/root
root@192.168.20.40's password: 
[root@Client ~]# 
[root@Client ~]# rsync -rvl test/ root@192.168.20.40:/root/test222
root@192.168.20.40's password: 
sending incremental file list
created directory /root/test222
./
test2.txt
test40.txt

sent 187 bytes  received 93 bytes  62.22 bytes/sec
total size is 12  speedup is 0.04
```

### 从远程主机复制文件/目录
```sh
rsync user@source_host:source_file_name local_destination_folder # 复制文件
rsync -r user@source_host:source_file_name local_destination_folder # 复制目录
```

案例1：复制远程主机文件到本机
```sh
[root@Client ~]# rsync root@192.168.20.40:/root/test40.txt /root
root@192.168.20.30's password: 
[root@Client ~]# ll test40.txt
-rw-r--r-- 1 root root 12 7月   8 11:11 test40.txt
[root@Client ~]# 
```



### 其它用法
#### 复制指定类型的文件
仅复制py文件：
```sh
rsync *.py user@destination_host:destination_folder
```
#### 复制多个文件
```sh
[root@Client ~]# rsync test1.txt test2.txt test{5,6,7}.txt root@192.168.20.40:/root
root@192.168.20.40's password: 
[root@Client ~]# 
```
远程主机上查看是否复制成功
```sh
[root@Server ~]# ls | grep -E "test[0-9]{1}.txt"
test1.txt
test2.txt
test5.txt
test6.txt
test7.txt
[root@Server ~]# 
```


从远程主机复制多个文件（先删除本地文件）：
```sh
[root@Client ~]# rsync root@192.168.20.40:/root/test1.txt :test2.txt root@192.168.20.40:test{5,6,7}.txt /root
root@192.168.20.40's password: 
[root@Client ~]# ls | grep -E "test[0-9]{1}.txt"
test1.txt
test2.txt
test5.txt
test6.txt
test7.txt
```

### 本地文件/目录复制
和scp命令一样，rsync也可以用于在本机进行文件复制。
```sh
rsync source_file destination_folder # 复制文件
rsync -r source_directory destination_folder # 复制目录
```

## 小结
rsync工具只对差异文件做更新的特性，在多个服务器之间同步文件非常有用，通常跳过写一个自动化脚本来实现批量同步，但是，你也许已经发现了，在执行同步命令时，需要输入目标主机的密码，在主机很多的情况下就不方便了。

一种解决方案是可以使用expect实现自动化交互，另一种方法是配置服务器之间ssh免密登录，因为scp和rsync默认使用ssh协议。ssh免密登录配置方法可参考[配置多台服务器之间ssh免密登录](https://blog.csdn.net/u010698107/article/details/119079821)





