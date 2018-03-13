import random
comDircet = ['left', 'middle', 'right']#射球方向集合
youScore = 0
comScore = 0

def shoot(youstate,comstate):
    youDirect = input('please choose one side to %s:\nleft,middle,right'%youstate)
    print('you %s %s' %(youstate,youDirect))
    com = random.choice(comDircet)
    print('computer %s %s' % (comstate,com))
    if (youstate=='kick' ):
        if(youDirect != com):
            print(" you get a goal")
            global youScore
            youScore += 1
        else:
            print("oops...Missing")
    else:
        if (youDirect != com):
            print("computer get a goal")
            global comScore
            comScore += 1
        else:
            print("you saved")
    print('yourScore:%d-comScore:%d'%(youScore,comScore))

for i in range(2):
    print('=========Round%d,you kick!========='%(i+1))
    shoot(youstate='kick', comstate='save')
    print('=========Round%d,you Save!=========' % (i + 1))
    shoot(youstate='save', comstate='kick')
while (youScore == comScore):#如果得分相同，继续比赛
    shoot(youstate='kick', comstate='save')
if(youScore > comScore):
    print('You Win')
else:
    print('Computer Win')

