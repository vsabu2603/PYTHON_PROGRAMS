def pattern(row,col):
    for i in range(1,row):
        for j in range(1,col):
            print("*",end=' ')
    print()
    print('##########')
pattern(5,5)
pattern(6,6)
pattern(7,7)