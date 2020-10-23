def safe_intput(
        text: str = 'Введите число: ',
        error: str = 'Вы ввели не число!',
):
    """
    Функция вызывает ввод, проверяет его на ValueError, при возникновении ошибки снова запрашивает ввод.
    Если ввод корректен - преобразовывает введённое значение в int .
    :param text: выводится при запросе ввода
    :param error: выводится при попытке пользователя ввести не число
    :return: преобразованный в int ввод
    """
    while True:
        try:
            return int(input(text))
        except ValueError:
            print(error)


def my_range(start, end, increment=1):
    """
    Функция принимает значения по которым будет создана последовательность.
    :param start: число с которого начинается последовательность
    :param end: число до которого продолжается последовательность, указанное число не включается в диапазон
    :param increment: шаг увеличения
    :return: неизменяемая последовательность чисел
    """
    iteration = start
    while iteration < end:
        yield iteration
        iteration += increment


def my_title(word: str):
    """
    Функция конвертирует первый элемент принятой строки в верхний регистр,
    а все оставшиеся элементы в нижний регистр.
    :param word: строка
    :return: строка с заглавной буквы
    """
    first_letter = word[0].upper()
    the_rest = word[1:].lower()
    return first_letter + the_rest


def my_abs(num):
    """
    Функция идентична встроенной функции abs()
    :param num: число
    :return: абсолютная величина числа
    """
    return -num if num < 0 else num


def my_map(f, iterable):
    """
    Функция идентична встроенной функции map()
    :param f: функция
    :param iterable: итерируемый объект
    :return: преобразует значения в итерируемом объекте используя функцию f
     и возвращает новый итератор с изменёнными значениями
    """
    for i in iterable:
        yield f(i)


def my_max(*numbers):
    """
    Функция возвращает наибольшее число из переданных.
    :param numbers: числа
    :return: максимальное число
    """
    maximum = numbers[0]

    for num in numbers[1:]:
        if num > maximum:
            maximum = num

    return maximum
