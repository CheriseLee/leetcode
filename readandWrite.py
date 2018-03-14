f = open('data.txt','r+')
lst = f.readlines()
for x in lst:
    lst1 = x.split()
    lst2 = lst1[1:]
    sum = 0
    for y in lst2:
        sum += int(y)
    with open('datanew.txt','a') as g:
        g.write('%s %s '%(str(lst1[0]),str(sum))+ '\n')
f.close()
