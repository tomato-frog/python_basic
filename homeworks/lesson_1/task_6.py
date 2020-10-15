"""
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.
"""

first_result = int(input('Enter your result in the first day: '))
desired_result = int(input('Enter your desired result: '))
current_day = 1
increase_rate = 1.1

new_result = first_result

while True:
    print(f'{current_day} day: {new_result:.2f}')

    if new_result >= desired_result:
        break

    new_result = (new_result * increase_rate)
    current_day += 1

print(f'Спортсмен достигнет своей цели на {current_day}-й день.')
