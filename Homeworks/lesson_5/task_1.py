"""
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""


class Matrix:
    def __init__(self, nested_iter):
        self._data = nested_iter

    def __iter__(self):
        return self._data.__iter__()

    def __add__(self, other):
        matrix1 = self._data
        matrix2 = other
        matrix3 = []

        for vector1, vector2 in zip(matrix1, matrix2):
            new_list = []
            matrix3.append(new_list)

            for value1, value2 in zip(vector1, vector2):
                new_list.append(value1 + value2)

        return Matrix(matrix3)

    def __str__(self):
        result = ''
        for vector in self._data:
            result += '\n' + '|' + ' '.join(map(str, vector)) + '|'
        return result


square = Matrix([
    [2, 1],
    [2, 2],
    [3, 1],
    [3, 2]
])

shift = Matrix([
    [0, 2],
    [0, 2],
    [0, 2],
    [0, 2]
])

print(square + shift)
