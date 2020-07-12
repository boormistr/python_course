"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников."""

with open('lesson5/5-3.txt', 'r') as file:
    content = file.readlines()

# Определение сотрудников с ЗП менее 20тыс.
salaries_under_20 = {line.split()[0]: int(line.split()[1]) for line in content if int(line.split()[1]) < 20000}
for i in salaries_under_20:
    print(i, ': ', salaries_under_20[i], sep='')

# Подсчет средней ЗП
salaries = {line.split()[0]: int(line.split()[1]) for line in content}
print('Средняя зарплата:', round(sum(salaries.values())/len(salaries), 2))
