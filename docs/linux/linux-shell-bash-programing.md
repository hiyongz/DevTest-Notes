# Linux Bash编程
在《[Linux系统介绍](https://hiyongz.github.io/posts/linux-kernel-and-shell-introduce/)》中，介绍了shell的多个版本，现在的Linux发行版基本都默认使用bash（Bourne Again shell），兼容Bourne shell (sh)，本文将简要介绍Bash编程语法。<!--more-->

## 变量
### 命名规则
* 只能使用英文字母，数字和下划线，首个字符不能以数字开头
* 中间不能有空格，可以使用下划线(\_)
* 不能使用标点符号
* 不能使用bash里的关键字(可用help命令查看保留关键字)
[img](bash-help.png)

### 定义与使用变量
定义变量
```bash
your_name="abc"
echo $your_name
```
拼接字符串
```bash
your_name="world"
your_name2="hello,$your_name!"
echo $your_name2
```
数组
```bash
array_name=(value0 value1 value2 value3)
valuen=${array_name[n]} # 数组取值
array_name[0]=value0 # 赋值
length=${#array_name[@]} # 获取数组长度
```

数组实例：
```bash
my_array=(A B "C" D)
echo "第一个元素为: ${my_array[0]}"
my_array[1]=b
echo "数组的元素为:${my_array[*]}" # 打印所有元素
echo "数组的元素为:${my_array[@]}"
```
输出：
```bash
第一个元素为: A
数组的元素为:A b C D
数组的元素为:A b C D
```

### 只读变量
```bash
a="123"
readonly a
```
### 删除变量
```bash
unset variable_name #不能删除只读变量
```
不能删除只读变量
```bash
# b=10
# readonly b
# echo $b
10
# unset b
-bash: unset: b: cannot unset: readonly variable
#
```

### 环境变量
显示所有环境变量
```bash
env
# 或者
printenv
```
显示环境变量值
```bash
printenv LANG
# 或者
echo $LANG
```



## 控制语句
### 条件分支：if
### if定义
```bash
if condition
then
    command1
    command2
    ...
    commandN
fi
```
if和then写在同一行时，用分号分隔。

```bash
if [ 2==2 ]; then
	echo "true"; 
else 
	echo "false"; 
fi
```

#### 判断条件写法
```bash
# 写法一
test expression
# 写法二
[ expression ]
# 写法三
[[ expression ]]
```

```bash
if test 2==2; then	echo "true"; fi
if [ 2>1 ]; then echo "true"; fi

if [[ 2>1 ]]; then	echo "true"; fi
```
#### 实例
比较两个变量的大小
```bash
a=10
b=20
if [ $a -eq $b ]; then 
	echo"equal"; 
elif [ $a -lt $b ]; then 
	echo "small"; 
elif [ $a -gt $b ]; then 
	echo "big"; 
fi
```

### 循环：for
#### for定义
```bash
for var in item1 item2 ... itemN
do
    command1
    command2
    ...
    commandN
done
```
#### 实例
for和do写在同一行时，用分号分隔。
```bash
for Ioop in 1 2 3 4 5
do
    echo "hello"
done

for Ioop in 1 2 3 4 5;do
    echo "hello"
done
```

循环读取文件内容并输出
```bash
for i in $(cat test.txt); do echo $i; done
```

循环遍历列表
```bash
list=(value1 value2 value3)
for i in ${list[*]}; do echo $i; done
# 或者
for i in ${list[@]}; do echo $i; done
```

### 循环: while
#### while定义
```bash
while condition
do
    command
done
```
#### 实例
```bash
int=1
while(( $int<=5))
do
    echo $int
    let "int++"
done
```

循环读取文件内容并输出
```bash
while read line; do echo $line; done<test.txt
```
输出：
```bash
test1
test222
test3
test4
test5
```

## read命令
* read命令是用于从终端或者文件中读取输入的内部命令
* 读取整行输入
* 每行末尾的换行符不被读入

### read命令使用
从标准输入读取输入并赋值给变量
```bash
read var
```
从标准输入读取多个内容
```bash
read varl var2 var3
```
不指定变量(默认赋值给 REPLY)
```bash
read
```
### 实例
```bash
# read a
123
# echo $a
123
# read a b c
1 2 3
# echo $a   
1
# echo $b
2
# echo $c
3
#
```

默认变量
```bash
# read
456
# echo $REPLY
456
#
```

## 注释
```bash
# 注释
# 多行注释
:<<EOF
内容
.......
EOF
```

## 脚本参数传递
* **\$0** 脚本名称
* **\$1~\$n** 获取第n个参数：
* **\$#** 传递到脚本的参数个数
* **\$\$** 脚本运行的当前进程ID号
* **\$*** 以一个单字符串显示所有向脚本传递的参数
* **$?** 显示最后命令的退出状态。0表示没有错误,其他任何值表明有错误

vim param.sh：
```bash
#!/bin/bash
echo "脚本名称：$0"
echo "脚本运行的当前进程ID号：$$"
echo "参数个数：$#"
echo "所有参数：$*"
echo "第1个参数：$1"
echo "第10个参数：${10}"
echo "return "$?
```
执行：
```bash
# chmod +x param.sh
# ./param.sh 1 2 3 4 5 6 7 8 9 10 1        
脚本名称：./param2.sh
脚本运行的当前进程ID号：21097
参数个数：11
所有参数：1 2 3 4 5 6 7 8 9 10 1
第1个参数：1
第10个参数：10
return 0
# 
```

## 基本运算
bash会把反引号里面当作一条命令来执行
In: 

```bash
# echo `date +%y/%m/%d` 
20/12/27
# echo `expr 2 + 2`  
4
```


```bash
# a=10
# b=20
# echo expr $a + $b  
30
# echo $(($a+$b))
30
# echo expr $a - $b
-10
# echo expr $a \* $b
200
# echo expr $b / $a
2
# 
```


* %   取余
* =   赋值 a=\$b 将把变量b的值赋给a
* ==  相等 相同则返回true
* !=  不相等 不相同则返回true
```bash
# a=10
# b=20
# echo `expr $b % $a`
0
# echo $[$a == $b] 
0
# echo $[$a != $b]  
1
#
```

* -eq 检测相等
* -ne 检测不相等
* -gt 检测左边是否大于右边
* -lt 检测左边是否小于右边
* -ge 检测左边是否大于等于右边
* -le 检测左边是否小于等于右边

```bash

# vim test.sh  
# cat test.sh
#!/bin/bash
a=10
b=20
if [ $a -lt $b ]
then
        echo "equal"
fi
# chmod +x test.sh
# ./test.sh
equal
#
```
## 其它实例
### 内存统计
```bash
#!/bin/bash
# 内存使用百分比
free | sed -n '2p' | gawk 'x = int(( $3 / $2 ) * 100) {print x}' | sed 's/$/%/'

# 统计内存
for i in `ps aux | awk '{print $6}' | grep -v 'RSS'`; do
    count=$[$count+$i]
done
echo "$count/kb"
```

```bash
# ./test.sh  
16%
474608/kb
```

### 求阶乘
`vim test.sh`
```bash
read -p "Enter a number:"
factorial=1
for (( count=1; count<=$REPLY; count++))
do
	factorial=$[ $factorial * $count ]
done
echo "The factorial of $REPLY is $factorial"
```

```bash
# chmod +x test.sh
# ./test.sh 
Enter a number:6
The factorial of 6 is 720
```



