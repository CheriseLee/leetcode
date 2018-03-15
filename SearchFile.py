#-*- coding:utf-8 -*-
import os
import sys
def findfile(key, inputdir = '.'):
    found_list = []
    '''
    os.walk 获取指定目录下所有深度的文件，子目录的列表,得到三元组 (dirpath, dirnames, filenames)
    第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
    dirpath    是一个string，代表目录的路径，
    dirnames    是一个list，包含了dirpath下所有子目录的名字。
    filenames    是一个list，包含了非目录文件的名字。
    这些名字不包含路径信息，如果需要得到全路径，需要使用os.path.join(dirpath, name).
    '''
    for path, dirnames, filenames in os.walk(inputdir):
        print('search'+ path + '...')
        for name in filenames:
            full_name = path + '/' + name
            if key in name:
                found_list.append(full_name)
            with open(full_name) as f:
                for l in f.readlines():
                    if key in l:
                        found_list.append(full_name + ' : ' + l)
    return found_list

keyword = input("please input keyword:")

path = 'C:\\Users\\Yuexl\\Desktop\\daochu'

if not path.strip():
    path = '.'
result = findfile(keyword, path)
print('=========result=======')
for r in result:
    print (r)