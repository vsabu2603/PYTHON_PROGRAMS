mylist=[67,79,85,40,22,95,88]
print(max(mylist))
print('OR')
max=mylist[0]
for x in mylist:
    if x>max:
        max=x
print('The largest number from the list is',max)
