# -*- coding:GBK  -*-
import requests
import urllib.request
import json
import re

while True:
    city_name = input("你想查看哪个城市的天气？\n")
    hello = urllib.parse.urlencode({'city': city_name})
    url = "http://wthrcdn.etouch.cn/weather_mini?%s"%hello
    content = requests.get(url).text
    conToDict = json.loads(content)#变成字典
    descResult = conToDict.get('desc')
    if (conToDict.get('desc') == 'OK'):
       dataResult = conToDict['data']
       weather = dataResult['forecast']
       print("%s\n%s\n%s~%s\n%s%s"%(weather[0]['date'],weather[0]['type'],weather[0]['low'],weather[0]['high'],weather[0]['fengxiang'],weather[0]['fengli']))
    else:
        print('请输入正确的城市名称！')