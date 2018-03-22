#coding:gbk
import re
import os
with open('from.txt') as f:
    text = f.readlines()
m = re.findall('[a-zA-Z]+',str(text[0]))
n = sorted(m)
for x in n:
    print(x)