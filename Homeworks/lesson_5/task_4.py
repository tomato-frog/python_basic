"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехал')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} повернул на{direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


class LimitedSpeedCar(Car):
    _speed_limit = 0

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()

        if self.speed > self._speed_limit:
            print(f'Превышение скорости!')


class TownCar(LimitedSpeedCar):
    _speed_limit = 60


class WorkCar(LimitedSpeedCar):
    _speed_limit = 40


cars = [
    TownCar(70, 'white', 'Volkswagen Beetle'),
    SportCar(120, 'blue', 'Subaru Impreza WRX STi'),
    PoliceCar(100, 'black', 'Jeep Grand Cherokee SRT'),
    WorkCar(30, 'silver', 'Kia Rio')
]

for car in cars:
    car.go()
    car.turn('лево')
    car.show_speed()
    car.stop()
