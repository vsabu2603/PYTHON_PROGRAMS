a=input('enter any character')
x=ord(a)
if (x>=65 or x<=90 or x>=97 or x<=122):
    print('The character is an alphabet')
elif (x>=48 and x<=57):
    print("abc")
    print('The character is a digit')
else:
    print('It is a special character')
