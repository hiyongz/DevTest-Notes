# Linux三剑客grep、awk和sed介绍
grep，sed 和 awk是Linux/Unix 系统中常用的三个文本处理的命令行工具，称为文本处理三剑客。本文将简要介绍这三个命令并给出基本用法。<!--more-->

## 管道

在介绍这两个命令之前，有必要介绍一下Unix/Linux中管道（pipe）的概念。管道将一个命令/程序/进程的输出发送到另一个命令/程序/进程，以进行进一步处理。是一种进程间通信机制，使用管道符"|”将两个命令隔开，管道符左边命令的输出就会作为管道符右边命令的输入。
![](linux-shell-programming-grep-sed-awk/pipe.png)
管道实现了数据在多个命令之间传递，不需要创建临时文件来传递，它是单向的，数据通过管道从左向右流动。

实例1：
`cat test.txt | grep test1`

```bash
$ cat test.txt | grep test1
test1
test111
test3 test1
test111
$ cat test.txt | grep test1 | grep test3
test3 test1
$
```
实例2：
```bash
$ cat test.txt | head -3
test1
test2
test3
$ cat test.txt | tail -5
test
test

test
rrrr
$ 
```

## grep
### 定义

grep(Global Regular Expression Print) 命令用于搜索文件的特定模式，它不能增加、修改、删除文本内容，通常用于搜索过滤文本，显示被模式匹配到的行。使用正则表达式进行文本匹配（正则表达式参考文章《[Python正则表达式](https://blog.csdn.net/u010698107/article/details/111568817)》），它的使用权限是所有用户。

命令形式：
`grep [OPTIONS] PATTERN [FILE...]`
* 扩展正则表达式（egrep）添加 `-E` 参数：`grep -E [OPTIONS] PATTERN [FILE...]`
* `-P`参数可以让grep使用perl的正则表达式语法

### 选项参数
* -v 或 --invert-match ： 显示不被 pattern匹配到的行
* -n 或 --line-number ： 显示匹配的行号
* -o 或 --only-matching ：仅显示匹配到的字符串
* -c 或 --count ： 统计匹配的行数
* -i 或 --ignore-case ：忽略字符大小写
* -m或--max-count：`-m 1` : 匹配到1行后停止匹配
* -A<显示行数> 或 --after-context=<显示行数> : 除了显示符合范本样式的那一列之外，并显示该行之后的内容。
* -B<显示行数> 或 --before-context=<显示行数> : 除了显示符合样式的那一行之外，并显示该行之前的内容。
* -C<显示行数> 或 --context=<显示行数> : 除了显示符合样式的那一行之外，并显示该行之前和之后的内容。

or操作：
* `grep 'pattern1\|pattern2'`
* `grep -E 'pattern1|pattern2'`
* `egrep 'pattern1|pattern2'`


### 实例1：查找文件内容，显示行号
查找文件内容包含'test1'的行，显示行数
```bash
$ grep -n test1 test.txt 
1:test1
7:test111
9:test3 test1
11:test111
$ grep -o test1 test.txt  
test1
test1
test1
test1
$ grep -no test1 test.txt
1:test1
7:test1
9:test1
11:test1
```

### 实例2：查找文件内容，不包含test1的行

```bash
$ grep -nv test1 test.txt
2:test2
3:test3
4:test4
5:test5
6:test6
8:test2
10:test
```

### 实例3：grep 正则表达式
查找test1开头的行
```bash
$ grep -n ^test1 test.txt
1:test1
7:test111
11:test111
```

查找以1结尾的行
```bash
$ grep -n 1$ test.txt    
1:test1
7:test111
9:test3 test1
11:test111
```

### 实例4：判断或者提取数字
提取文本中的数字
```sh
$ cat test.txt
test123
456test
66
$ grep -Eo '[0-9]{1,}' test.txt
123
456
66
$ grep -o '[[:digit:]]*' <<< cat test.txt
123
456
66
$ cat test.txt | grep -o '[[:digit:]]*'
123
456
66
```
打印全为数字的行：
```sh
$ grep -Eo '^[0-9]{1,}*$' test.txt
66
$ grep -o '^[[:digit:]]*$' <<< cat test.txt
66
$ cat test.txt | grep -o '^[[:digit:]]*$'
66
```
判断某个变量是否为数字：
```sh
$ num='123'
$ grep '^[[:digit:]]*$' <<< $num
123
```

### 查看进程
```bash
$ ps -aux | grep chrome
root       5425  0.4  1.8 869280 34200 pts/0    Sl   Dec22  11:31 /opt/google/chrome/chrome --no-sandbox
root       5439  0.0  0.0 563592  1132 pts/0    S    Dec22   0:00 /opt/google/chrome/chrome --type=zygote --no-zygote-sandbox --no-sandbox
root       5440  0.0  0.1 563592  2836 pts/0    S    Dec22   0:06 /opt/google/chrome/chrome --type=zygote --no-sandbox
root       5441  0.0  0.0  26452   208 pts/0    S    Dec22   0:00 /opt/google/chrome/nacl_helper --no-sandbox
root       5442  0.0  0.0  26452   144 pts/0    S    Dec22   0:00 /opt/google/chrome/nacl_helper --no-sandbox
```

## sed
### 定义
sed（Stream Editor）是一种流编辑器，一次处理一行内容，将行存储在模式空间（临时缓冲区），然后用sed命令处理模式空间中的内容，处理完成后将内容送入屏幕，然后清除模式空间，继续读入下一行，执行下一个循环，直到文件末尾。这个过程中不会改变文件内容（除了 `-i` 选项）。

命令形式：
`sed [选项] [sed命令] [-f <script FILE>] [FILE]`
查看帮助文档：
```bash
man sed
sed -h
```

### 选项
* -h： 显示帮助信息
* -n： 仅显示 script处理后的结果，常与sed命令p连用：`sed -n 'p' test.txt` 打印test.txt文件内容
* -e：直接在指令列模式上进行 sed 的动作编辑，不修改原文件，输出到终端
* -i：修改文件内容，而不输出到终端
* -f filename ： sed 动作写在filename 内，执行 filename 内的sed 动作
* -r∶扩展正规表达式

### 常用命令
* a：append，新增： `sed -e '4 a newline' test.txt` 
* c：change，取代： `sed -e '2,5c No 2-5 number' test.txt` 
* d：delete，删除： `sed -e '2,5d' test.txt` 
	* `sed -e '/^$/d' test.txt`：删除test.txt文件空行
* i：insert，插入： `sed -e '2i newline' test.txt` 
* p：print，打印：`sed -n 'p' test.txt`
* s：substitute，替换：` sed -e 's/old/new/g' test.txt`
	* `sed -e 's/$/%/' test.txt`：在每行末尾添加%
	* `sed -e 's/ *//g' test.txt`： 删除test.txt文件空格
	* `sed -e "4s;old;new;g" test.txt` 或者 `sed -e '4s/old/new/g' test.txt`：替换第4行
* N：将下一行添加到pattern space中，将当前读入行和用N命令添加的下一行看成“一行”

注意：
1. 在替换操作中，替换时用的分割符 '/' 可以使用其它符号代替，特别是替换的内容中有 '/' 时，可以使用@、#、%等符号代替。
2. grep和sed命令的正则表达式中不支持 `\d` ,可使用如下方式匹配数字：
	* `sed -re 's/[0-9]+//g' test.txt`
	* `egrep '[0-9]+' test.txt` 或 ` grep -E '[0-9]+' test.txt`


### 实例1：打印并输出数据
打印并输出第5行数据
```bash
$ sed -n '5p' test.txt
test5
$ cat -n test.txt | sed -n '5p' 
     5	test5
$ 
```
打印并输出第3-5行数据
```bash
$ sed -n '3,5p' test.txt
test3
test4
test5
```
取反，不选择第3到5行数据
```bash
$ sed -n '3,5!p' test.txt
test1
test2
```
隔行输出
```bash
$ sed -n '1~2p' test.txt
test1
test3
test5
$ sed -n '1~3p' test.txt
test1
test4
$ 
```

### 实例2：将匹配的行数据输出到指定文件

```bash
$ 累加
sed -n '1~2p' test.txt >> a.log
$ 覆盖
sed -n '1~3p' test.txt > a.log 
```

```bash
$ sed -n '1~2p' test.txt>> a.log
$ cat a.log
test1
test3
test5
$ sed -n '1~3p' test.txt > a.log 
$ cat a.log
test1
test4
$ 
```

### 实例3：新增、插入字符串
在第2行后加上 newLine
```bash
$ sed '2 a newline' test.txt
test1
test2
newline
test3
test4
test5
$ 
```
在第2行前加上 newline
```bash
$ sed '2 i newline' test.txt
test1
newline
test2
test3
test4
test5
```

### 实例4：删除匹配到的行或者匹配行后的n行 
介绍两种方法来删除某一行的内容，一种是使用替代（substitute）的方法：
删除匹配到test3的那一行
```bash
$ sed -e 's/test3.*//g' test.txt
test1
test2

test4
test5
```
删除匹配行及后一行
```bash
$ sed -e 'N;s/test3.*//g' test.txt
test1
test2

test5
```
这种方法会留一个空行，可以进一步使用命令`sed -e '/^$/d' test.txt`命令删除空行。


第二种方法是使用删除（delete）命令：
```bash
$ sed -e '/test3.*/d' test.txt
test1
test2
test4
test5
```
也可以删除匹配到的行及匹配行后的n行 
```bash
$ sed -e '/test2.*/,+2d' test.txt
test1
test5
```


### 实例5：全局替换

将所有的test2替换为test222
```bash
$ sed -e 's/test2/test222/g' test.txt
test1
test222
test3
test4
test5
$ sed -e 's/test2/test222/' test.txt
test1
test222
test3
test4
test5
```
替换某一行：替换test1开头的所在行
test2.txt内容：
```sh
$ cat test2.txt
hello world !
test1 test2 test2
test1
test2
test3 
```

```sh
# 方法1：c参数，替换某一行
$ sed "2c hello" test2.txt
hello world !
hello
test1
test2
test3 
$ sed "3c hello" test2.txt
hello world !
test1 test2 test2
hello
test2
test3 
# 方法2：s参数替换
$ sed 's/^test1.*$/hello/' test2.txt
hello world !
hello
hello
test2
test3 
```

### 实例6：修改文件
前面的新增、替换操作都没有改变文件内容，如果要使文件修改生效，需要使用 `-i` 选项。
```bash
$ sed -i 's/test2/test222/' test.txt
$ cat test.txt 
test1
test222
test3
test4
test5
$ 
```

### 实例7：横向连接
将匹配到的对象横向连接

比如我们需要杀掉某个服务有多个进程：
```sh
[root@Server ~]# ps -ef | grep named | grep -v grep
root       7136      1  0 1月22 ?       00:00:54 /var/bin/named -c /var/named/named.conf
root       7690      1  0 1月21 ?       00:01:02 /var/bin/named -c /var/named/named.conf
```
使用命令 `kill -9 7136 7690`来杀掉这两个进程，使用如下命令实现连接这两个进程的ID：
```sh
kill -9 $(ps -ef | grep named | grep -v grep | awk '{print $2}') | sed ':1;N;s/\n/ /g;t1'
```
关键命令为 `sed ':1;N;s/\n/ /g;t1'`，将换行替换为空格。

## awk
### 定义
awk是一种文本模式扫描和处理的编程语言，由 Aho, Weinberger 和 Kernighan开发。awk功能强大，可用于数据提取和统计，常用在shell脚本中。awk逐行读入文件，以空格为默认分隔符将每行切片，切开的部分再进行后续处理。

命令形式：
`awk [options] 'pattern action' [FILE(s)]`

* pattern：正则表达式
* action：对匹配到的内容执行的命令(默认为输出每行内容)

### 常用参数
* **$0**： 整条记录（当前行）
* **\$1 - \$​n**： 表示当前行的第n个域
* **FILENAME**： awk浏览的文件名
* **BEGIN**： 处理文本之前要执行的操作
* **END**： 处理文本之后要执行的操作
* **FS**： 设置输入域分隔符，等价于命令行 `-F` 选项，默认为空格“ ”
	* `awk -F: '{print $1}' test.txt` 
	* 或者 `awk 'BEGIN {FS = ":"} {print $1}' test.txt`
* **NF**： 浏览记录的域的个数/列数
* **NR**： 已读的记录数/行数
*  **FNR**： 当前输入文件的记录数
* **OFS**： 输出域分隔符，默认为空格“ ”
* **ORS**： 输出记录分隔符，默认为“\n”
* **RS**： 控制记录分隔符
* **exit**：匹配到第一行内容后退出：`awk -F: '{print $2;exit}' test.txt` ，grep使用 `-m` 参数

### 实例1：查找、打印
搜索/etc/passwd有root关键字的所有行
```bash
$ awk -F : '/root/ {print $0}' /etc/passwd
root:x:0:0:root:/root:/bin/bash
operator:x:11:0:operator:/root:/sbin/nologin
$
$ awk -F : '/root/ {print $7}' /etc/passwd
/bin/bash
/sbin/nologin
```
打印etc/passwd/的第二行信息
```bash
$ awk -F : 'NR==2 {print $0}' /etc/passwd
bin:x:1:1:bin:/bin:/sbin/nologin
$
```

### 实例2：BEGIN、END制表
使用 begin加入标题
```bash
$ awk -F : 'BEGIN {print "No", "User", "Auth"} {print NR "|" $1 "|" $2} END {print FILENAME}' /etc/passwd
No User Auth
1|root|x
2|bin|x
3|daemon|x
4|adm|x
5|lp|x
6|sync|x
7|shutdown|x
8|halt|x
9|mail|x
.................
28|nscd|x
29|exim|x
/etc/passwd
```

### 实例3：自定义分割符
```bash
$ echo "123|456|789"
123|456|789
$ echo "123|456|789" | awk 'BEGIN{RS="|"}{print $0}'
123
456
789
```

## 综合实例
### 找出log中的404 500的报错有多少条
```bash
$ grep -E ' 404 | 500 ' nginx.log | wc -l
267
$ grep -P ' 404 | 500 ' nginx.log | wc -l
267
$ grep -Pc ' 404 | 500 ' nginx.log  
267

$ awk '$9~/404|500/' nginx.log | wc -l    # {print}省略
267
$ awk '$9~/404|500/{print}' nginx.log | wc -l
267
```
- $9表示查找第9列
- 波浪号～表示用来匹配后面的正则表达式，告诉awk后面开始是正则语法。
- `wc -l` ：和`-c`参数一样，统计匹配到的行数

### 访问量最高的ip
#### 使用awk命令查找
```bash
$ awk '{print$1}' nginx.log | sort | uniq -c | sort -nr | head -3
    282 216.244.66.241
    130 136.243.151.90
    110 127.0.0.1

$ awk '{print$1}' nginx.log | sort | uniq -c | sort -nr | head -3 | awk '{print $2}'
216.244.66.241
136.243.151.90
127.0.0.1
```
sort命令用于排序：
- `-r`：sort默认为升序，`-r`参数表示降序
- `-n`：以数值来排序，如果不使用这个参数就会出现10比2小的情况，因为把10当做字符来进行比较了。

uniq 命令用于检查及删除文本文件中重复出现的行列，一般与 sort 命令结合使用
- `-c`：在每列旁边显示该行重复出现的次数

head命令用于查看文件的开头部分的内容


#### 使用grep查找
```bash
$ grep '^[0-9]*.[0-9]*.[0-9]*.[0-9]*' nginx.log    #其中的点“.”为正则语法，表示匹配任意字符
123.127.112.18 - - [05/Dec/2018:00:09:18 +0000] "GET /cable HTTP/1.1" 101 1017 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36" 70.577 70.577 .
139.180.132.174 - - [05/Dec/2018:00:09:20 +0000] "GET /bbs.zip HTTP/1.1" 404 1264 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36" 0.011 0.011 .
139.180.132.174 - - [05/Dec/2018:00:09:12 +0000] "GET /__zep__/js.zip HTTP/1.1" 500 2183 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36" 0.018 0.018 .

$ grep -o '^[0-9]*.[0-9]*.[0-9]*.[0-9]*' nginx.log
216.244.66.241
223.71.41.98
113.87.161.17
216.244.66.241
216.244.66.241
144.76.81.72
............
$ grep -o '^[0-9]*.[0-9]*.[0-9]*.[0-9]*' nginx.log | wc -l
2000
$ grep -o '^[0-9]*.[0-9]*.[0-9]*.[0-9]*' nginx.log | sort | uniq -c | sort -nr |head -3   
    282 216.244.66.241
    130 136.243.151.90
    110 127.0.0.1
  ......................
$ 
```

### 将 topics 后面的数字替换成numer
```bash
$ grep 'topics' nginx.log | sed 's#topics/[0-9]*#topics/number#g' 

```

### 将ip地址横向打印
```bash
[root@centos7 tmp]# awk '{print $1}' nginx.log | sed ':1;N;s/\n/|/g;t1'  
216.244.66.241|216.244.66.241|216.244.66.241|216.244.66.241|216.244.66.241|216.244.66.241|216.244.66.241|223.71.41.98|113.87.161.17|216.244.66.241|216.244.66.241|144.76.81.72
```
* `# :1` ：标记  t1
* `;`：把不同的命令分开


## 参考资料
1. 正则表达式30分钟入门教程：[https://deerchao.cn/tutorials/regex/regex.htm](https://deerchao.cn/tutorials/regex/regex.htm)
2. [Python正则表达式](https://blog.csdn.net/u010698107/article/details/111568817)



