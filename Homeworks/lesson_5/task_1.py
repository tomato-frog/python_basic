"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def to_int(cls, date):
        return [int(number) for number in date.split('-')]

    @staticmethod
    def validate(date):
        day, month, year = Date.to_int(date)
        return 1 <= day <= 31 and 1 <= month <= 12


user_date = Date('31-07-2015')
print(user_date.to_int('31-07-2015'))
print(Date.validate('31-50-2015'))
