"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:
    def __init__(self):
        self.speed = 0
        self.color = None
        self.name = ''
        self.is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def __trunc__(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    pass

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.speed}. Превышение скорости!')
        else:
            print(f'Скорость {self.speed}.')


class SportCar(Car):
    pass


class WorkCar(Car):
    pass

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость {self.speed}. Превышение скорости!')
        else:
            print(f'Скорость {self.speed}.')


class PoliceCar(Car):
    def __init__(self):
        super(Car, self).__init__()
        self.is_police = True


work_car = WorkCar()
work_car.speed = 70
work_car.color = 'Violet'
work_car.name = 'Tesla'
work_car.show_speed()
print(f'\nМарка: {work_car.name}\nЦвет: {work_car.color}\nСкорость автомобиля: {work_car.speed}\n')

town_car = TownCar()
town_car.speed = 30
town_car.show_speed()

police_car = PoliceCar()
print(police_car.is_police)
