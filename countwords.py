import re
with open('countwords.txt') as f:
    content = f.read()
lst = re.split('[ ,?.]',content)
print('There are %d words in countwords.txt.'%len(lst))