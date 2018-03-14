'''
版权声明: 暂无
文件名称 : GuessNum.py
创建者 : lihh
创建日期: 2018/03/14
文件描述: 本文件完成猜数字游戏
历史记录: 无
'''
import random
f = open('game.txt')
lines = f.readlines() #game.txt中所有数据读取出来写入一个list
f.close()
scores = {}#定义一个空字典
for l in lines:#每一行代表一个用户的信息
    s = l.split()#每一行生成一个list
    scores[s[0]] = s[1:]#为字典中的每个key赋值

name = input('请输入你的名字：')
#获的该用户的信息
score = scores.get(name)
if score is None:#如果该用户不存在，初始化用户信息为0，0，0
    score = [0,0,0]
game_times = int(score[0])  # 猜了几轮
min_times = int(score[1])  # 最少猜中所用次数
total_times = int(score[2])  # 一共猜了几次，猜中未猜中都算
if game_times > 0:
    avg_times = float(total_times) / game_times  # 平均次数
else:
    avg_times = 0
print('你已经玩了%d次，最少%d次猜出答案，平均%.2f轮猜出答案' % (game_times, min_times, avg_times))

def guess(aim):
    for i in range(5):
        num = input("猜猜我想的是几？")
        if(num.isdigit()):
            num = int(num)
            global total_times
            total_times += 1
            if ((num > aim) & (i < 4)):
                print("猜大了！")
            elif ((num < aim) & (i < 4)):
                print("猜小了！")
            elif ((num != aim) & (i == 4)):
                print("You Get Lost！Game Over")
                scores[name] = [str(game_times), str(min(min_times, i)), str(total_times)]
                result = ''
                for n in scores:
                    line = n + ' ' + ' '.join(scores[n]) + '\n'
                    result += line
                #result = '%d %d %d' % (game_times, min(min_times, i), total_times)
                f = open('game.txt', 'w')
                f.write(result)
                f.close()
                Ifcontinue = input("想要继续这个游戏吗？y or n")
                if (Ifcontinue == 'y'):
                    return True
                else:
                    return False
            elif (num == aim):
                global game_times
                game_times += 1
                print("Bingo, WIN！%d次猜中！" % (i + 1))
                scores[name] = [str(game_times), str(min(min_times, i)), str(total_times)]
                result = ''
                for n in scores:
                    line = n + ' ' + ' '.join(scores[n]) + '\n'
                    result += line
               # result = '%d %d %d' % (game_times, min(min_times, i), total_times)
                f = open('game.txt', 'w')
                f.write(result)
                f.close()
                Ifcontinue = input("想要继续这个游戏吗？y or n")
                if (Ifcontinue == 'y'):
                    return True
                else:
                    return False
while True:
    aim = random.randint(1, 15)
    print(aim)
    if(guess(aim) != True):
        break



