"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if len(set(map(len, value))) > 1 and key == 'matrix' and type(value) == list:
            print('Некорректная размерность матрицы')

    def __str__(self):
        output = ''
        for line in self.matrix:
            for x in line:
                output += str(x) + ' '
            output += '\n'
        return output

    def __add__(self, other):
        try:
            new_matrix = self.matrix
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    new_matrix[i][j] += other[i][j]
            return new_matrix
        except IndexError:
            return 'Невозможносно приозвести сложение матриц - разная размерность'


my_matrix = Matrix([[1, 2, 3], [4, 5, 6], [2, 2, 7]])
print(my_matrix)
matrix2 = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
result = Matrix(my_matrix + matrix2)
print(result)
