# Python笔记：Python装饰器
装饰器是通过装饰器函数修改原函数的一些功能而不需要修改原函数，在很多场景可以用到它，比如① 执行某个测试用例之前，判断是否需要登录或者执行某些特定操作；② 统计某个函数的执行时间；③ 判断输入合法性等。合理使用装饰器可以极大地提高程序的可读性以及运行效率。本文将介绍Python装饰器的使用方法。

<!--more-->


## python简单装饰器

python装饰器可以定义如下：
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('this is wrapper')
        func(*args, **kwargs)
        print('bye')
    return wrapper

def test_decorator(message):
    print(message)

decorator = my_decorator(test_decorator)
decorator('hello world')
```

输出：
```python
this is wrapper
hello world
bye
```
python解释器将test_decorator函数作为参数传递给my_decorator函数，并指向了内部函数 wrapper()，内部函数 wrapper() 又会调用原函数 test_decorator()，所以decorator()的执行会先打印'this is wrapper'，然后打印'hello world'， test_decorator()执行完成后，打印 'bye' ，\*args和\*\*kwargs，表示接受任意数量和类型的参数。

装饰器 my_decorator() 把真正需要执行的函数 test_decorator() 包裹在其中，并且改变了它的行为，但是原函数 test_decorator() 不变。

一般使用如下形式使用装饰器：

```python
@my_decorator
def test_decorator(message):
    print(message)

test_decorator('hello world')
```
@my_decorator就相当于 `decorator = my_decorator(test_decorator)` 语句。

### functools()
内置装饰器@functools.wrap可用于保留原函数的元信息（将原函数的元信息，拷贝到对应的装饰器函数里）。先来看看没有使用functools的情况：

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('this is wrapper')
        func(*args, **kwargs)
    return wrapper

@my_decorator
def test_decorator(message):
    print(message)

test_decorator('hello world')
print(test_decorator.__name__)
print("######")
help(test_decorator)
```
输出：
```python
this is wrapper
hello world
wrapper
######
Help on function wrapper in module __main__:

wrapper(*args, **kwargs)
```

从上面的输出可以看出test_decorator() 函数被装饰以后元信息被wrapper() 函数取代了，可以使用@functools.wrap装饰器保留原函数的元信息：

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('this is wrapper')
        func(*args, **kwargs)
    return wrapper

@my_decorator
def test_decorator(message):
    print(message)

test_decorator('hello world')
print(test_decorator.__name__)
print("######")
help(test_decorator)
```
输出：
```python
this is wrapper
hello world
test_decorator
######
Help on function test_decorator in module __main__:

test_decorator(message)
```

## 带参数的装饰器
装饰器可以接受自定义参数。比如定义一个参数来设置装饰器内部函数的执行次数：

```python
def repeat(count):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(count):
                print(f'counter: {i}')
            func(*args, **kwargs)
        return wrapper
    return my_decorator

@repeat(4)
def test_decorator(message):
    print(message)

test_decorator('hello world')
```
输出：
```python
counter: 0
counter: 1
counter: 2
counter: 3
hello world
```

## 装饰器的嵌套
Python 支持多个装饰器嵌套：

```python
@decorator1
@decorator2
@decorator3
def func():
    ...
```
### 嵌套示例
```python
import functools

def decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator1')
        func(*args, **kwargs)
    return wrapper


def decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator2')
        func(*args, **kwargs)
    return wrapper

def decorator3(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator3')
        func(*args, **kwargs)
    return wrapper


@decorator1
@decorator2
@decorator3
def test_decorator(message):
    print(message)

test_decorator('hello world')

```
装饰的过程：
* wrapper3 = decorator3(test_decorator)
* wrapper2 = decorator2(wrapper3)
* wrapper1 = decorator1(wrapper2)
* test_decorator = wrapper1

顺序从里到外：
```python
decorator1(decorator2(decorator3(func)))
```
test_decorator('hello world') 执行顺序和装饰的过程相反。

输出：
```python
decorator1
decorator2
decorator3
hello world
```


## 类装饰器
类也可以作为装饰器，类装饰器主要依赖\_\_call\_\_()方法，是python中所有能被调用的对象具有的内置方法（python魔术方法），每当调用一个类的实例时，\_\_call\_\_()就会被执行一次。

下面的类装饰器实现统计函数执行次数：
```python
class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'num of calls is: {self.num_calls}')
        return self.func(*args, **kwargs)

@Count
def test_decorator():
    print("hello world")

test_decorator()
test_decorator()
```
输出：
```python
num of calls is: 1
hello world
num of calls is: 2
hello world
```

## 装饰器使用实例
下面介绍两种装饰器使用场景

### 统计函数执行时间
统计函数执行所花费的时间
```python
import functools
import time

def timer(func):
    # 统计函数执行时间
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      
        run_time = end_time - start_time    
        print(f"{func.__name__} 执行时间为：{run_time:.4f} 秒")
        return value
    return wrapper_timer

@timer
def test_sum(num):
    sum = 0
    for i in range(num+1):
        sum = sum + i
    print(sum)
    
test_sum(100000)
```
输出：
```python
5000050000
test_sum 执行时间为：0.0046 秒
```


### 登录认证
在使用某些web服务时，需要先判断用户是否登录，如果没有登录就跳转到登录页面或者提示用户登录：
```python
import functools

def authenticate(func):
    @functools.wraps(func)
    def wrapper_login(*args, **kwargs):
        request = args[0]
        if check_user_logged_in(request): # 判断用户是否处于登录状态
            return func(*args, **kwargs) # 执行函数secret() 
        else:
            return redirect(url_for("login", next=request.url)) # 跳转登录页面
    return wrapper_login
    
@authenticate
def secret()
    ...
 
```

