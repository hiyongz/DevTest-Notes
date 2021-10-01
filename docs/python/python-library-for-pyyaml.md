---
title: Python yaml文件读写
date: 2021-07-13 12:12:00
author: hiyo
copyright: true
tags:
	- Python
	- yaml
categories: 
	- [编程语言,python]
---

yaml相比json来说数据表示更加简洁，特别适合用来读取/更新配置文件，和json一样，也是一种数据串行化格式。本文介绍在Python中PyYAML库解析、保存yaml文件的方法。

<!--more-->

# YAML介绍
YAML是YAML Ain't a Markup Language（YAML不是一种标记语言）的缩写，它其实也是一种标记语言（Yet Another Markup Language），但为了强调这种语言以数据作为中心，而不是以标记语言为重点，而用反向缩略语重命名。(维基百科：[https://zh.wikipedia.org/wiki/YAML](https://zh.wikipedia.org/wiki/YAML))

在[**Python中的`__new__`、`__init__`以及metaclass**](https://blog.csdn.net/u010698107/article/details/117629711)中介绍了序列化和反序列化概念，PyYAML使用了metaclass 的超越变形特性实现序列化和反序列化。

## YAML和JSON差异
1. YAML使用缩进表示层级关系，使用空格进行缩进，JSON使用大括号和方括号  
2. YAML允许使用`#`注释，JSON不能  
3. YAML的字符串可以使用单引号或者双引号，JSON必须使用双引号


YAML文档：
```yaml
Arrays:
- 1
- 2
- 3
Dicts:
  '1': 1
  '2': 2
Numbers: 1
Strings: value
```

JSON文档：
```json
{
    "Arrays": [
        1,
        2,
        3
    ],
    "Numbers": 1,
    "Strings": "value"
}
```


# yaml序列化
Python 安装 PyYAML库
```sh 
pip install pyyaml
```
## dump
dump函数将Python对象序列化为一个YAML文档或者字符串。


```python
import yaml
data1 = {'Numbers':1, 'Strings':"value", 'Arrays':[1,2,3], 'Dicts':{'1':1,'2':2}}
data = yaml.dump(data1, explicit_start=True)
print(data)
print(type(data))
```
执行结果：
```python
---
Arrays:
- 1
- 2
- 3
Dicts:
  '1': 1
  '2': 2
Numbers: 1
Strings: value

<class 'str'>
```


## dump_all
序列化多组对象，yaml文件中的多组数据用`---`分隔。


```python
data2 = [1,2,3]
print(yaml.dump_all([data1,data2], explicit_start=True))
```
执行结果：
```python
---
Arrays:
- 1
- 2
- 3
Dicts:
  '1': 1
  '2': 2
Numbers: 1
Strings: value
---
- 1
- 2
- 3
```

## 保存到文件中

可以将序列化数据保存到文件中。


```python
with open("data1.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data1,f,allow_unicode=True)
```

## 序列化类实例

和json一样，也可以序列化类实例。

```python
class Person(yaml.YAMLObject):
  yaml_tag = u'!Person'
  def __init__(self, name, height):
    self.name = name
    self.height = height

  def __repr__(self):
    return f"{self.name}‘s height is {self.height}cm"

p = Person(name='zhangsan', height=175)
print(p)
print(yaml.dump(p))
with open("data2.yaml", "w", encoding="utf-8") as f:
    yaml.dump(p,f,allow_unicode=True)

```
执行结果：

```python
zhangsan‘s height is 175cm
!Person
height: 175
name: zhangsan
```

<img src="yaml_dump_class.png" width="60%" height="60%" />

# yaml反序列化

主要有load、safe_load、load_all和safe_load_all4种方法，`safe_load()`方法只识别标准的YAML标签，防止不信任的对象输入。

## load
支持任意类型的python对象，

```python
datas = '{"Numbers":1, "Strings":"value", "Arrays":[1,2,3]}'
# data = yaml.safe_load(datas)
data = yaml.load(datas)
print(data)
print(type(data))
```
执行结果：
```python
{'Numbers': 1, 'Strings': 'value', 'Arrays': [1, 2, 3]}
<class 'dict'>
```

## load_all

加载多组序列化yaml数据


```python
with open("data1.yaml", encoding="utf-8") as f:
    datas = yaml.load_all(f)
    print(datas)
    for data in datas:
        print(data)
        print(type(data))

```

执行结果：
```python
<generator object load_all at 0x000001D8AE697CC8>
{'Arrays': [1, 2, 3], 'Dicts': {'1': 1, '2': 2}, 'Numbers': 1, 'Strings': 'value'}
<class 'dict'>
```


## 修改字段内容


```python
import yaml

with open("data1.yaml", encoding="utf-8") as f:
    # data = yaml.safe_load(f)
    data = yaml.load(f)
    data['Arrays'].append(4)
    data['Strings'] = 'hello'
    # data.update({data['Strings']:hello})
    print(data)

with open("data1.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data,f,allow_unicode=True)
```

执行结果：
```python
{'Arrays': [1, 2, 3, 4], 'Dicts': {'1': 1, '2': 2}, 'Numbers': 1, 'Strings': 'hello'}
```


## 加载Python类实例
和json一样，也支持加载Python类的实例


```python
import yaml

class Person(yaml.YAMLObject):
  yaml_tag = u'!Person'
  def __init__(self, name, height):
    self.name = name
    self.height = height

  def __repr__(self):
    return f"{self.name}‘s height is {self.height}cm"

with open("data2.yaml", encoding="utf-8") as f:
    p = yaml.load(f)
    print(p.name)
```

执行结果：
```python
zhangsan
```

**参考文档：**
pyyaml官方文档：[https://pyyaml.org/wiki/PyYAMLDocumentation](https://pyyaml.org/wiki/PyYAMLDocumentation)


<center><b>--THE END--<b></center>

