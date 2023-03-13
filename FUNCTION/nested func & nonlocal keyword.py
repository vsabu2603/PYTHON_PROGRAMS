def outer():
    print('IN OUTER')
    msg ="Hello World"
    def inner():
        nonlocal msg
        msg ="hi"
        print('IN INNER')
        print(msg)

        inner()
        print(msg)
outer()
