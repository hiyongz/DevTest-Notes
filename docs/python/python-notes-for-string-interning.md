---
title: Python内存驻留机制
date: 2021-07-22 12:12:00
author: hiyo
copyright: true
tags:
	- Python
	- 内存驻留
categories: 
	- [编程语言,python]
---

字符串驻留机制在许多面向对象编程语言中都支持，比如Java、python、Ruby、PHP等，它是一种数据缓存机制，对不可变数据类型使用同一个内存地址，有效的节省了空间，本文主要介绍Python的内存驻留机制。


<!--more-->

# 驻留
字符串驻留就是每个字符串只有一个副本，多个对象共享该副本，驻留只针对不可变数据类型，比如字符串，布尔值，数字等。在这些固定数据类型处理中，使用驻留可以有效节省时间和空间，当然在驻留池中创建或者插入新的内容会消耗一定的时间。

下面举例介绍python中的驻留机制。

# python内存驻留

在[Python对象及内存管理机制](https://blog.csdn.net/u010698107/article/details/117406942)一文中介绍了python的参数传递以及以及内存管理机制，来看下面一段代码：

```python
l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
l3 = l2
print(l1 == l2)
print(l1 is l2)
print(l2 == l3)
print(l2 is l3)
```

知道结果是什么吗？下面是执行结果：

```python
True
False
True
True
```

l1和l2内容相同，却指向了不同的内存地址，l2和l3之间使用等号赋值，所以指向了同一个对象。因为列表是可变对象，每创建一个列表，都会重新分配内存，列表对象是没有“内存驻留”机制的。下面来看不可变数据类型的驻留机制。

## 整型驻留

在**Jupyter或者控制台交互环境**中执行下面代码：

```python
a1 = 300
b1 = 300
c1 = b1
print(a1 is b1)
print(c1 is b1)

a2 = 200
b2 = 200
c2 = b2
print(a2 is b2)
print(c2 is b2)
```

执行结果：

```python
False
True
True
True
```

可以发现a1和b1指向了不同的地址，a2和b2指向了相同的地址，这是为什么呢？

因为启动时，Python 将一个 **-5~256** 之间整数列表预加载（缓存）到内存中，我们在这个范围内创建一个整数对象时，python会自动引用缓存的对象，不会创建新的整数对象。

浮点型不支持：

```python
a = 1.0
b = 1.0
print(a is b)
print(a == b)

# 结果
# False
# True
```

如果上面的代码在非交互环境，也就是将代码作为python脚本运行的结果是什么呢？（运行环境为python3.7）

```python
True
True
True
True
True
True
```

全为True，没有明确的限定临界值，都进行了驻留操作。这是因为使用不同的环境时，代码的优化方式不同。

## 字符串驻留

在**Jupyter或者控制台交互环境**中：

- 满足**标识符命名规范**的字符串都会被驻留，长度不限。
- 空字符串会驻留
- 使用乘法得到的字符串且满足标识符命名规范的字符串：长度小于等于20会驻留（**peephole**优化），Python 3.7改为4096（**AST**优化器）。
- 长度为1的特殊字符（ASCII 字符中的）会驻留
- 空元组或者只有一个元素且元素范围为-5~256的元组会驻留

满足标识符命名规范的字符：

```python
a = 'Hello World'
b = 'Hello World'
print(a is b)

a = 'Hello_World'
b = 'Hello_World'
print(a is b)
```

结果：

```python
False
True
```

乘法获取字符串（运行环境为python3.7）

```python
a = 'aa'*50
b = 'aa'*50
print(a is b)

a = 'aa'*5000
b = 'aa'*5000
print(a is b)
```

结果：

```python
True
False
```

**在非交互环境中：**

- 默认字符串都会驻留
- 使用乘法运算得到的字符串与在控制台相同
- 元组类型（元组内数据为不可变数据类型）会驻留
- 函数、类、变量、参数等的名称以及关键字都会驻留

注意：**字符串是在编译时进行驻留**，也就是说，如果字符串的值不能在编译时进行计算，将不会驻留。比如下面的例子：

```python
letter = 'd'
a = 'Hello World'
b = 'Hello World'
c = 'Hello Worl' + 'd'
d = 'Hello Worl' + letter
e = " ".join(['Hello','World'])

print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
```

在交互环境执行结果如下：

```python
1696903309168
1696903310128
1696903269296
1696902074160
1696903282800
```

都指向不同的内存。

python 3.7 非交互环境执行结果：

```python
1426394439728
1426394439728
1426394439728
1426394571504
1426394571440
```

发现d和e指向不同的内存，因为d和e不是在编译时计算的，而是在运行时计算的。前面的`a = 'aa'*50`是在编译时计算的。

## 强行驻留

除了上面介绍的python默认的驻留外，可以使用sys模块中的intern()函数来指定驻留内容

```python
import sys
letter_d = 'd'
a = sys.intern('Hello World')
b = sys.intern('Hello World')
c = sys.intern('Hello Worl' + 'd')
d = sys.intern('Hello Worl' + letter)
e = sys.intern(" ".join(['Hello','World']))

print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
```

结果：

```python
1940593568304
1940593568304
1940593568304
1940593568304
1940593568304
```

使用intern()后，都指向了相同的地址。

# 总结

本文主要介绍了python的内存驻留，内存驻留是python优化的一种策略，注意不同运行环境下优化策略不一样，不同的python版本也不相同。注意字符串是在编译时进行驻留。




<center><b>--THE END--<b></center>

