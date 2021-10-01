---
title: Python笔记：字符串操作
date: 2021-02-16 12:12:00
author: hiyo
copyright: true
tags:
	- 字符串
	- Python
categories: 
	- [编程语言,python]
---

字符串相关操作
<!--more-->

# 统计字符串中某个单词的出现的次数

```python
a = 'test 123 dfg test'
## 方法1
len([i for i in a.split(' ') if i == test])

## 方法2
len(a.split('test'))-1
```

# Python提取两个字符串之间的内容
```python
import re 
str = '''/begin MEASUREMENT
100
LINK
DISPLAY
SYMBOL
/end MEASUREMENT'''
 
regex = r'/begin MEASUREMENT([\s\S]*)/end MEASUREMENT'
matches = re.findall(regex, str)
for match in matches:
    print(match)
```

```python
import re 
str = 'test:100      end' 
regex = r'test:([\s\S]*)/end'
matches = re.findall(regex, str)
test = matches[0].strip()
```

# 字符删除、替换
## 删除空格
```python
s = ' 123abcd456  '
# 删除两边的空格
print(s.strip())
# 删除右边空格
print(s.rstrip()) 
# 删除左边空格
print(s.lstrip())
# 删除两边的数字
print(s.strip(' ').strip('123456'))
# 删除两边的引号
s = "'123abcd456'"
print(s.strip("'"))
```

分割并去除空格
```python
string = " hello , world !"
string = [x.strip() for x in string.split(',')]
```
## 将格式化字符转换为字典
```python
string = "dst='192.168.0.1',src='192.168.1.2'"
fields = dict((field.split('=') for field in string.split(',')))
fields = dict(((lambda a:(a[0].strip("'"),a[1].strip("'"))) (field.split('=')) for field in string.split(',')))
```

```python
>>> fields
{'dst': "'192.168.0.1'", 'src': "'192.168.1.2'"}
```

## 删除(替换)任意位置字符
```python
s = '11233aabcdd41556'
# 删除某个特定字符
print(ss.replace('1', ''))
# 同时删除不同字符
import re
print(re.sub('[1a]', '', s))
```

<center><b>--THE END--<b></center>