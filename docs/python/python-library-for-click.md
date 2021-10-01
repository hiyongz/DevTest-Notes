---
title: Python 命令行参数解析之 Click
date: 2021-06-29 12:12:00
author: hiyo
copyright: true
tags:
	- click
	- 命令行参数
	- Python
categories: 
	- [编程语言,python]
---

在[Python笔记：命令行参数解析](https://blog.csdn.net/u010698107/article/details/116346563)中介绍了sys.argv、getopt 和 argparse三种命令行参数解析方法，今天来分享另外一个python命令行工具click，它是用来支持 Web开发框架 Flask的，都由[Pallets 项目](https://palletsprojects.com/)组织开发。

<!--more-->

# click简介
click相比于其他命令行工具的一个优势就是支持多个命令的嵌套和组合，主要包含以下特性：（摘自：[为什么用 Click?](https://click-docs-zh-cn.readthedocs.io/zh/latest/why.html)）
- 没有限制可以简单组合
- 完全遵循 Unix 命令行约定
- 支持从环境变量中加载值
- 支持特定值的提示
- 充分地可嵌套可组合
- 兼容python 2 和 3
- 支持外部文件处理
- 与一些常用的工具帮手结合 (获得 terminal 大小, ANSI 字符颜色, 直接输入按键, 屏幕清理, 获取 config 路径, 启动 apps 和 editors, 等。)



# 选项设置

下面使用click来实现文章[Python笔记：命令行参数解析](https://blog.csdn.net/u010698107/article/details/116346563)中的命令行，可以对比一下它们的差异。

```python
import click

@click.command()
@click.option('--field', '-f', help='字段', multiple=True)
# @click.option('--display-filter', '-Y', prompt='display-filter', nargs=2, help='条件')
@click.option('--display-filter', '-Y', prompt='display-filter', type=(str, int, float, bool), help='条件')
@click.option('--count', '-c', default=2, prompt='count', help='条件')
def cli(field, display_filter,count):
    """Simple program that greets NAME for a total of COUNT times."""

    click.echo(f'{field} {display_filter} {count}')

if __name__ == '__main__':
    cli()
```

可以看到，click使用装饰器@click.command()将cli()方法包装成 click 对象，然后使用@click.option来添加选项参数，下面来介绍这些参数的含义。

## 基本选项

默认第一个参数为长选项，`help`参数用于设置选项的描述信息：

```sh
$ python3 test_click.py --help
Usage: test_click.py [OPTIONS]

  Simple program that greets NAME for a total of COUNT times.

Options:
  -f, --field TEXT                字段
  -Y, --display-filter <TEXT INTEGER FLOAT BOOLEAN>...
                                  条件
  -c, --count                     计数
  --help                          Show this message and exit.
```

也可以使用help_option方法修改help选项显示信息：

```python
@click.help_option('--help', '-h', help='帮助信息')
```

- `default`参数：设置选项默认值
- `type`：设置参数类型

- `prompt`：设置提示信息，设置`prompt=true`或者`prompt=提示信息`后，如果没有设置参数，会出现提示，默认关闭。



## 多个选项和选项多个值

1、选项可以设置多个值，可以通过两种方式：

- 通过 `nargs` 参数来配置。多个值将被放入一个元组（tuple）中，只支持固定数量的参数。

- 使用`type`参数设置不同类型的值：`type=(str, int, float, bool)`

2、`multiple=True`允许多个选项赋值：

一个参数传递多次，并且记录每次的值

```sh
$ python3 test_click.py -f tcp -f udp -Y ip.version==4 -c 1 
('tcp', 'udp') ip.version==4 1
```

## 密码提示

Click 支持隐藏输入信息和确认，比如输入密码时隐藏内容，也可以直接用 `password_option()`装饰器：

```python
import click

@click.command()
@click.option('--password', '-p', prompt=True, hide_input=True, confirmation_prompt=True)
# @click.password_option('--password', '-p', prompt=True, hide_input=True, confirmation_prompt=True)
def cli(password):
    click.echo(f'the password is {password}')    

if __name__ == '__main__':
    cli()
```
执行：
```sh
$ python test_click.py
Password:
Repeat for confirmation:
the password is 123456

$ python test_click.py -p 123456
the password is 123456

```

# 总结

Click相比argparse使用起来更加简洁，可以实现快速构建命令行程序，当然在扩展性上就没有argparse库好。本文只介绍了click的部分功能，更详细的用法可参考：

1. click库官方文档：[https://click.palletsprojects.com/en/8.0.x/](https://click.palletsprojects.com/en/8.0.x/)
2. click库中文文档：[https://click-docs-zh-cn.readthedocs.io/zh/latest/](https://click-docs-zh-cn.readthedocs.io/zh/latest/)



<center><b>--THE END--<b></center>

