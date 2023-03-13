def sum(*args):
    print(args)
    z=0
    for x in args:
        z=z+x
        print('Sum is',z)

sum(1,2)
sum(1,2,3,4)
