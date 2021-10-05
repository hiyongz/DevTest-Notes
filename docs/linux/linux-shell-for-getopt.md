# Linux Bash之getopt命令行参数解析
Unix shell 中内置了命令行参数解析函数getopts，但它仅支持简单的参数解析，不支持长参数，getopt是getopts的增强版，支持长参数。在[Python笔记：命令行参数解析](https://hiyongz.github.io/posts/python-notes-for-getopt/)中介绍了Python中的命令行参数解析方法getopt()，本文介绍shell中如何使用getopt进行命令行参数解析。

<!--more-->

先看下面脚本(test_getopt.sh)：
```bash
#!/bin/bash

FIELD=unset
DF=unset
COUNT=unset
green='\033[32m'

help()
{
  Usage="Usage: sh test_getopt.sh [OPTION]  \n\
  Options:\n\
        [ -f | --field FIELD]  \t\t-- 字段 \n \
        [ -Y | --display-filter DF] \t-- 条件 \n \
        [ -c | --count COUNT ]  \t-- 计数 \n \
        [ -h | --help ]  \t\t-- 帮助信息  \n \
        "
  echo -e ${green} $Usage
  exit 2
}

ARGS=$(getopt -a -n test_getopt.sh -o f:Y:ch --long field:,display-filter:,count,help -- "$@")
VALID_ARGS=$?
if [ "$VALID_ARGS" != "0" ]; then
  help  
fi

eval set -- "$ARGS"
while :
do
  case "$1" in
    -f | --field)            FIELD="$2"   ; shift 2  ;;
    -Y | --display-filter)   DF="$2"      ; shift 2  ;;
    -c | --count)            COUNT=2      ; shift    ;;
    -h | --help)             help; exit 0 ; shift    ;;    
    --) shift; break ;;
  esac
done

echo "FIELD   : $FIELD"
echo "DF   : $DF "
echo "COUNT : $COUNT"
echo "其余参数: $@"

exit 0
```
下面对脚本进行简要解释：
1. 在开头可以定义脚本的全局变量，green用于设置字体颜色。

2. help()函数用于显示帮助信息，说明脚本的使用方法。

3. `ARGS=$(getopt -a -n test_getopt.sh -o f:Y:ch --long field:,display-filter:,count,help -- "$@")`
    - 短参数一般在前面加单破折号(`-`)，长参数使用双破折号(`--`)，`-a`选项可以使长参数支持单破折号(`-`)
    - 如果参数必须赋值，在后面加冒号(`:`)，
    - `-n test_getopt.sh`：指定程序名为test_getopt.sh，如果不设置，默认使用getopt
    - `-o | --options`：短选项
    - `-l | --longoptions`：长选项

4. getopt接收所有输入后会返回一个状态码，0表示成功，其他值表示失败，状态码会传递给变量`$?`，对变量`$?`做一个判断，如果不为0则打印帮助信息。

5. `eval set -- "$ARGS"`：
    - eval 命令把字符串当做命令来执行，这里用于处理参数中的转义字符。
    - set 命令将命令行参数替换成getopt格式化后的命令行参数，也就是将getopt格式化的参数分配至位置参数（$1,$2,...)

6. 接下来就是对参数（$1,$2,...)进行遍历处理
    - 通过shift来移动获取参数，用它来实现移动一个或者多个位置（也就是弹栈）
    - 每次循环，检查`$1`参数，对于必须赋值的参数，需要移动两位，因为它后面跟了一个参数值，需要移动两位才能到下一个参数。取值为`$2`，因为第一个参数为选项名称，第二个参数才是参数值。
    - 移位到`--`后，表示所有参数解析完成，退出循环。

运行：
```sh

$ sh test_getopt.sh --help
 Usage: sh test_getopt.sh [OPTION]
 Options:
 [ -f | --field FIELD]          -- 字段
 [ -Y | --display-filter DF]    -- 条件
 [ -c | --count COUNT ]         -- 计数
 [ -h | --help ]                -- 帮助信息
$ 
$ sh test_getopt.sh -c -f test -Y hello test2
FIELD   : test
DF   : hello
COUNT : 2
其余参数: test2
```




