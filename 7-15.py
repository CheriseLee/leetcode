import random
import string

total = []
num = 0
while num <200:
    str = ''
    for j in range(8):
        str = str + random.choice(string.ascii_letters)
    if(str not in total):
        total.append(str)
        num = num + 1
    print(num,total[num-1])

#方法2
total2 = []
num2 = 0
while num2 <200:
    str = random.sample(string.ascii_letters,8)
    if(str not in total2):
        total2.append(str)
        num2 = num2 + 1
    print(num2,''.join(total2[num2-1]))

#方法3
total3 = []
num3 = 0
while num3 <200:
    lst = list(string.ascii_letters)
    random.shuffle(lst)
    str = ''.join(lst[:7])
    if(str not in total3):
        total3.append(str)
        num3 = num3 + 1
    print(num3,total3[num3-1])





