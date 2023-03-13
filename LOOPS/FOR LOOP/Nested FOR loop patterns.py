print("NESTED FOR LOOP")
for i in range(1,5):
    for j in range(1,5):
        print("*",end=' ')
        print(' ')
#####################################################
print("###############")
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=' ')
        print(' ')
#####################################################
print("###############")
for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end=' ')
    print(' ')
#####################################################
print("###############")
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=' ')
    print(' ')
#####################################################
print("###############")
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print(' ')
#####################################################
print("###############")
for i in range(65,69):
    for j in range(65,i+1):
        print(chr(j),end=' ')
    print(' ')
#####################################################
print("###############")
for i in range(68,64,-1):
    for j in range(65,i+1):
        print(chr(j),end=' ')
    print(' ')
#####################################################
print("###############")
for i in range(1,5):
    for j in range(1,5):
        if i==1 or  i==4 or j==1 or j==4:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print(' ')
#####################################################
print("###############")
for i in range(1,6):
    for j in range(1,6):
        if i==j or i+j==6:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()