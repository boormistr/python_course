a = int(input('Enter a: '))
b = int(input('Enter b: '))

day = 1
while a < b:
    a *= 1.1
    day += 1

print('Day number: ', day)

