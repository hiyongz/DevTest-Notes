#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/3/16 15:22
# @Author:  haiyong
# @File:    test_pandas.py

import pandas as pd

# Import .csv file
df = pd.read_csv('demo.csv')
del df['x1']
# df= df.drop('x1', 1) # 不改变内存，及输入df的时候，它还是显示原数据
# df.drop('x1',axis=1, inplace=True) # 改变内存，及输入df的时候，它显示改变后的数据
# df.drop([df.columns[[0,1, 3]]], axis=1,inplace=True)
df['d1'] = 'tacfin'
df.loc[df.d1=='a','d1'] = 'tacfin'

df