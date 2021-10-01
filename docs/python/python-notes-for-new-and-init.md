---
title: Python中的__new__、__init__以及metaclass
date: 2021-06-22 12:12:00
author: hiyo
copyright: true
tags:
	- Python
	- 单例模式
	- metaclass

categories: 
	- [编程语言,python]
---

在Python的面向对象编程中，首先得创建实例对象，然后初始化实例对象，Python中`__new__`负责创建实例对象，` __init__` 负责初始化对象，本文介绍`__new__`和` __init__` 的区别以及Python中的元类。

<!--more-->

# `__new__` 和 ` __init__` 

`__new__` 和 ` __init__` 主要具有如下区别：

- `__new__`是在实例创建**之前**被调用的，用于**创建实例然后返回该实例对象**，是个静态方法。`__new__`必须要有返回值，也就是返回实例化出来的实例。
- `__new__`的返回值（实例）将传递给`__init__`方法的第一个参数，然后`__init__`给这个实例设置一些参数。
- `__new__`至少要有一个参数cls，代表当前类
- `__init__`是实例对象**创建完成后被调用**，然后设置对象属性的一些初始值，通常用在初始化一个类实例的时候，是一个实例方法。
- `__init__`的参数self就是`__new__`返回的实例，`__init__`在`__new__`的基础上可以完成一些其它初始化的动作，`__init__`不需要返回值（`__init__()` should return None）。


下面创建一个类：

```python
class Person(object):
    def __new__(cls, *args, **kwargs):
        print("__new__ is called")
        return object.__new__(cls)

    def __init__(self, x, y):
        print("__init__ is called")
        self.name = x
        self.height = y

if __name__ == '__main__':
    p1 = Person("zhangsan",180)        
```

执行结果：

```python
__new__ is called
__init__ is called
```

# python实现单例模式

单例(Singleton)模式就是一个类只能实例化一个对象，这个类必须自己创建自己的唯一实例。

一般情况下，一个类可以实例化多个对象：

```pythpon
p1 = Person("zhangsan",180)
print(p1)
print(p1.name)
p2 = Person("lishi",175)
print(p2)
print(p2.name)
```

执行结果：

```python
__new__ is called
__init__ is called
<__main__.Person object at 0x000001939679BC88>
zhangsan
__new__ is called
__init__ is called
<__main__.Person object at 0x000001939679BC48>
lishi
```

发现两个实例化对象的内存地址不一样，单例模式写法：

```python
class Singleton(object):
    # 单例模式
    _instance = None
    def __new__(cls, *args, **kwargs):
        print("__new__ is called")
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self,x, y):
        print("__init__ is called")
        self.name = x
        self.height = y
```

单例模式重写了`__ new__` 方法，保证只存在一个实例化对象。

执行：

```python
p1 = Singleton("zhangsan",180)
print(p1)
print(p1.name)
p2 = Singleton("lishi", 175)
print(p2)
print(p2.name)
print(p1.name)
```

输出结果：

```python
__new__ is called
__init__ is called
<__main__.Singleton object at 0x00000243DD386E48>
zhangsan
__new__ is called
__init__ is called
<__main__.Singleton object at 0x00000243DD386E48>
lishi
lishi

```

两个实例化对象指向了相同的内存地址，单例模式可以保证系统中一个类只有一个实例，如果希望某个类的对象只能存在一个，使用单例模式可以节省内存。

# python元类MetaClass

`__new__` 方法也用于自定义元类(MetaClass)，下面先来介绍MetaClass的概念。

## 什么是MetaClass

metaclass定义为类中的类（the class of a class），Meta 起源于希腊词汇 meta，有“超越”和“改变”的意思，所以metaclass包含了“超越类”和“变形类”的含义。

先来看一个例子：

```python
>>> class MyClass(object): data = 6
...
>>> myobject = MyClass()
>>> print(myobject.__class__)
<class '__main__.MyClass'>
>>> print(MyClass.__class__)
<class 'type'>
>>>
```

上面的例子中，myobject对象的类为MyClass，MyClass的类是type，也就是说myobject是一个MyClass对象，而MyClass又是一个type对象。

type就是一个元类，它是最常用的元类，是Python中所有类的默认元类，所有的 Python 的用户定义类，都是 type 这个类的实例。

元类被用来构造类(就像类用来构造对象一样)。Python类的创建过程如下：

1. 进行类定义时，Python收集属性到一个字典中
2. 类定义完成后，确定类的元类Meta，执行Meta(name, bases, dct)进行实例化。
	- Meta是元类
	- name：类的名称，`__name__`属性
	- bases：类的基类元组，`__bases__`属性
	- dct：将属性名映射到对象中，列出类的所有属性，`__dict__`属性

