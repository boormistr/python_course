"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
   количества слов в каждой строке."""

with open('lesson5/5-1.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    print('Количество строк: {}'.format(len(content)))
    n = 1
    for line in content:
        print(f'Слов в строке {n}: {len(line.split())}')
        n += 1
