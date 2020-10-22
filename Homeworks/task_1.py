"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
from common import safe_intput


def divide(divisor, divider):
    return divisor / divider


x = safe_intput('Введите делимое: ')

while True:
    try:
        y = safe_intput('Введите делитель: ')
        print(divide(x, y))

        break
    except ZeroDivisionError:
        print("Делить на ноль нельзя")
