"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
from common import safe_intput


def my_func(x, y, z):
    if y + z > x + y and y + z > x + z:
        return y + z
    elif x + z > z + y and x + z > x + y:
        return x + z
    else:
        return x + y


print(my_func(safe_intput('Введите число x: '), safe_intput('Введите число y: '), safe_intput('Введите число z: ')))
