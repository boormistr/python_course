number = input('Enter the number: ')

n = 0
result = 0

while n < len(number):
    if int(number[n]) > result:
        result = int(number[n])
    n += 1

print('The biggest one: ', result)

