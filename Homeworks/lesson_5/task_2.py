"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import abstractmethod, ABC


class Clothes(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    @abstractmethod
    def cost(self): pass


class Coat(Clothes):
    @property
    def cost(self):
        return self.size / 6.5 + 0.5


class Suite(Clothes):
    @property
    def cost(self):
        return 2 * self.size + 0.3


calvin_klein_coat = Coat('Calvin Klein', 44)
tommy_hilfiger_coat = Coat('Tommy Hilfiger', 48)
carhartt_suite = Suite('Carhartt', 168)
lazy_oaf_suite = Suite('Lazy Oaf', 180)

print(calvin_klein_coat.cost)
print(tommy_hilfiger_coat.cost)
print(carhartt_suite.cost)
print(lazy_oaf_suite.cost)
