n = int(input('enter a number'))
sum = 0
while n > 0:
    b = n % 10
    n = n // 10
    sum = sum + b
    print('sum of the digits entered by user is', sum)
