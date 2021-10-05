# Linux和Windows创建指定大小文件方法
在测试中有时需要创建不同大小的测试文件，用于测试上传下载性能以及以及其它文件传输功能，本文介绍几种Liunx和Windows系统下创建指定大小文件的方法。

<!--more-->

## Linux系统创建指定大小文件

下面介绍的dd 、fallocate和truncate命令包含于GNU coreutils软件包中，不需要单独安装。


### dd命令
dd (device driver) 命令常用来复制备份文件，与cp命令具有以下区别：
- dd是对块进行操作，操作磁盘的扇区字节，
- cp操作文件或目录，对于不能以文件或目录格式呈现的数据cp无法复制。
- dd是对磁盘连续的读取，也就是完全的数据搬移，cp复制的数据排列不是按顺序的。

也可以使用这个命令来创建特定大小的文件。
```sh
root@Server ~]# dd if=/dev/urandom of=testfile10MB_dd bs=10MB count=1
记录了1+0 的读入
记录了1+0 的写出
10000000字节(10 MB)已复制，0.124436 秒，80.4 MB/秒
root@Server ~]# ll testfile10MB_dd
-rw-r--r--   1 root    root    10000000 7月   7 11:56 testfile10MB_dd
[root@Server ~]# du testfile10MB_dd
9768    testfile10MB_dd
```
`/dev/urandom`用于生成随机数据，也可以使用`/dev/zero`来生成全0的文件：
```sh
[root@Server ~]# dd if=/dev/zero of=testfile10MB_dd0 bs=10MB count=1
记录了1+0 的读入
记录了1+0 的写出
10000000字节(10 MB)已复制，0.00799675 秒，1.3 GB/秒
[root@Server ~]# ll testfile10MB_dd0
-rw-r--r--   1 root    root    10000000 7月   7 13:57 testfile10MB_dd0
[root@Server ~]# od -c testfile10MB_dd0
0000000  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0
*
46113200
[root@Server ~]# 
```

> **/dev/urandom、/dev/random以及/dev/zero、/dev/null介绍**：
>
> - /dev/urandom和/dev/random都可以产生随机的ASCII码字符流，其中/dev/random依赖系统中断，当系统中断不足时，/dev/random设备会“挂起”。/dev/urandom不依赖系统中断，所以在生成特定大小文件时一般使用/dev/urandom，不使用/dev/urandom。 
> - /dev/zero “零”设备可以无限的提供空字符，产生二进制的零流
> - /dev/null “空”设备，像”黑洞“一样，所有写入它的内容都会永远丢失，也不会读取到任何内容。常用于禁止标准输出和标准错误的输出，比如抓包命令：`tcpdump -i eth1 -w /tmp/packet.pcap  >/dev/null &`


根据/dev/urandom的特性，也可以结合head命令来创建指定大小的文件：
```sh
head -c 10MB /dev/urandom > testfile10MB
# 或者
head -c 10MB /dev/zero > testfile10MB
```

`bs`参数和truncate命令的size参数类似，默认单位为bytes，也支持以下单位：
- c =1 bytes, w =2 bytes, b =512 bytes
- K, M, G, T, P, E, Z, Y（幂底数为1024 bytes，如5M=5×1024×1024）
- KB, MB, GB ...（幂底数为1000 bytes，如5MB=5×1000×1000）


### fallocate命令
fallocate用于创建大文件（大于2G）：
```sh
[root@Server ~]# fallocate -l 2G testfile2G_fal
[root@Server ~]# ll testfile2G_fal
-rw-r--r--   1 root    root    2147483648 7月   7 14:01 testfile2G_fal
```
`-l`参数指定文件大小，默认单位为bytes，也可以指定单位：K, M, G, T, P, E, Z, Y以及KB, MB, GB等

### truncate命令
truncate命令也可以用来创建指定大小的文件，下面创建一个10 MB大小的文件
```sh
[root@Server ~]# truncate -s 10M testfile10M
[root@Server ~]# ll testfile10M
-rw-r--r--   1 root    root    10485760 7月   7 10:45 testfile10M
[root@Server ~]# 
[root@Server ~]# truncate -s 10MB testfile10Mb
[root@Server ~]# ll testfile10Mb
-rw-r--r--   1 root    root    10000000 7月   7 10:49 testfile10Mb
```

`-s | --size`参数 用于指定要生成的文件大小，单位可以是：
- K, M, G, T, P, E, Z, Y（幂底数为1024 bytes，如5M=5×1024×1024）
- KB, MB, GB ...（幂底数为1000 bytes，如5MB=5×1000×1000）

### dd 、fallocate和truncate的区别
truncate命令生成的是空洞文件，并不占用实际的磁盘空间，文件中间是用“\0”填充的，实际占用的空间为0。使用du命令查看truncate生成文件占用的磁盘空间：
```sh
[root@Server ~]# ll testfile10Mb
-rw-r--r-- 1 root root 10000000 7月   7 14:30 testfile10Mb
[root@Server ~]# du -sh testfile10Mb
0       testfile10Mb
[root@Server ~]# od -c testfile10Mb
0000000  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0
*
46113200
[root@Server ~]# 
```
fallocate命令为文件预分配物理空间，分配的空间在磁盘的扇区上是连续的，生成的不是空洞文件，不是空洞文件那样“假装”占有那么多空间：
```sh
[root@Server ~]# ll testfile2G_fal
-rw-r--r-- 1 root root 2147483648 7月   7 14:01 testfile2G_fal
[root@Server ~]# du -sh testfile2G_fal
2.0G    testfile2G_fal
```
可以看到，和truncate不一样，用fallocate生成的文件在磁盘上确实占用了2.0G的空间。

dd命令生成的文件也不是空洞文件，使用它来生成大文件时速度较慢，而且使用dd以及提到的head命令生成文件时会进行大量IO操作，所以在Linux中生成文件时，建议使用fallocate命令。

## Windows系统创建指定大小文件

### fsutil工具

Windows中可以使用fsutil工具生成文件，命令语法格式如下：
```bash
fsutil file createNew test.txt 1024 # 文件大小单位为bytes
```

以管理员身份打开cmd，创建一个5M bytes的文件：5×1024×1024=5242880 bytes
```sh
C:\Users\DELL> fsutil file createNew test.txt 5242880
File C:\Users\DELL\test.txt is created
C:\Users\DELL> dir test.txt | findstr test.txt
2021/07/07  15:26         5,242,880 test.txt
```





