"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('task_2.txt', 'r') as text:
    lines = text.readlines()

    for i, line in enumerate(lines, 1):
        words = len([word for word in line.split()])
        print(f'В {i} строке - {words} слов')

    print(f'Всего строк: {len(lines)}')
