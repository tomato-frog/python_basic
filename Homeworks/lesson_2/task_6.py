"""
Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""

# Мы не хотим допускать опечаток, верно? :)
name_field = "название"
price_field = "цена"
amount_field = "количество"
unit_field = "ед"

products = []

i = 1

while True:
    products.append((i, {
        name_field: input(f"Ведите название товара {i}: "),
        price_field: int(input(f"Введите цену товара {i}: ")),
        amount_field: int(input(f"Введите кол-во товара {i}: ")),
        unit_field: input(f"В чём измеряется кол-во?: "),
    }))

    q = input(
        f"Создан товар {i}: {products[i - 1]}.\n"
        f"Нажмите Enter чтобы продолжить добавление товаров или введите 'q' чтобы закончить: "
    )

    if q == 'q':
        break

    i += 1

"""
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
"""

analytics = {
    name_field: [],
    price_field: [],
    amount_field: [],
    unit_field: [],
}

for _num, product in products:
    for field in product:
        if not product[field] in analytics[field]:
            analytics[field].append(product[field])


products_texts = ["товаров", "товар", "товара", "товаров"]
products_length = len(products)

teen = 10 < products_length < 20
choice_rem = products_length % 10

product_text = f"{products_length}"

if products_length == 0:
    product_text += f" {products_texts[0]}"
elif not teen and choice_rem == 1:
    product_text += f" {products_texts[1]}"
elif not teen and 2 <= choice_rem <= 4:
    product_text += f" {products_texts[2]}"
else:
    product_text += f" {products_texts[3]}"

print(f"\nАналитика на {product_text}:")

for field in analytics:
    print(f"{field.title()}: {analytics[field]}")
