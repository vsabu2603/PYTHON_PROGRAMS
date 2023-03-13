mylist=[67,79,85,40,22,95,88]
print(min(mylist))
print('OR')
min=mylist[0]
for x in mylist:
    if x<min:
        min=x
print('The smallest number from the list is',min)
