list1 = [1, 6, 4, 3, 5, 8, 2, 3]
temp = []
for x in list1:
    if x not in temp:
        temp.append(x)
        print(temp)
