"""
б) Итератор, повторяющий элементы некоторого списка, определенного заранее.
"""
from itertools import cycle
from sys import argv


def my_iterator(iterable, repeat_times):
    iteration = repeat_times * len(iterable)

    for item in cycle(iterable):
        if iteration == 0:
            break

        yield item

        iteration -= 1


iterables = argv[1:-1]
count = argv[-1]

try:
    print(list(my_iterator(iterables, int(count))))
except ValueError:
    print('Укажите количество повторений последним параметром.')
