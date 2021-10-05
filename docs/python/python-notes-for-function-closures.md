# Python中的闭包
闭包 (closure) 是函数式编程中的一个概念，Python虽然不是纯粹的是函数式编程语言，但它仍然具有函数式编程的一些特性。在以前的文章[Python笔记：Python装饰器](https://blog.csdn.net/u010698107/article/details/114716537)中介绍的装饰器其实就使用了闭包，本文来介绍一下Python中的闭包。

<!--more-->

# 嵌套函数和变量作用域
介绍闭包之前，先理解什么是嵌套函数和变量作用域。

## 嵌套函数

函数嵌套就是在一个函数内部又定义函数:

```python
def TestFunc(val1):
    val = val1

    def innerFunc():
        print(val)

    innerFunc()


if __name__ == '__main__':
    TestFunc('Hello world')
```

在TestFunc()内部又定义了innerFunc()函数，函数的嵌套主要两个方面的作用。

1. 函数的嵌套能够保证内部函数的隐私，内部函数只能在外部函数作用域内访问。
2. 合理的使用函数嵌套，能够提高程序的运行效率。

## 局部变量和全局变量

在函数内部定义的变量称为**局部变量**，只在函数内部有效。一旦函数执行完毕，局部变量就会被回收。**全局变量**是定义在函数外的变量，作用域范围为全局，函数内部和外部都可以访问它。可以使用`locals()`和`globals()`分别检索局部和全局名称空间字典。

一般情况下，不能在函数内部改变全局变量的值。如果想要在函数内部改变全局变量的值，需要加上 global 关键字：

```python
VALUE1 = 666

def TestFunc2():
    global VALUE1
    VALUE1 = VALUE1 + 1
    VALUE2 = 2
    print(VALUE1)
    print(locals())

TestFunc2()
print(VALUE1)
```

执行结果：

```python
667
{'VALUE2': 2}
667
```

从执行结果可以看到，局部变量为VALUE2，使用global 关键字修饰后，VALUE1变为全局变量。

如果函数内部局部变量和全局变量同名，那么在函数内部，局部变量会覆盖全局变量：

```python
VALUE1 = 666

def TestFunc3():
    VALUE1 = 2
    print(VALUE1)

TestFunc3()
print(VALUE1)
```

执行结果：

```python
2
666
```

## 嵌套函数的变量作用域

类似的，对于嵌套函数，内部函数可以访问外部函数定义的变量，但是无法修改，如果要修改，需要加上 nonlocal 关键字：

```python
def TestFunc():
    val = 1
    def innerFunc():
        nonlocal val
        val = 2
        print("inner:",val)
    innerFunc()
    print("outer:", val)

TestFunc()
```

执行结果：

```python
inner: 2
outer: 2
```

同样，如果内部函数的变量和外部函数变量同名，内部函数变量会覆盖外部函数的变量。

# 闭包

闭包和嵌套函数类似，不同之处在于外部函数返回的是一个函数，而不是一个具体的值。下面用闭包实现计算一个数的 n 次幂：

```python
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of

square = nth_power(2) # 平方
cube = nth_power(3) # 立方
print(square)
print(cube)

print(square(2))  # 2的平方
print(cube(2)) # 2的立方
```

执行结果：

```python
<function nth_power.<locals>.exponent_of at 0x000001E9629C04C8>
<function nth_power.<locals>.exponent_of at 0x000001E9629C0708>
4
8
```

外部函数 nth_power() 返回的是函数 exponent_of()函数，闭包是一个函数对象，它记住了封闭作用域中的值，也就是记住了外部函数 nth_power() 的参数 exponent。

函数exponent_of()的作用域只在nth_power()内部，通过使用闭包，扩展了它的作用域，使能够在其作用域之外调用内部函数。即使函数本身从当前命名空间中删除，闭包作用域中的这个值也会被记住：

```python
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of

square = nth_power(2) # 平方
print(square(2)) # 2的平方

del nth_power
print(square(3)) # 3的平方
```

执行结果：

```python
4
9
```

闭包函数对象有一个`__closure__`属性，返回cell 对象的元组，而cell 对象中保存闭包的变量（例子中的exponent值）：

```python

print(square)
print(cube)
print(square.__closure__)
print(square.__closure__[0].cell_contents)
print(cube.__closure__[0].cell_contents)
```

执行结果：

```python
<function nth_power.<locals>.exponent_of at 0x000001DC127D04C8>
<function nth_power.<locals>.exponent_of at 0x000001DC127D0708>
(<cell at 0x000001DC124401F8: int object at 0x00007FFFA7FAA1B0>,)
2
3
```

# 总结

和嵌套函数返回一个值不同，闭包返回的是一个函数对象。闭包和嵌套函数的优点是可以让程序变得更简洁易读。python装饰器（decorator）中也使用闭包，可参考：[Python笔记：Python装饰器](https://blog.csdn.net/u010698107/article/details/114716537)。