可以使用type直接创建类：

```python
>>> myobject = type('MyClass', (), {'data': 6})
>>> print(myobject.__class__)
<class 'type'>

>>> print(myobject.__name__)
MyClass
>>> print(myobject.__bases__)
(<class 'object'>,)
>>> print(myobject.data)
6
>>> print(myobject.__dict__)
{'data': 6, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}
```

也就是说当定义MyClass类时，真正执行的是：`class = type(name, bases, dct)` 语句，

如果一个类或它的一个基类有`__metaclass__`属性，它就被当作元类。否则，type就是元类。对元类的自定义要用到`__new__` 和 ` __init__`方法，接下来介绍元类的定义。

## 定义元类

元类可以实现在创建类时，动态修改类中定义的属性或者方法，一般使用`__new__`方法来修改类属性。

下面的例子使用元类来添加属性方法：

```python
class MyMetaClass(type):
    def __new__(meta, name, bases, attrs):
        print(meta, "__new__ is called")
        # 动态添加属性
        attrs['name'] = "zhangsan"
        attrs['talk'] = lambda self: print("hello")
        return super(MyMetaClass, meta).__new__(meta, name, bases, attrs)

    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        print(metacls, "__prepare__ is called")
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, attrs, **kwargs):
        print(cls, "__init__ is called")
        super().__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        print(cls, "__call__ is called")
        return super().__call__(*args, **kwargs)


class Myclass(metaclass=MyMetaClass):
    pass


if __name__ == '__main__':
    cla = Myclass()
    print(cla.name)
    cla.talk()
    print(cla.__dir__())
```

执行结果：

```python
<class '__main__.MyMetaClass'> __prepare__ is called
<class '__main__.MyMetaClass'> __new__ is called
<class '__main__.Myclass'> __init__ is called
<class '__main__.Myclass'> __call__ is called
zhangsan
hello
['__module__', 'name', 'talk', '__dict__', '__weakref__', '__doc__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

```

可以看到元类MyMetaClass的 `__new__() `方法动态地为 Myclass 类添加了 name 属性和 talk() 方法。

在元类的创建中，可以对name, bases, attrs进行修改，实现我们想要的功能，可以使用getattr()、setattr()等Python反射函数，Python反射机制介绍可参考[Python反射介绍]()。

# PyYAML的序列化和反序列化
在实际应用中，Python 的YAML使用metaclass 的超越变形特性实现了序列化和反序列化（serialization & deserialization）。

## 序列化和反序列化
- 序列化：将结构化数据转换为可存储或可传输格式的过程，就是把对象转换成字节序列的过程。

- 反序列化：把字节序列恢复成对象的过程。

序列化的好处是实现了数据的持久化，可以把数据永久地保存到硬盘上；另外，利用序列化实现远程数据传输，在网络上传输对象的字节序列。

## PyYAML使用

下面的例子中，使用yaml.load()反序列化文本中的Person对象，使用yaml.dump()来序列化创建的Person类。

data.yaml文件内容：

```yaml
!Person
height: 180
name: zhangsan
```

```python
import yaml

class Person(yaml.YAMLObject):
  yaml_tag = u'!Person'
  def __init__(self, name, height):
    self.name = name
    self.height = height

  def __repr__(self):
    return f"{self.name}‘s height is {self.height}cm"

with open("data.yaml", encoding="utf-8") as f:
    p1 = yaml.load(f)
    print(p1)

p2 = Person(name='lishi', height=175)
print(p2)
print(yaml.dump(p2))
# with open("data.yaml", "w", encoding="utf-8") as f:
#     yaml.dump(p2,f)
```

执行结果：

```python
zhangsan‘s height is 180cm
lishi‘s height is 175cm
!Person
height: 175
name: lishi
```

yaml.load()把 yaml 序列加载成一个 Python Object；yaml.dump()把YAMLObject 子类序列化。我们不需要提前知道任何类型信息，这实现了超动态配置编程。

# 总结

本文简要介绍了Python的`__new__` 和 ` __init__`方法，`__new__`在实例创建之前调用并返回实例对象， ` __init__`是在实例对象创建完成后被调用，用于初始化一个类实例，是一个实例方法。

python的元类比较复杂，不好理解，一般在Python框架开发中使用，使用时要谨慎。除了YAML的序列化和反序列化外，**对象关系映射**(ORM)框架也使用了元类，比如Django的models。

元类可以实现类似装饰器的功能，如果不想在方法前面加@decorator_func，可以使用元类来实现。

<center><b>--THE END--<b></center>

