#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/6/6 14:03
# @Author:  hiyongz
# @File:    test_yaml.py


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
