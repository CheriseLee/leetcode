# _*_ coding:utf-8 _*_
import os
#读取学生成绩
f = open('report.txt',encoding='UTF-8')
scores = f.readlines()
f.close()

#计算每个人的总成绩和平均成绩
stus_lst = []
for x in scores:
    stu_total_score = 0
    stu_lst = x.split()
    stu_score = stu_lst[1:]
    for y in stu_score:
        stu_total_score += int(y)
    stu_lst.append(stu_total_score)
    stu_lst.append(round(float(stu_total_score)/9,2))
    stus_lst.append(stu_lst)

#按照总成绩从大到小排序
stus_lst.sort(key=lambda x:x[-2], reverse=True)
avg = ['平均']

#计算各科的平均成绩
for i in range(1, 12):
    sum = 0
    for x in stus_lst:
        sum += int(x[i])
    avg.append(round(sum/len(stus_lst),2))

#小于60分的替换为不及格
for x in stus_lst:
    for y in x[1:]:
        if(float(y) < 60):
            x[x.index(y)] = '不及格'

#平均成绩插入第一行
stus_lst.insert(0,avg)
#插入序号
for x in stus_lst:
    x.insert(0, stus_lst.index(x))

#插入标题行
title =['名次', '姓名', '语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '总分', '平均分']
stus_lst.insert(0,title)

#成绩写入新文件,编码设为GBK,在notepad中打开不会乱码
g = open('result.txt','w',encoding='GBK')
for x in stus_lst:
    g.writelines('\n' + ' '.join(map(str,x)))
g.close()


