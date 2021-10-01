# -*- coding: UTF-8 -*-
from urllib import request,error
from urllib import parse
import json

if __name__ == "__main__":
    #对应上图的Request URL
    Request_URL = 'http://fanyi.youdao.com/translate'
    #创建Form_Data字典，存储上图的Form Data
    Form_Date = {}
    Form_Date['i'] = '我爱你'
    Form_Date['doctype'] = 'json'    

    #使用urlencode方法转换标准格式
    data = parse.urlencode(Form_Date).encode('utf-8')
    #传递Request对象和转换完格式的数据
    #异常处理 https://blog.csdn.net/c406495762/article/details/59488464
    try:
        response = request.urlopen(Request_URL,data)
        #读取信息并解码
    except error.HTTPError as e:
        print("HTTPError")
        print(e.code)
    except error.URLError as e:
        print("URLError")
        print(e.reason)
    html = response.read().decode('utf-8')
    print(html)
    #使用JSON
    translate_results = json.loads(html)
    #找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']
    #打印翻译信息
    print("翻译的结果是：%s" % translate_results)
