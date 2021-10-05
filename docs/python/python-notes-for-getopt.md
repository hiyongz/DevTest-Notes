# Python笔记：命令行参数解析

<!--more-->

# sys.argv
sys.argv是传入的参数列表，sys.argv[0]是当前python脚本的名称，sys.argv[1]表示第一个参数，以此类推。

```python
import sys

print(sys.argv)
print(sys.argv[0])
```
命令行运行：
```bash
$ python test_sys_argv.py 1 2 3
['test_sys_argv.py', '1', '2', '3']
test_sys_argv.py
```
可以看到传入的参数通过sys.argv来获取，它就是一个参数列表。


# getopt方法

python的getopt与C语言的的getopt()函数类似。相比于sys模块，支持长参数和短参数，并对参数解析赋值。但它需要结合sys模块进行参数解析，语法格式如下：
```bash
getopt.getopt(args, options, [long_options])
```
短参数为单个英文字母，如果必须赋值需要在后面加英文冒号(`:`)，长参数一般为字符串(相比短参数，更能说明参数含义)，如果必须赋值需要在后面加等号(`=`)。

```python

from scapy.all import *
import sys

class ArgParser():
    # 预处理输入参数
    def usage(self):
        Usage = """
        Usage: python test_getopt.py [OPTION...]\n \n \
        Options:\n \
        -f, --field \t\t-- 字段\n \
        -Y, --display-filter \t-- 条件\n \
        -c, --count \t\t-- 计数\n \
        -h, --help \t\t-- 帮助信息\n \n\
        """
        print(Usage)

    def arg_parser(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:], "f:Y:c:h", ["field=","display-filter=", "count=","return_flag=", "help"])
        except getopt.GetoptError as e:
            print(e)
            self.usage()
            sys.exit()

        if opts == []:
            self.usage()
            sys.exit()
        for op, value in opts:
            if op in ("-f", "--field"):
                self.filters = value
                print(f"field: {value}")
            elif op in ("-Y", "--display-filter"):
                self.display_filter = value
                print(f"display-filter: {value}")
            elif op in ("-c", "--count"):
                self.count = int(value)
                print(f"count: {value}")
            elif op in ('-h', '--help'):
                self.usage()
                sys.exit()

if __name__ == "__main__":
    arg = ArgParser()
    arg.arg_parser()
```

命令行运行：
```bash
$ python test_getopt.py -f test -Y hello
field: test
display-filter: hello
```
注意：短参数(options)和长参数(long_options)不需要一一对应，可以任意顺序，也可以只有短参数或者只有长参数。

# argparse方法

argparse模块提供了很多可以设置的参数，例如参数的默认值，帮助消息，参数的数据类型等。argparse类主要包括ArgumentParser、add_argument和parse_args三个方法。
- ArgumentParser用于初始化解析器，可设置脚本名，描述信息，帮助信息等
- add_argument用于添加参数
- parse_args用于解析参数

下面介绍这三个函数的使用方法。
## ArgumentParser
argparse默认提供了`-h | --help`参数：
```python
import argparse

parser = argparse.ArgumentParser(description="脚本描述信息...")
parser.parse_args()
```
命令行运行：
```bash
$ python test_argparse.py --help
usage: test_argparse.py [-h]

脚本描述信息...

optional arguments:
  -h, --help  show this help message and exit
```
## add_argument
下面列出部分参数：
- name or flags： 参数
- action：对参数执行的动作，比如将多个参数放到列表中：`action='append'`
- nargs：关联不同数目的命令行参数到单一动作
- default：参数默认值
- type：命令行参数应当被转换成的类型
- required：此命令行选项是否必须输入
- help： 此选项简单描述


下面来添加参数：
```python
import argparse

parser = argparse.ArgumentParser(description="脚本描述信息...")
# 添加参数
parser.add_argument("-f", "--field", help = "字段", action='append')
parser.add_argument("-Y", "--display-filter", help = "条件", nargs='*')
parser.add_argument("-c", "--count", help = "计数", type=int, default=2)

args = parser.parse_args()
print(args)
print(f"field: {args.field}")
print(f"display-filter: {args.display_filter}")
print(f"count: {args.count}")
print(f"type(count): {type(args.count)}")
```

命令行运行：
```bash
$ python test_argparse.py -f test -f test2 -Y hello  world
Namespace(count=2, display_filter=['hello', 'world'], field=['test', 'test2'])
field: ['test', 'test2']
display-filter: ['hello', 'world']
count: 2
type(count): <class 'int'>
```

## parse_args
parse_args() 方法用于解析参数，在前面的示例代码中使用parse_args方法来提取参数值，对于无效或者错误的参数会打印错误信息和帮助信息：

命令行运行：
```bash
$ python test_argparse.py -F test
usage: test_argparse.py [-h] [-f FIELD]
                        [-Y [DISPLAY_FILTER [DISPLAY_FILTER ...]]] [-c COUNT]
test_argparse.py: error: unrecognized arguments: -F test
```

# 总结
本文介绍了Python的三种命令行参数解析方法sys.argv、getopt和argparse，可以根据自己的需要进行选择，getopt和argparse两种方法相比来说，建议选择argparse，代码量更少更简洁。更详细的使用方法参考官方文档：
1. argparse：[https://docs.python.org/zh-cn/3/library/argparse.html](https://docs.python.org/zh-cn/3/library/argparse.html)
2. getopt：[https://docs.python.org/zh-cn/3/library/getopt.html](https://docs.python.org/zh-cn/3/library/getopt.html)
3. sys.argv：[https://docs.python.org/zh-cn/3/library/sys.html](https://docs.python.org/zh-cn/3/library/sys.html)




