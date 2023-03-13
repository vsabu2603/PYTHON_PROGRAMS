a=int(input('Marks of physics subject'))
b=int(input('Marks of chemistry subject'))
c=int(input('Marks of biology subject'))
d=int(input('Marks of mathematics subject'))
e=int(input('Marks of computer subject'))
f=a+b+c+d+e
percentage=(f/500)*100
if percentage>=90:
    print('Grade A')
elif percentage>=80:
    print('Grade B')
elif percentage>=70:
    print('Grade C')
elif percentage>=60:
    print('Grade D')
elif percentage>=40:
    print('Grade E')
else:
    print('Grade F')