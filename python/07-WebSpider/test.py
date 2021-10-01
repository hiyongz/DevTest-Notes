#!/usr/bin/python3
# -*-coding: utf-8-*-
from urllib import request
import chardet   # pip install chardet

if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com") #rllib.request模块:打开和读取URLs
    html = response.read()
    # print(html)
    html1 = html.decode("utf-8")# 通过decode()命令将网页的信息进行解码，并显示出来
    # print(html)
    charset = chardet.detect(html) # 判断网页的编码方式
    print(charset)


    req = request.Request("http://fanyi.baidu.com/")
    response = request.urlopen(req)
    print("geturl打印信息：%s"%(response.geturl()))  # 返回url的字符串
    print('**********************************************')
    print("info打印信息：%s"%(response.info()))  # 返回meta标签，包括一些服务器的信息；
    print('**********************************************')
    print("getcode打印信息：%s"%(response.getcode())) # 返回HTTP状态码，如果返回200表示请求成功。
