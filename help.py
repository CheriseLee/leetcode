import re

filePath = "D:\\test.txt"
with open(filePath, 'r') as a:
    content = a.readlines()
    print(content)
    #得到包含邮箱的每一行
    pattern = re.compile('.+@.+\.com')
    maillist = []
    for i in content:
        if(len(pattern.findall(i)) != 0):
            maillist.append(i)

    #对所有行按长度排序
    content.sort(key = lambda i:len(i), reverse=True)
    print(content)
    #把所有行写入到新生成的文件


