try:
    month_number = int(input('Enter the month number: '))
except ValueError:
    print('Enter a number!')


seasons_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer',
                'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']

seasons_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer',
                7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}

print('Season via list: ', seasons_list[month_number-1])
print('Season via dict: ', seasons_dict[month_number])

