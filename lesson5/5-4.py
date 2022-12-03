""" Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""

numbers = {eng: rus for eng, rus in zip(['One', 'Two', 'Three', 'Four'], ['Один', 'Два', 'Три', 'Четыре'])}
with open('lesson5/5-4.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    file.seek(0)

with open('lesson5/5-4write.txt', 'w', encoding='UTF-8') as new_file:
    for x in content:
        new_file.write(x.replace(x.split()[0], numbers[x.split()[0]]).strip() + '\n')
