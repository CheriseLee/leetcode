for i in range(1, 10):
    for j in range(1, 10):
        if(j > i):
            break
        elif(j < i):
            print('%d x %d = %-2d,'% (j,i,i*j), end = ' ')
        else:
            print('%d x %d = %-2d' % (j,i,i*j))
        
