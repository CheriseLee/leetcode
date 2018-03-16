# -*- coding: utf-8 -*-
f = open('data.txt','r')
import urllib.request

url1 = 'http://m.weather.com.cn/data3/city.xml'
content1 = urllib.request.urlopen(url1).read().decode('utf8')
provinces = content1.split(',')
result = 'city = {\n'
url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
    p_code = p.split('|')[0]
    url2 = url % p_code
    content2 = urllib.request.urlopen(url2).read().decode('utf8')
    cities = content2.split(',')
    for c in cities:
        c_code = c.split('|')
        url3 = url % c_code[0]
        print(url3)
        content3 = urllib.request.urlopen(url3).read().decode('utf8')
        districts = content3.split(',')
        for d in districts:
            d_pair = d.split('|')
            d_code = d_pair[0]
            name = d_pair[1]
            url4 = url % d_code
            content4 = urllib.request.urlopen(url4).read().decode('utf8')
            code = content4.split('|')[1]
            line = "    '%s': '%s',\n" % (name, code)
            result += line
            print(name + ':' + code)
result += '}'
f = open('city.py', 'w')
f.write(result)
f.close()