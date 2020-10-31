"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
"""

with open('task_5.txt', 'w') as file:
    numbers = input('Введите числа через пробел: ')
    file.write(numbers)


with open('task_5.txt', 'r') as file:
    numbers = file.read()
    sum_of_numbers = sum([float(number) for number in numbers.split()])
    print(f'Сумма введенных чисел: {sum_of_numbers}')
