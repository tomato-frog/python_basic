def safe_intput(
        text: str = 'Введите число: ',
        error: str = 'Вы ввели не число!',
):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print(error)


def my_range(start, end, increment=1):
    iteration = start
    while iteration < end:
        yield iteration
        iteration += increment


def my_title(word: str):
    first_letter = word[0].upper()
    the_rest = word[1:].lower()
    return first_letter + the_rest


def my_abs(num):
    return -num if num < 0 else num


def my_map(f, iterable):
    for i in iterable:
        yield f(i)
