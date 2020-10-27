"""
а) Итератор, генерирующий целые числа, начиная с указанного
"""
from itertools import count
from sys import argv


def my_iter(start_num, stop_num):
    for num in count(start_num):
        yield num

        if num == stop_num:
            break


_, start, stop = argv

try:
    print(*(my_iter(int(start), int(stop))))
except ValueError:
    print('Not a number!')
