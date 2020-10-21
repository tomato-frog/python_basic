"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division():
    try:
        x = int(input('Введите делимое: '))
        y = int(input('Введите делитель: '))
        result = x / y
    except ValueError:
        return 'Вы ввели не число'
    except ZeroDivisionError:
        return "Делить на 0 нельзя"

    return result


print(division())
