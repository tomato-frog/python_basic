"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict


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


class EquipmentError(Exception):
    def __init__(self, msg: str, *equipment: OfficeEquipment):
        self.msg = msg
        self.equipment = equipment

    def __str__(self):
        indent = '\n\t- '
        return f'{self.msg}:{indent}{indent.join(map(str, self.equipment))}'


class OfficeEquipment(ABC):
    def __init__(self, brand: str, model: str, price: float):
        self.brand = brand
        self.model = model
        self.price = price

    @property
    @abstractmethod
    def str_suffix(self):
        pass

    def __str__(self):
        return f'{self.brand} {self.model} (${self.price})' + self.str_suffix


class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, supports_color):
        super().__init__(brand, model, price)
        self.supports_color = supports_color

    @property
    def str_suffix(self):
        return ', supports color print' if self.supports_color else ', b&w'


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price, supports_film):
        super().__init__(brand, model, price)
        self.supports_film = supports_film

    @property
    def str_suffix(self):
        return ', supports scanning film' if self.supports_film else ''


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, price, max_paper_size):
        super().__init__(brand, model, price)
        self.max_paper_size = max_paper_size

    @property
    def str_suffix(self):
        return f', max paper size: {self.max_paper_size}'


class EmptyString(ABC):
    @abstractmethod
    def __str__(self):
        return ''


class WithAddress(EmptyString, ABC):
    address: str

    def __init__(self, address):
        self.address = address

    def __str__(self):
        return f'{type(self).__name__} at {self.address}: ' + super(WithAddress, self).__str__()


class WithStorage(EmptyString, ABC):
    items: Dict[type, list]

    def __init__(self, items: Dict[type, list] = None):
        self.items = {} if items is None else items

    def count(self, _type):
        actual_type = _type if isinstance(_type, type) else type(_type)

        if actual_type not in self.items:
            return 0

        if isinstance(_type, actual_type):
            return len([*filter(lambda x: x is _type, self.items[actual_type])])
        else:
            return len(self.items[actual_type])

    def __str__(self):
        indent = '\n\t\t- '
        res = super(WithStorage, self).__str__()

        if len(self.items.keys()) == 0:
            return res + 'empty'

        for item_type in self.items:
            res += f'\n\t{item_type.__name__}s ({self.count(item_type)}):{indent}'
            res += indent.join(map(str, self.items[item_type]))

        return res


class EquipmentReceiver(WithStorage, ABC):
    def receive(self, *equipment: OfficeEquipment):
        for piece in equipment:
            if type(piece) not in self.items:
                self.items[type(piece)] = [piece]
            else:
                self.items[type(piece)].append(piece)


class EquipmentSender(WithStorage, ABC):
    def send(self, receiver: EquipmentReceiver, *equipment: OfficeEquipment):
        missing_pieces = []
        available_pieces = []

        for piece in equipment:
            if self.count(piece) == 0:
                missing_pieces.append(piece)
                continue

            self.items[type(piece)].remove(piece)
            available_pieces.append(piece)

            if self.count(type(piece)) == 0:
                del self.items[type(piece)]

        receiver.receive(*available_pieces)

        if len(missing_pieces) > 0:
            raise EquipmentError(
                f'Unable to move missing pieces from the {self.__class__.__name__}',
                *missing_pieces
            )


class Department(EquipmentReceiver, WithAddress):
    def __init__(self, address: str, items: Dict[type, list] = None):
        WithAddress.__init__(self, address)
        super().__init__(items=items)


class Warehouse(EquipmentSender, Department):
    pass


def ask_to_send(what, where):
    return safe_intput(f'Сколько {what}ов отправить {where}? ')


available_equipment = {
    'принтер': Printer('Canon', 'LBP710Сx', 200, True),
    'сканер': Scanner('Plustek', 'OpticFilm 8200i SE', 300, True),
    'ксерокc': Xerox('Xerox', 'WorkCentre 3025', 110, 'A4'),
}

my_warehouse = Warehouse('Kazan')
my_department = Department('Innopolis')

for item_name in available_equipment:
    item = available_equipment[item_name]
    for _ in range(ask_to_send(item_name, 'на склад')):
        my_warehouse.receive(item)

print(my_warehouse)
print()

try:
    my_warehouse.send(my_department, *[
        available_equipment[name]
        for name in available_equipment
        for _ in range(ask_to_send(name, 'в подразделение'))
    ])
except EquipmentError as err:
    print(err)

print()
print(my_warehouse)
print(my_department)
