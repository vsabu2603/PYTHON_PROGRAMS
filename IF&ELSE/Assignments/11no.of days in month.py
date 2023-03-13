a=int(input('enter month number'))
if (a==1 or a==3 or a==5 or a==7 or a==8or a==10or a==12):
    print("no. of days are 31 days")
elif(a==2):
    print("no. of days are 28 or 29 days")
else:
    print("no. of days are 30 days")
