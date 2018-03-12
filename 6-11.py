def picprint(length = 5, width = 5, pic = '*'):
    for i in range(1 , length + 1):
        for j in range(1 , width + 1):
            print(pic, end='')
        print()

picprint()
picprint(4,3)
picprint(2,6,'!')
