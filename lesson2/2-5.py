rating = []
while True:
    value = input()
    if value == 'exit':
        break
    try:
        number = int(value)
    except ValueError:
        print('Enter the number!!!')
        continue

    if not rating:
        rating.append(number)
    else:
        for i in rating:
            if number >= i:
                rating.insert(rating.index(i), number)
                break
            else:
                continue
"""
Последние 9 строчек можно было заменить двумя:
rating.append(number)
rating.sort(reverse=True)

"""
print(rating)