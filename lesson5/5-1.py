"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
   Об окончании ввода данных свидетельствует пустая строка."""

with open('lesson5/5-1.txt', 'w', encoding='utf-8') as file:
    while True:
        new_line = input()
        if new_line == '':
            break
        else:
            file.write(new_line + '\n')
