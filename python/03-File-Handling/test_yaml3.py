#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/6/13 20:25
# @Author:  hiyongz
# @File:    test_yaml3.py

import yaml


with open("data3.yaml", encoding="utf-8") as f:
    # steps = yaml.safe_load(f)
    steps = yaml.load(f)
    steps.update({"123":1234})
    print(steps)

steps = {'user': {'name': '可优', 'age': 17, 'money': None, 'gender': True},

'lovers': [u'柠檬小姐姐', u'橘子小姐姐', '小可可']

}


with open("data3.yaml", "w", encoding="utf-8") as f:
    yaml.dump(steps,f,allow_unicode=True)

