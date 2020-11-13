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
