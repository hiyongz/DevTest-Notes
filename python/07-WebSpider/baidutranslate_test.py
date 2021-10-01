from urllib import request,parse
import json
 
if __name__ == '__main__':
   
    #实时翻译的接口，只能翻译英语到汉语
    Request_URL = 'https://fanyi.baidu.com/sug' 
    # Request_URL = 'https://fanyi.baidu.com/transapi'  
    Form_Data = {"kw": '我爱你'}
    # Form_Data = {"query": 'love','from':'en','to':'de'} #英语翻译为德语
    # Form_Data = {}
    # Form_Data['kw'] = '爱'    
    # Form_Data['form'] = 'zh'
    # Form_Data['to'] = 'en'
    
    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(Request_URL,data)
    html = response.read().decode('utf-8')
    
    # print(html)
    #可以看出html是一个json格式    
    translate_results = json.loads(html)
    # print(translate_results['data'][0]['dst'])

    for item in translate_results['data']:
        for items in item:
            print(item[items])
