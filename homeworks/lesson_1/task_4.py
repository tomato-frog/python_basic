"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = input('Введите целое положительное число: ')
numbers = [int(i) for i in number]

x = 0
largest = 0

while x < len(numbers):
    if numbers[x] > largest:
        largest = numbers[x]
    x = x + 1

print(largest)
