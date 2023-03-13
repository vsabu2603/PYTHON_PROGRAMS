mylist=[6,9,1,4,14,2]
print(mylist)
mylist.sort()
mylist.sort(reverse=True)
list2=['aaaaaaa','bb','ccccc']
def show(x):
    return x[0]
list3=[[9,2],[4,10]]
print(list3[0])
print(list3[0],[1])
print(list3[1],[0])
list3.sort(key=show)
print(list3)