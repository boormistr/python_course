seconds_number = int(input('Enter the number of seconds: '))
hours = seconds_number // 3600
minutes = seconds_number % 3600 // 60
seconds = seconds_number % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')

