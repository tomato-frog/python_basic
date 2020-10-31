"""
Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
"""
from re import findall

subjects = {}
r_numbers = r'\d+'

with open('task_6.txt', 'r') as file:
    for line in file:
        subject, lessons = line.split(':')
        hours = sum([int(num) for num in findall(r_numbers, lessons)])
        subjects[subject] = hours

print(subjects)
