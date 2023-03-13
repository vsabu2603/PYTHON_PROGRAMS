a=int(input('enter basic salary'))
if a<=10000:
    hra=20
    da=80
    gs=a+da+hra
    print('gross salary is',gs)
elif a<=20000:
    hra=25
    da=90
    gs = a + da + hra
    print('gross salary is', gs)
else:
    hra=30
    da=95
    gs = a + da + hra
    print('gross salary is', gs)
