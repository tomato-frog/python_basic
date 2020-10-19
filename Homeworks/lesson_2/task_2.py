"""
Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

list_of_variables = [
    input(f"Введите значение в индексе {i} : ")
    for i in range(0, int(input("Введите размер списка: ")))
]

print("Список: ", list_of_variables)

for i in range(1, len(list_of_variables), 2):
    list_of_variables[i - 1], list_of_variables[i] = list_of_variables[i], list_of_variables[i - 1]

print("Преобразованный список: ", list_of_variables)
