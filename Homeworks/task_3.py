"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
from common import safe_intput


def my_func(x, y, z):
    if x + y >= y + z:
        return x + y
    elif y + z >= x + y:
        return y + z
    elif x + z >= z + y:
        return x + z


print(my_func(safe_intput('Введите число x: '), safe_intput('Введите число y: '), safe_intput('Введите число z: ')))
