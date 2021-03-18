"""
5. Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]
* Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например
«5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек
или 0 копеек (должно быть 07 коп или 00 коп).

* Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки
остался тот же).
* Создать новый список, содержащий те же цены, но отсортированные по убыванию.
* Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""

import random

prices = []

while len(prices) < 20:
    prices.append(random.randint(0, 10000)/100)
print(prices, '\n')


# * Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после
# сортировки остался тот же).

print(id(prices), '- ID списка до сортировки:')
prices.sort()
print(*prices, sep=', ')
print(id(prices), '- ID списка после сортировки (цены, отсортированы по возрастанию)\n')


# * Создать новый список, содержащий те же цены, но отсортированные по убыванию.

prices_2 = prices.copy()
prices_2.reverse()
print(*prices_2, sep=', ')
print(id(prices_2), '- ID нового списка (цены, отсортированы по убыванию)\n')


# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

print('Пять самых дорогих товаров (отсортированы по возрастанию):')
print(*prices_2[-16::-1], sep=', ')


# * Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например
# «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось
# 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

count = 0
for price in prices:
    if len(str(price).split(".")[1]) == 1:
        prices[count] = f'{str(price).split(".")[0]} руб ' \
                        f'{str(price).split(".")[1]}0 коп'      # один знак после запятой указывает, что это десятые,
                                                                # поэтому добавляю ноль в конце.
    else:
        prices[count] = f'{str(price).split(".")[0]} руб ' \
                        f'{str(price).split(".")[1]} коп'
    count += 1
print('\nФорматированная строка:')
print(*prices, sep=', ')