"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
from common import my_range

print(*[number for number in my_range(20, 240) if number % 20 == 0 or number % 21 == 0])
