print('COPYING ONLY REFERNCE')
list1=[10,20,30]
list2=list1
list2[0]=90
print(list1)
print(list2)
##########################
print('MAKING AN ENTIRE NEW COPY')
list1=[10,20,30]
list2=list1.copy()
list2[0]=90
print(list1)
print(list2)

