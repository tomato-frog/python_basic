"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(),
принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""
from __future__ import annotations
from operator import floordiv, mod


class Cell:
    def _sub_error(self, other: Cell):
        return f'Результат вычитания клеток {self.cells_amount} и {other.cells_amount} должен быть больше нуля'

    def __init__(self, number_of_cells: int):
        self.cells_amount = number_of_cells

    def __add__(self, other: Cell):
        return Cell(self.cells_amount + other.cells_amount)

    def __sub__(self, other: Cell):
        if self.cells_amount - other.cells_amount > 0:
            return Cell(self.cells_amount - other.cells_amount)
        else:
            raise ValueError(self._sub_error(other))

    def __mul__(self, other: Cell):
        return Cell(self.cells_amount * other.cells_amount)

    def __truediv__(self, other: Cell):
        # Раз в задании написано использовать нецелочисленное деление и потом округлять
        # то тут используется / и round()
        return Cell(round(self.cells_amount / other.cells_amount))

    def make_order(self, cells_in_a_row: int):
        def amount(op) -> int: return op(self.cells_amount, cells_in_a_row)

        return '\n'.join([
            *[
                '*' * cells_in_a_row
                for _ in range(amount(floordiv))
            ],
            '*' * amount(mod)
        ])

    def __str__(self):
        return str(self.cells_amount)


cel1 = Cell(10)
cel2 = Cell(15)

try:
    print(cel1 + cel2)
    print(cel1 - cel2)
    print(cel1 * cel2)
    print(cel1 / cel2)
    print(cel1.make_order(3))
except ValueError as err:
    print(err)

