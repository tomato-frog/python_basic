"""
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

translator = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}
result = []

with open('task_4_before.txt', 'r') as latin_text:
    for line in latin_text:
        el = line.split()

        if el[0] in translator:
            word = translator[el[0]]  # передаем ключ - вытаскиваем значение
            result.append(' '.join((word, *el[1:])))

with open('task_4_after.txt', 'w', encoding='UTF-8') as russian_text:
    russian_text.write(('\n'.join(result)))
