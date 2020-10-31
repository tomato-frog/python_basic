"""
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
"""
from json import dump

firms_profits = {}
combined_profit = 0
firms_count = 0

with open('task_7.txt', 'r') as firms, open('task_7.json', 'w') as firms_json:
    for firm, _, gain, costs in map(lambda _: _.split(), firms):
        profit = float(gain) - float(costs)
        firms_profits[firm] = profit

        if profit >= 0:
            combined_profit += profit
            firms_count += 1

    dump([
        firms_profits,
        {'average_profit': combined_profit / firms_count}
    ], firms_json)
