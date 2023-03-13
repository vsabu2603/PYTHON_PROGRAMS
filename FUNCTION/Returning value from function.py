def sum(*args):
    print(args)
    z=0
    for x in args:
        z=z+x
        avg=z/len(args)
        return z,avg
a,b=sum(1,2)
print('sum is',a)
print('avg is',b)
