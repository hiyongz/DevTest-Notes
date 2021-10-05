# Python反射介绍
反射机制是面向对象编程语言中比较重要的功能，可以动态获取对象信息以及动态调用对象，Python作为一门动态编程语言，当然也有反射机制，本文介绍Python反射函数使用方法。

<!--more-->


# 反射

> 反射的概念是由Smith在1982年首次提出的，主要是指**程序可以访问、检测和修改它本身状态或行为**的一种能力。

在程序运行时可以获取对象类型定义信息，例如，Python中的type(obj)将返回obj对象的类型，这种获取对象的type、attribute或者method的能力称为反射。通过反射机制，可以用来检查对象里的某个方法，或某个变量是否存在。也就是可以**通过字符串映射对象的方法或者属性**。

# Python反射函数

Python反射常用的内置函数

- **type**(obj)：返回对象类型
- **isinstance**(object, classinfo)：判断一个对象是否是一个已知的类型，类似 type()
- **callable**(obj)：对象是否可以被调用
- **dir**([obj])：返回obj属性列表
- **getattr**(obj, attr)：返回对象属性值
- **hasattr**(obj, attr)：判断某个函数或者变量是否存在
- **setattr**(obj, attr, val)：给模块添加属性（函数或者变量）
- **delattr**(obj, attr)：删除模块中某个变量或者函数

# 反射函数使用方法

先创建一个类：

```python
class Person():
    def __init__(self, x, y):
        self.age = x
        self.height = y
        
    def __new__(cls, *args, **kwargs):
        print("begin!!!")
        return object.__new__(cls)
        
    def __call__(self, *args, **kwargs):
        print("hello!!!")

    def talk(self):
        print(f"My age is {self.age} and height is {self.height}")
```
## dir()
利用反射的能力，我们可以通过属性字典`__dict__`来访问对象的属性：

```python
p = Person(20, 180)
print(p)
p()
print(p.__dict__)
p.__dict__['age']=22
print(p.__dict__)
p.weight = 60
print(p.__dict__)
print(dir(p))

```

执行输出：

```python
begin!!!
<__main__.Person object at 0x000002484557BCC8>
hello!!!
{'age': 20, 'height': 180}
{'age': 22, 'height': 180}
{'age': 22, 'height': 180, 'weight': 60}
['__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'height', 'talk', 'weight']

```


- 在实例创建之前调用`__new__`方法，返回值（实例）将传递给`__init__`方法的第一个参数。`__new__`方法的详细介绍可参考：[Python中的`__new__`和`__init__`]()
- 实例化对象时会自动执行 `__init__` 方法
- 打印一个对象时，会自动执行` __str__` 方法
- 调用实例化对象时，会自动触发` __call__` 方法
- 通过`dir()`方法可以打印出了对象p的属性。

接下来测试一下其他反射函数：

## callable()

```python
if (callable(p)):
    print("p is callable")
else:
    print("p is not callable")
```

Out:

```python
p is callable
```

## isinstance()和type()
```python
print(isinstance(p, Person))
print(type(p) == Person)
print(isinstance(p.age, int))
print(type(p.age) == int)
```
Out:

```python
True
True
True
True
```
## hasattr()

```python
print(hasattr(p,"talk"))

print(hasattr(p.talk,"__call__"))
```
Out:

```python
True
True
```
## getattr()
```python
print(getattr(p,"talk"))
print(getattr(p.talk, "__call__"))

if hasattr(p,'walk'):
    print(getattr(p,'walk'))
else:
    print("I can't walk")

print(getattr(p, "walk", None)) # 如果没有walk属性就返回None
```
Out:

```python
<bound method Person.talk of <__main__.Person object at 0x000001FF52868288>>
<method-wrapper '__call__' of method object at 0x000001FF52155048>
I can't walk
None
```
## setattr()
```python
setattr(p,'walk','ON')
if hasattr(p,'walk'):
    print(getattr(p,'walk'))
else:
    print("I can't walk")
print(p.__dict__)
```
Out:

```python
ON
{'age': 22, 'height': 180, 'weight': 60, 'walk': 'ON'}

```
## delattr()
```python
delattr(p,'walk')
if hasattr(p,'walk'):
    print(getattr(p,'walk'))
else:
    print("I can't walk")
print(p.__dict__)
```
Out:

```python
I can't walk
{'age': 22, 'height': 180, 'weight': 60}

```

# 应用

下面介绍两种Python反射的应用场景。

## 动态调用

从前面举的例子中，我们了解到可以通过**字符串**来获取对象的属性（`getattr()`），这是非常有用的一个功能。比如，一个类中有很多方法，它们提供不同的服务，通过输入的参数来判断执行某个方法，一般的使用如下写法：

```python
class MyService():
    def service1(self):
        print("service1")

    def service2(self):
        print("service2")

    def service3(self):
        print("service3")

if __name__ == '__main__':
    Ser = MyService()
    s = input("请输入您想要的服务: ").strip()
    if s == "service1":
        Ser.service1()
    elif s == "service2":
        Ser.service2()
    elif s == "service3":
        Ser.service3()
    else:
        print("error!")
```

如果函数比较少这样写没有太大问题，如果有很多，这样写就比较复杂了，需要写大量else语句，可以使用反射机制来写：

```python
if __name__ == '__main__':
    Ser = MyService()
    s = input("请输入您想要的服务: ").strip()
    if hasattr(Ser, s):
        func = getattr(Ser, s)
        func()
    else:
        print("error!")
```

这样是不是简洁了很多，上面的例子中，通过反射，将字符串变成了函数，实现了对对象方法的动态调用。

## 动态属性设置

可以通过setattr()方法进行动态属性设置，在使用scapy库构造报文时，我们需要设置某些报文字段，然而网络协议的报文字段很多，在需要设置大量字段时，一个一个的赋值就很麻烦：

```python
>>> ls(IP)
version    : BitField  (4 bits)                  = ('4')
ihl        : BitField  (4 bits)                  = ('None')
tos        : XByteField                          = ('0')
len        : ShortField                          = ('None')
id         : ShortField                          = ('1')
flags      : FlagsField                          = ('<Flag 0 ()>')
frag       : BitField  (13 bits)                 = ('0')
ttl        : ByteField                           = ('64')
proto      : ByteEnumField                       = ('0')
chksum     : XShortField                         = ('None')
src        : SourceIPField                       = ('None')
dst        : DestIPField                         = ('None')
options    : PacketListField                     = ('[]')
```

可以使用setattr()方法来赋值：

```python
from scapy.all import *

fields = {"version":4, "src":"192.168.0.1","dst":"192.168.10.1"}
ip = IP()
for key, val in fields.items():
    setattr(ip, key, val)
```






