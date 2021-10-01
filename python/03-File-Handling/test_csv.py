#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/6/13 22:35
# @Author:  hiyongz
# @File:    test_csv.py
import csv

article_name, article_url,publish_time,word_count = [],[],[],[]
f = open('articles.csv', 'w', encoding='utf-8',newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(["文章标题", "URL地址", "发布时间", "字数"])
csv_writer.writerow([article_name, article_url,publish_time,word_count])
f.close()