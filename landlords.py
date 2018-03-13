#生成54张牌
import random
color = ['A','B','C','D']#四个花色
lst = ['King','Queen']
for x in color:
    for i in range(13):
       lst.append(x+str(i))
random.shuffle(lst) #洗牌

buttom = lst[-3:] #后三张是底牌
InUse = lst[:-3] #发到玩家手中的牌

lst1 = [x for x in InUse if((InUse.index(x)+1)%3 ==0)]
lst2 = [x for x in InUse if((InUse.index(x)+1)%3 ==1)]
lst3 = [x for x in InUse if((InUse.index(x)+1)%3 ==2)]

print('底牌为：%s'buttom)
print(lst1)
print(lst2)
print(lst3)




