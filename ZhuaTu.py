# -*- encoding: utf-8 -*-
import requests
import re
import os
import urllib.request
import json
import chardet

#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码
def getHtml(url):
    content = requests.get(url)
    content.encoding = 'utf8'
    return content.text

def getImg(html):
    reg = r'src="(.+?\.jpeg)" '
    imgre = re.compile(reg)
    imglist = imgre.findall(html)#表示在整个网页中过滤出所有图片的地址，放在imglist中
    x = 0
    path = 'D:\\test'
    # 将图片保存到D:\\test文件夹中，如果没有test文件夹则创建
    if not os.path.isdir(path):
        os.makedirs(path)
    paths = path+'\\'      #保存在test路径下

    for imgurl in imglist:
        urllib.request.urlretrieve("https:" + imgurl,'{}{}.jpeg'.format(paths,x))  #打开imglist中保存的图片网址，并下载图片保存在本地，format格式化字符串
        x = x + 1
    return imglist

url = "https://www.qiushibaike.com/imgrank/"
html = getHtml(url)
getImg(html)