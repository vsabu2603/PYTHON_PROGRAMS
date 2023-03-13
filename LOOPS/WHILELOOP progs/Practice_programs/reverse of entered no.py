n=int(input('enter number'))
a=0
while n>0:
    c=n%10
    a=(a*10)+c
    n=n//10
    print('the reverse number is',a)