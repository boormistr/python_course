"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление
(__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
"""


class Cell:
    def __init__(self, cells_quantity):
        self.cells_quantity = cells_quantity

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if value < 0 and key == 'cells_quantity':
            raise ValueError('Значение количества клеток не может быть отрицательным!')

    def __add__(self, other):
        if type(other) == Cell:
            return Cell(self.cells_quantity + other.cells_quantity)
        else:
            print('Классы не совпадают!')

    def __sub__(self, other):
        if type(other) != Cell:
            print('Классы не совпадают!')
        else:
            if self.cells_quantity <= other.cells_quantity:
                print('Уменьшаемое меньше вычитаемого!')
            else:
                return Cell(self.cells_quantity - other.cells_quantity)

    def __mul__(self, other):
        if type(other) == Cell:
            return Cell(self.cells_quantity * other.cells_quantity)
        else:
            print('Классы не совпадают!')

    def __floordiv__(self, other):
        if type(other) == Cell:
            return Cell(self.cells_quantity // other.cells_quantity)
        else:
            print('Классы не совпадают!')

    def make_order(self, n):
        result = ''
        for i in range(1, self.cells_quantity + 1):
            result += '*\n' if i % n == 0 else '*'
        print(result)


first_cell = Cell(7)
second_cell = Cell(3)

sum_cell = first_cell + second_cell
print('Результат суммирования:', sum_cell.cells_quantity)

sub_cell_one = first_cell - second_cell
print('Результат вычитатния:', sub_cell_one.cells_quantity)

sub_cell_two = second_cell - first_cell

mul_cell = first_cell * second_cell
print('Результат умножения:', mul_cell.cells_quantity)

div_cell = first_cell // second_cell
print('Результат целочисленного деления:', div_cell.cells_quantity)

print('Результат работы метода make_order:')
mul_cell.make_order(5)
