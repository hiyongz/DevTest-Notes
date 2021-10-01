# Python函数的参数类型

python函数的参数类型主要包括必选参数、可选参数、可变参数、位置参数和关键字参数，本文介绍一下他们的定义以及可变数据类型参数传递需要注意的地方。
<!--more-->


## 必选参数
必选参数（Required arguments）是必须输入的参数，比如下面的代码，必须输入2个参数，否则就会报错：

```python
def test_divide(num1, num2):
  return num1/num2

print(test_divide(1,2))
```
其实上面例子中的参数 num1和num2也属于关键字参数，比如可以通过如下方式调用：
```python
print(test_divide(num1=1,num2=2))
print(test_divide(num2=2,num1=1))
```
执行结果：
```python
0.5
0.5
```


## 可选参数
可选参数（Optional arguments）可以不用传入函数，有一个默认值，如果没有传入会使用默认值，不会报错。

```python
def test_add(num=1):
  return num + 1
```
## 位置参数
位置参数（positional arguments）根据其在函数定义中的位置调用，下面是pow()函数的帮助信息:
```sh
>>> help(pow)
Help on built-in function pow in module builtins:

pow(x, y, z=None, /)
    Equivalent to x**y (with two arguments) or x**y % z (with three arguments)

    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.
```
x，y，z三个参数的的顺序是固定的，并且不能使用关键字：
```python
print(pow(2,5))
print(pow(5,2))
print(pow(x=5,2))
```
输出：
```python
32
25
SyntaxError: positional argument follows keyword argument
```

