mylist=[10,20,30,40,10,20,10]
print(mylist)
mylist.remove(10)
print(mylist)
##############
for x in mylist:
    if x==10:
        mylist.remove(x)
        print(mylist)
##########################
print(mylist)
mylist.pop(2) 
print(mylist)
###################
mylist.clear()
print(mylist)
                                                     