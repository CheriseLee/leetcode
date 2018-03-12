def picprint(length = 5, width = 5, pic = '*'):
    for i in range(1 , length + 1):
        for j in range(1 , width + 1):
            if(j != width):
                print(pic, end='')
            else:
                print(pic)

picprint()
picprint(4,3)
picprint(2,6,'!')