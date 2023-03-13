list1=[101,54,65,85,402]
print(sum(list1))
print(min(list1))
max=list1[0]
for x in list1:
    if x>max:
        max=x
        print("Max number is",max)



