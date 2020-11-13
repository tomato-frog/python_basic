"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class DivisionByZero(Exception):
    def __init__(self):
        super().__init__('Делить на ноль нельзя!')


try:
    dividend = int(input('Введите делимое: '))
    divisor = int(input('Введите делитель: '))
    if divisor == 0:
        raise DivisionByZero()
    else:
        print(dividend / divisor)
except DivisionByZero as error:
    print(error)
