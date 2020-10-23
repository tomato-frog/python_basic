"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
from common import safe_intput, my_max


def my_func(x, y, z):
    return my_max(x + y, x + z, y + z)


print(my_func(safe_intput('Введите число x: '), safe_intput('Введите число y: '), safe_intput('Введите число z: ')))
