# Python PEP—Python增强提案

PEP的全称是Python Enhancement Proposals，Python增强提案。描述了Python的语言特性、功能、编程规范等，包括了技术规范和功能的基本原理说明，是了解Python语言的详细指南。
<!--more-->
PEP官网：https://www.python.org/dev/peps/

PEP创建于2000年，到目前已经有上千个提案了，下面介绍几个值得仔细阅读了解的提案。

### 1. PEP 8 - 编码规范

[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)：定义了编写 Python 代码的规范和编码原则

### 2. PEP 257 - 文档注释
[PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
文档注释规范

### 3. PEP 20 - Python之禅
[PEP 20 -- The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
Python之禅，在Python终端导入this模块查看：

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
### 4. PEP 202 - 列表
[PEP 202 -- List Comprehensions](https://www.python.org/dev/peps/pep-0202/)
列表生成式

### 5. PEP 274 - 字典
[PEP 274 -- Dict Comprehensions](https://www.python.org/dev/peps/pep-0274/)
字典生成式

### 6. PEP 234 - 迭代器
[PEP 234 -- Iterators](https://www.python.org/dev/peps/pep-0234/)
迭代器

### 7. PEP 279 - enumerate
[PEP 279 -- The enumerate() built-in function](https://www.python.org/dev/peps/pep-0279/)
enumerate枚举函数

### 8. PEP 282 - 日志
[PEP 282 -- A Logging System](https://www.python.org/dev/peps/pep-0282/)
日志模块

### 9. PEP 289 - 生成器
[PEP 289 -- Generator Expressions](https://www.python.org/dev/peps/pep-0289/)
生成器表达式

### 10. PEP 318 - 装饰器
[PEP 318 -- Decorators for Functions and Methods](https://www.python.org/dev/peps/pep-0318/)
装饰器


### 11. PEP 309 - 偏函数
[PEP 309 -- Partial Function Application](https://www.python.org/dev/peps/pep-0309/)：Python 偏函数

### 12. PEP 333 - web 服务
[PEP 333 -- Python Web Server Gateway Interface v1.0](https://www.python.org/dev/peps/pep-0333/)：Web开发相关，WSGI协议，描述 web 服务器和 Python web 应用程序\框架之间的标准接口。
[PEP 3333 -- Python Web Server Gateway Interface v1.0.1](https://www.python.org/dev/peps/pep-3333/)：PEP 333的更新版本

### 13. PEP 343 - with语句
[PEP 343 -- The "with" Statement](https://www.python.org/dev/peps/pep-0343/)
with语句

### 14. PEP 484 - 类型提示
[PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)：Python类型提示（Type Hints），在Python3.5.0中引入，允许开发者指定变量类型。

### 15. PEP 342 - 协程
[PEP 342 -- Coroutines via Enhanced Generators](https://www.python.org/dev/peps/pep-0342/)：协程和yield

### 16. PEP 498 - 字符串插值
[PEP 498 -- Literal String Interpolation](https://www.python.org/dev/peps/pep-0498/)
Python3.6新提出的字符串插值方法：
```python
>>> import datetime
>>> name = 'Fred'
>>> age = 50
>>> anniversary = datetime.date(1991, 10, 12)
>>> f'My name is {name}, my age next year is {age+1}, my anniversary is {anniversary:%A, %B %d, %Y}.'
'My name is Fred, my age next year is 51, my anniversary is Saturday, October 12, 1991.'
>>> f'He said his name is {name!r}.'
"He said his name is 'Fred'."
```
### 17. PEP 3101 - 字符串格式化
[PEP 3101 -- Advanced String Formatting](https://www.python.org/dev/peps/pep-3101/)
字符串格式化



