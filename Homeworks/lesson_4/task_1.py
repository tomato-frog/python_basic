"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv
from common import help_script

usage = 'python3 task_1.py'
desc = 'вычисляет зарплату по формуле (выработка в часах * ставка в час) + премия'
params = {
    'часы': 'кол-во отработанных часов',
    'ставка': 'размер заработной платы в час',
    'премия': 'дополнительная плата, не зависит от кол-ва часов',
}


def calculate_salary(work_hours, hourly_rate, salary_bonus=0.0):
    return work_hours * hourly_rate + salary_bonus


try:
    _, hours, rate, bonus = argv

    salary = calculate_salary(float(hours), float(rate), float(bonus))
    print(salary)
except ValueError:
    help_script(usage, desc, params)
