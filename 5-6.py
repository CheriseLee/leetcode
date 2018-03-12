import random
aim = random.randint(1,20)
cnt = 0  #每轮猜了几次  
Time = 0 #一共猜了几次，猜中未猜中都算
circle = 0 #猜了几轮
while True:
    num = int(input("猜猜我想的是几？"))
    cnt = cnt + 1
    Time = Time +1
    if((num > aim) and cnt < 6):
        print("猜大了！")
    elif((num < aim) and cnt < 6):
        print("猜小了！")
    elif((num == aim)and cnt < 6):
        circle = circle +1
        print("Bingo, WIN！%d次猜中！参与者平均猜中次数为%d"%(cnt,Time/circle))
        Ifcontinue = input("想要继续这个游戏吗？y or n")
        if(Ifcontinue == 'y'):
            cnt = 0
            continue
        else:
            break
    else:
        print("Game Vver ,Lost！")
        Ifcontinue = input("想要继续这个游戏吗？y or n")
        if(Ifcontinue == 'y'):
            cnt = 0
            continue
        else:
            break
