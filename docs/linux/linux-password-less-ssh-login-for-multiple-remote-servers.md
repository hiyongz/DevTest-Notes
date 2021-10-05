# 配置多台服务器之间ssh免密登录
使用scp 或者 rsync命令在多台Linux服务器之间同步文件时需要输入密码，除了使用expect实现自动化交互以外，还有一种方法就是配置服务器之间ssh免密登录，本文记录一下具体配置过程。

<!--more-->


## 1. 创建.ssh目录

假定有3台Linux主机，分别为A，B，C

在所有主机上创建ssh目录并赋予权限
```sh
mkdir /root/.ssh 
chmod 700 /root/.ssh
```

## 2. 生成公钥与私钥

所有主机生成公钥与私钥，执行以下命令：

```sh
$ cd ~  # 进⼊入用户目录
$ ssh-keygen -t rsa -P ""  # 生成ssh密码，-t 参数表示生成算法，可以选择rsa和dsa；-P表示使用的密码，""表示无密码。

```

## 3. 将公钥追加authorized_keys文件中

将第一台主机A上生成公钥追加到authorized_keys文件中

```sh
$ cd ~/.ssh  # 进入.ssh目录
$ cat id_rsa.pub >> authorized_keys   # 将id_rsa.pub的内容追加到authorized_keys文件中
```

然后可以删除A上的id_rsa.pub文件，因为已经写进了authorized_keys文件中

```sh
$ rm -rf id_rsa.pub 
或者
$ mv id_rsa.pub id_rsa.pub.copy
```

接下来将B和C的id_rsa.pub写入到A的authorized_keys文件中，使用scp 或者 rsync命令分别将B和C两台机器的id_rsa.pub复制到主机A 。（scp 或者 rsync命令的使用方法可参考文章[使用SCP或Rsync实现Linux主机之间文件、目录的复制]()）

在主机B上操作 ：

```sh
$ scp id_rsa.pub hostA:~/.ssh/ # hostA为A的主机名或者A的IP地址
```

也可以直接在主机A上操作，执行如下命令：

```sh
$ scp hostB:~/.ssh/id_rsa.pub ~/.ssh/
```

在主机A上执行如下命令，将主机B的id_rsa.pub文件内容添加到authorized_keys文件中：

```sh
$ cat id_rsa.pub >> authorized_keys
$ mv id_rsa.pub id_rsa.pub.copy2
```

主机C类似，将C的id_rsa.pub文件内容添加到authorized_keys文件中。

这样authorized_keys文件里面保存了主机A，B，C的公钥，然后将authorized_keys文件拷贝到其它两台主机上就可以了：

```sh
$ scp authorized_keys hostB:/root/.ssh/
$ scp authorized_keys hostC:/root/.ssh/
```

## 4. 测试

```sh
ssh root@要进行链接的机器ip地址
```
主机A -> B：
```sh
[root@hostA ~]# ssh root@192.168.20.20
Last login: Sat Jul 10 10:17:34 2021 from hostA
[root@hostB ~]# 
```
主机B -> A：
```sh
[root@hostB ~]# ssh root@192.168.20.10
Last login: Sun Jul 11 19:54:08 2021 from hostB
[root@hostA ~]# 
```





