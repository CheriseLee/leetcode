import random
import string

total = []
num = 0
while num <200:
    str = ''
    for j in range(9):
        str = str + random.choice(string.ascii_letters)
    if(str not in total):
        total.append(str)
        num = num + 1
    print(num,total[num-1])




