def show(**args):
    print(args)
    for a,b in args.items():
        print(a,b)
show(id=10,name='abc')
show(id=10,name='abc',address='xyz')