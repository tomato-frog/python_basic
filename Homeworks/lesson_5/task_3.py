"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('task_3.txt', 'r') as text:
    workers = text.readlines()
    salaries = 0
    salary_threshold = 20000

    for name, salary in map(lambda _: _.split(), workers):
        if int(salary) < salary_threshold:
            print(name)

        salaries += int(salary)

    print(f'Средняя зарплата = {salaries / len(workers)}')