在上面的pow()函数帮助信息中可以看到位置参数后面加了一个反斜杠`/`，这是python内置函数的语法定义，Python开发人员不能在python3.8版本之前的代码中使用此语法。但python3.0到3.7版本可以使用如下方式定义位置参数：
```python
def myfunc(positional_or_keyword_parameters, *, keyword_only_parameters):
	pass
```
星号前面的参数为位置参数或者关键字参数，星号后面是强制关键字参数，具体介绍见[强制关键字参数](#强制关键字参数)。

python3.8版本引入了强制位置参数（Positional-Only Parameters），也就是我们可以使用反斜杠`/`语法来定义位置参数了，可以写成如下形式：
```python
def myfunc(positional_only_parameters, /, positional_or_keyword_parameters, *, keyword_only_parameters):
```
来看下面的例子：
```python
def test_divide(num1, num2, /):
  return num1/num2

print(test_divide(1,2))
print(test_divide(num1=1,num2=2))
```
python3.8运行：
```python
0.5
TypeError: test_divide() got some positional-only arguments passed as keyword arguments: 'num1, num2'
```
不能使用关键字参数形式赋值了。


## 可变参数

可变参数 (varargs argument) 就是传入的参数个数是可变的，可以是0-n个，使用星号（`*`）将输入参数自动组装为一个元组（tuple）：

```python
def test_sum(*numbers):
    print(numbers)
    print(type(numbers))
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum

print(test_sum(1,2,3,4))
```

执行结果：

```python
(1, 2, 3, 4)
<class 'tuple'>
10
```

## 关键字参数

关键字参数（keyword argument）允许将任意个含参数名的参数导入到python函数中，使用双星号（`**`），在函数内部自动组装为一个字典。

```python
def person(**message):
    print(message)
    print(type(message))
    if 'name' in message:
        print(f"my name is {message['name']}")

person(name='zhangsan', age=18)
```

执行结果：

```python
{'name': 'zhangsan', 'age': 18}
<class 'dict'>
my name is zhangsan
```

上面介绍的参数可以混合使用：

```python
def person(name,age=20,*hobby, **message):    
    print(f"my name is {name}, age {age}, hobbies {hobby}, others {message}")
    

person('zhangsan', 18, 'running','swimming', height=175, weight=60)
```

结果：

```python

my name is zhangsan, age 18, hobbies ('running', 'swimming'), others {'height': 175, 'weight': 60}
```



注意：由于传入的参数个数不定，所以当与普通参数一同使用时，必须把带星号的参数放在最后。


## 强制关键字参数
强制关键字参数（Keyword-Only Arguments）是python3引入的特性，可参考：[https://www.python.org/dev/peps/pep-3102/](https://www.python.org/dev/peps/pep-3102/)。 使用一个星号隔开：
```python
def person(name,age=20,*, height, weight):    
    print(f"my name is {name}, age {age}, height {height}, weight {weight}")    

person('zhangsan', 18, height=175, weight=60)
```
在[位置参数](#位置参数)一节介绍过星号前面的参数可以是位置参数和关键字参数。星号后面的参数都是强制关键字参数，必须以指定参数名的方式传参，如果强制关键字参数没有设置默认参数，调用函数时必须传参。
```python
def person(name,age=20,*, height=175, weight):    
    print(f"my name is {name}, age {age}, height {height}, weight {weight}")    

person('zhangsan', 18)
```
执行结果：
```python
TypeError: person() missing 1 required keyword-only argument: 'weight'
```

也可以在可变参数后面命名关键字参数，这样就不需要星号分隔符了：
```python
def person(name,age=20,*hobby, height=175, weight):    
    print(f"my name is {name}, age {age}, hobbies {hobby}, height {height}, weight {weight}")    

person('zhangsan', 18, 'running','swimming', weight=60)
```
执行结果：
```python
my name is zhangsan, age 18, hobbies ('running', 'swimming'), height 175, weight 60
```


## Python函数的参数传递

在[Python对象及内存管理机制](https://blog.csdn.net/u010698107/article/details/117406942)中介绍了python中的参数传递属于对象的**引用传递**（pass by object reference），在编写函数的时候需要特别注意。

先来看个例子：

```python
def test_func1(l):
  l.append(4)

l1 = [1, 2, 3]
l2 = l1
test_func1(l1)
print(l1)
print(l2)
```

执行结果：

```python
[1, 2, 3, 4]
[1, 2, 3, 4]
```

 l1 和 l2指向相同的地址，由于列表可变，l1改变时，l2也跟着变了。

接着看下面的例子：

```python
def test_func2(l):
  l = l + [4]

l1 = [1, 2, 3]
test_func2(l1)
print(l1)
```

结果：

```python
[1, 2, 3]
```

l1没有变化！为什么不是[1, 2, 3, 4]呢？

l = l + [4]表示创建一个“末尾加入元素 4“的新列表，并让 l 指向这个新的对象，l1没有进行任何操作，因此 l1 的值不变。如果要改变l1的值，需要加一个返回值：

```python
def test_func3(l):
  l = l + [4]
  return l
l1 = [1, 2, 3]
l1 = test_func3(l1)
print(l1)
```

结果：

```python
[1, 2, 3, 4]
```

下面的代码执行结果又是什么呢？

```python
def test_func4(l):
  l.append(4)
  return l

l1 = [1, 2, 3]
l2 = l1
l1 = test_func4(l1)
print(l1)
print(l2)
print(l1 is l2)
```

执行结果：

```python
[1, 2, 3, 4]
[1, 2, 3, 4]
True
```

和第一个例子一样，l1 和 l2指向相同的地址，所以会一起改变。这个问题怎么解决呢？

可以使用下面的方式：

```python
def test_func5(l):
  l = l + [4]
  return l

l1 = [1, 2, 3]
l2 = l1
l1 = test_func5(l1)
print(l1)
print(l2)
print(l1 is l2)

# 执行结果
# [1, 2, 3, 4]
# [1, 2, 3]
# False
```

也可以使用浅拷贝或者深度拷贝，具体使用方法可参考[Python对象及内存管理机制](https://blog.csdn.net/u010698107/article/details/117406942)。这个问题在Python编程时需要特别注意。

## 小结
本文主要介绍了python函数的几种参数类型：必选参数、可选参数、可变参数、位置参数、强制位置参数、关键字参数、强制关键字参数，注意他们不是完全独立的，比如必选参数、可选参数也可以是关键字参数，位置参数可以是必选参数或者可选参数。

另外，python中的参数传递属于对象的**引用传递**，在对可变数据类型进行参数传递时需要特别注意，如有必要，使用python的拷贝方法。

**参考文档：**

1. Positional-Only Parameters：[https://www.python.org/dev/peps/pep-0570/](https://www.python.org/dev/peps/pep-0570/)
2. Keyword-Only Arguments：[https://www.python.org/dev/peps/pep-3102/](https://www.python.org/dev/peps/pep-3102/)

<center><b>--THE END--<b></center>

