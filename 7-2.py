"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    @property
    def tissue_consumption(self):
        return self.size * 6.5 + 0.5


class Suit(Clothes):
    @property
    def tissue_consumption(self):
        return self.height * 2 + 0.3


my_coat = Coat(45, 65)
print(my_coat.tissue_consumption)

my_suit = Suit(50, 60)
print(my_suit.tissue_consumption)
