# Python笔记：lambda匿名函数
在Python中，一般使用def关键字来定义普通函数。顾名思义，匿名函数意味着函数没有名称，Python使用lambda关键字定义匿名函数。在某些情况下，使用匿名函数可以简化代码，提高代码的可读性。本文介绍python匿名函数的使用方法。
<!--more-->

# 匿名函数

Python匿名函数的语法格式：

```python
lambda argument1, argument2,... argumentN: expression
```

匿名函数可以有多个参数，只有一个表达式。下面来看一下普通def函数和lambda函数的区别：

```python
def cube(y):
    return y*y*y

lambda_cube = lambda y: y*y*y

print(cube(3))
print(lambda_cube(3))
```

执行结果：

```python
27
27
```

可以看到，lambda函数更加简洁，不包含“return”语句，返回的是一个函数对象。与常规函数还有以下区别：

**1、lambda 是一个表达式，不是一个语句**

- 表达式（expression）是用“公式”去表达一个东西，比如`y*y*y`就是一个表达式

- 语句（statement）是完成了某些功能，比如赋值语句，条件语句等

- 由于lambda 是表达式，它可以用在一些常规函数 def 不能用的地方，比如，可以用在列表内部，可以作为某些函数的参数。

lambda 函数在列表推导式中使用：
```python
list_num = [3, 4, 6, 2, 5, 8]
list_square = [x ** 2 for x in list_num if x % 2 == 0]
list_square2 = [(lambda x: x** 2)(x) for x in list_num if x % 2 == 0]
print(list_square)
print(list_square2)
```
执行结果：

```python
[16, 36, 4, 64]
[16, 36, 4, 64]
```


作为函数的参数：根据字典值降序排序
```python
mydict = {1:"apple",3:"banana",2:"orange"}
mydict = sorted(mydict.items(), key=lambda x: x[0], reverse=True)
print(mydict)
```
执行结果：

```python
[(3, 'banana'), (2, 'orange'), (1, 'apple')]
```

**2、lambda表达式只有一行，不能写成多行的代码块。**

lambda 用于快速编写简单函数，对于更复杂的多行逻辑使用常规函数来实现。关于这点，Python 之父 Guido van Rossum 曾发了一篇文章解释：[Language Design Is Not Just Solving Puzzles](https://www.artima.com/weblogs/viewpost.jsp?thread=147358)

Lambda函数具有函数式编程的特性，关于函数式编程这里不做介绍，后面有时间单独写一篇文章。Lambda函数可以与filter()、map()和reduce()等内置函数一起使用，下面介绍使用方法。

# filter()函数

Python中的filter()函数接受一个函数对象和一个可迭代对象作为参数。

```python
filter(function or None, iterable)
```

filter()函数对iterable中的每个元素都进行 function 判断，并返回 True 或者 False，最后将返回 True 的元素组成一个新的可遍历的集合。

```python
list_num = [3, 4, 6, 2, 5, 8]

list_even = list(filter(lambda x: x % 2 == 0, list_num))
print(list_even)

list_even2 = [i for i in list_num if i % 2 == 0]
print(list_even2)

list_even3 = []
for i in list_num:
    if i % 2 == 0:
        list_even3.append(i)
print(list_even3)

```

执行结果：

```python
[4, 6, 2, 8]
[4, 6, 2, 8]
[4, 6, 2, 8]
```

如果是None，可用于过滤空格，返回为true的可遍历集合：

```python
list1 = ['', None, 6, 2, False, 8, True]
list1 = list(filter(None, list1))
print(list1)
```

执行结果：

```python
[6, 2, 8, True]
```

# map() 函数

和filter()类似，`map(function, iterable)` 函数表示对 iterable 中的每个元素，都运用 function 这个函数，最后返回一个新的可遍历的集合：

```python
list_num = [3, 4, 6, 2, 5, 8]
list_square = list(map(lambda x: x**2, list_num))
print(list_square)

list_num = [3, 4, 6, 2, 5, 8]
list_square2 = [(lambda x: x** 2)(x) for x in list_num]
print(list_square2)

list_square3 = [x**2 for x in list_num]
print(list_square3)
```

执行结果：

```python
[9, 16, 36, 4, 25, 64]
[9, 16, 36, 4, 25, 64]
[9, 16, 36, 4, 25, 64]
```

# reduce() 函数

reduce(function, iterable)函数同样接收一个函数和一个列表作为参数，reduce()函数属于functools模块，通常用来对一个集合做一些累积操作。function 对象有两个参数，表示对 iterable 中的每个元素以及上一次调用后的结果，运用 function 进行计算，也就是执行重复操作，最终返回一个数值。

```python
from functools import reduce

list_num = [3, 4, 6, 2, 5, 8]
sum = reduce(lambda x, y: x + y, list_num)
print(sum) # 输出：28 = 3 + 4 + 6 + 2 + 5 + 8
```

# 总结

本文介绍了lambda函数和常见的 map()，fiilter() 和 reduce() 三个函数，匿名函数通常用于实现一个简单功能，并且该函数只调用一次。

map()，fiilter() 和 reduce() 三个函数通常与lambda函数结合使用，它们的功能也可以使用列表推导式 (List Comprehension)来实现。它们的性能差异不大，可以根据自己习惯使用。




