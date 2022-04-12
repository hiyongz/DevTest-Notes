# Linux安装和配置SVN服务器
本文记录在centos7系统上搭建SVN服务器步骤。

<!--more-->


## 离线安装SVN

**1、下载安装包**

subversion-1.14.1.tar.gz：http://subversion.apache.org/download/

sqlite-autoconf-3140000.tar.gz：http://www.sqlite.org/download.html（数据库依赖包）

apr-1.7.0.tar.gz，apr-util-1.6.1.tar.gz：http://apr.apache.org/download.cgi

zlib-1.2.11.tar.gz：http://linux.softpedia.com/get/Programming/Libraries/zlib-159.shtml

**2、安装apr-1.7.0.tar.gz**

```bash
$ tar -xzvf apr-1.7.0.tar.gz
$ cd apr-1.7.0/
$ ./configure --prefix=/opt/svn/apr-1.7.0
```

如果报如下错误：
```bash
configure: error: no acceptable C compiler found in $PATH
```

需要安装gcc编译器，下载gcc包及依赖包：http://mirrors.aliyun.com/centos/7/os/x86_64/Packages/
```bash
mpfr-3.1.1-4.el7.x86_64.rpm
libmpc-1.0.1-3.el7.x86_64.rpm

kernel-headers-3.10.0-123.el7.x86_64.rpm
glibc-headers-2.17-55.el7.x86_64.rpm
glibc-devel-2.17-55.el7.x86_64.rpm
cpp-4.8.2-16.el7.x86_64.rpm
gcc-4.8.2-16.el7.x86_64.rpm
```

安装：

```bash
$ rpm -Uvh *.rpm --nodeps --force
```

然后重新安装apr

如果报错：rm: cannot remove 'libtoolT': No such file or directory

解决方案： configure文件，注释掉 \$RM "$cfgfile" ，然后重新编译安装。

**3、安装apr-util**

```bash
$ tar -xvzf apr-util-1.6.1.tar.gz 
$ cd apr-util-1.6.1
$ ./configure --prefix=/opt/svn/apr-util-1.6.1 --with-apr=/opt/svn/apr-1.7.0
$ make
$ make install
```

**4、安装subversion**

```bash
$ tar -xvzf subversion-1.14.1.tar.gz
$ cd subversion-1.14.1
$ ./configure --prefix=/opt/svn --with-apr=/opt/svn/apr-1.7.0 --with-apr-$ util=/opt/svn/apr-util-1.6.1
```

**5、安装sqlite-amalgamation**

下载地址：[https://www.sqlite.org/download.html](https://www.sqlite.org/download.html)

**6、安装zlib**

下载地址：[http://zlib.net/](http://zlib.net/)

```bash
$ tar -zxvf zlib-1.2.11.tar.gz
$ cd zlib-1.2.11
$ ./configure --prefix=/usr/local/zlib
$ cd subversion-1.14.1
$ ./configure --prefix=/opt/svn --with-apr=/opt/svn/apr-1.7.0 --with-apr-util=/opt/svn/apr-util-1.6.1 --with-zlib=/usr/local/zlib
```

**7、添加环境变量**

```bash
$ SVN_HOME=/opt/svn
$ export PATH=$PATH:$SVN_HOME/bin
$ source /etc/profile  # 刷新设置
$ echo $PATH # 查看设置是否生效
```

## 在线安装SVN

使用`svn --version` 命令查看SVN是否已经安装。

或者

```bash
$ rpm -qa subversion
subversion-1.14.1-1.x86_64
```

如果没有安装，使用yum命令安装：

```bash
$ yum install -y subversion
```

## 升级SVN版本

将svn从1.7版本升级到svn-1.14

配置svn的yum源
```bash
tee /etc/yum.repos.d/wandisco-svn.repo <<-'EOF'
[WandiscoSVN]
name=Wandisco SVN Repo
baseurl=http://opensource.wandisco.com/centos/7/svn-1.14/RPMS/$basearch/
enabled=1
gpgcheck=0
EOF
```

清理下本地的yum缓存
```bash
$ yum clean all
```

安装svn
```bash
$ yum install -y subversion
```

## 创建SVN版本库

建立SVN版本库：

```bash
$ mkdir /home/svn
$ mkdir -p /home/svn/project
$ svnadmin create /home/svn/project
```

执行完上面的命令后，project目录下会生成配置文件：

```bash
$ cd /home/svn/project
$ ls
conf  db  format  hooks  locks  README.txt
```

进入 `conf` 目录，配置svnserve.conf、passwd 和 authz。

```bash
$ vi svnserve.conf
[general]
anon-access = read
auth-access = write
password-db = passwd
authz-db = authz

$ vi passwd
[users]
admin = admin

$ vi authz
[groups]
g_admin = admin

[/]
@g_admin = rw
* = r
```

启动svn服务

```bash
$ svnserve -d -r /home/svn
```

## Windows安装SVN客户端

下载安装版本控制客户端[TortoiseSVN](https://tortoisesvn.net/about.zh.html)，下载地址：[https://tortoisesvn.net/downloads.zh.html](https://tortoisesvn.net/downloads.zh.html)

下载完成后，双击msi文件安装，安装完成后，使用TortoiseSVN来访问SVN版本库： svn://192.168.100.24/project

如果无法访问，可能原因是防火墙问题。

关闭防火墙服务：
```bash
$ systemctl stop firewalld
```
禁止防火墙开机自启
```bash
$ systemctl disabled firewalld
```


