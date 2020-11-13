"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real_part = float(real_part)
        self.imaginary_part = float(imaginary_part)

    def __str__(self):
        return f'{self.real_part} + {self.imaginary_part}i'

    def __add__(self, other: 'ComplexNumber'):
        return ComplexNumber(
            self.real_part + other.real_part,
            self.imaginary_part + other.imaginary_part
        )

    def __mul__(self, other: 'ComplexNumber'):
        return ComplexNumber(
            (self.real_part * other.real_part) - (self.imaginary_part * other.imaginary_part),
            (self.real_part * other.imaginary_part) + (self.imaginary_part * other.real_part)
        )

    def __eq__(self, other: 'ComplexNumber'):
        return self.real_part == other.real_part and self.imaginary_part == other.imaginary_part


n1 = ComplexNumber(5, 2)
n2 = ComplexNumber(5, 1)

assert n1 + n2 == ComplexNumber(10, 3)
assert n1 * n2 == ComplexNumber(23, 15)

print(f'({n1}) + ({n2}) = {n1 + n2}')
print(f'({n1}) * ({n2}) = {n1 * n2}')
