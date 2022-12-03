import random

class Card:
    def __init__(self, owner):
        self.data = self.__card_creating()
        self.owner = owner
        # self.numbers = self.__list_of_numbers()

    def __card_creating(self):
        # Создаю структуру карточки представляющую собой словарь словарей (столбцы и строки)
        structure = {key * 10: {1: '', 2: '', 3: ''} for key in range(1, 10)}
        # Заполняю каждый столбец минимум одним значением
        for col in structure:
            structure[col][random.randint(1, 3)] = random.randint(col-9, col)
        # Выбираю случайную ячейку и проверяю пустая она или нет
        n = 0
        while n <= 5:
            col = random.randint(1, 9) * 10
            row = random.randint(1, 3)
            if structure[col][row] != '':
                continue
            # Находим количество заполненных ячеек в строке
            elif sum(map(lambda x: structure[x][row] != '', structure)) == 5:
                continue
            else:
                # Заполняю выбранную ячейку значением, которого еще нет в столбце
                while True:
                    new_number = random.randint(col-9, col)
                    if new_number in list(structure[col].values()):
                        continue
                    else:
                        structure[col][row] = new_number
                        n += 1
                        break
        return structure

    def __str__(self):
        result = f'-----------------------------------\n           Player: {self.owner}\n'
        for row in range(1, 4):
            for column in self.data:
                result += str(self.data[column][row]) + '\t'
            result += '\n'
        result += '-----------------------------------\n'
        return result

    def crossing(self, number):
        for col in self.data:
            for row in self.data[col]:
                if self.data[col][row] == number:
                    self.data[col][row] = '--'

    @property
    def numbers(self):
        numbers = []
        for col in self.data:
            for row in self.data[col]:
                if isinstance(self.data[col][row], int):
                    numbers.append(self.data[col][row])
        return numbers


class Game:
    def __init__(self):
        self.__sequence = [x for x in range(1, 91)]
        random.shuffle(self.__sequence)

    def run(self):
        print('\nИгра началась!\n')
        human = Card('Human')
        computer = Card('Computer')
        turn = 1
        while len(human.numbers) > 0 and len(computer.numbers) > 0:
            barrel = self.__sequence.pop()
            print(f'\n\nХод номер {turn}')
            print(human)
            print(computer)
            print(f'Бочонок номер: {barrel}\n')
            answer = input('Число есть в карточке? (y/n)  ')
            if barrel in computer.numbers:
                computer.crossing(barrel)
            if answer == 'y' and barrel not in human.numbers:
                print('Вы ошиблись! Число нет в карточке. Игра окончена.')
                break
            elif answer == 'y' and barrel in human.numbers:
                human.crossing(barrel)
                turn += 1
                continue
            elif answer == 'n' and barrel not in human.numbers:
                turn += 1
                continue
            elif answer == 'n' and barrel in human.numbers:
                print('Вы ошиблись! Число есть в карточке. Игра окончена.')
                break
        if len(human.numbers) == 0 and len(computer.numbers) > 0:
            print('Игра окончена. Вы победили!')
        elif len(human.numbers) > 0 and len(computer.numbers) == 0:
            print('Игра окончена. Вы проиграли!')
        elif len(human.numbers) == 0 and len(computer.numbers) == 0:
            print('Игра закончилась вничью.')


game_one = Game()
game_one.run()
