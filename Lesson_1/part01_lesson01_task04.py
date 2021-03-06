"""
ЗАДАНИЕ 4

Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран
отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
"""

number = 0
percent = {
    '0': 'процентов',
    '1': 'процент',
    '2': 'процента',
    '3': 'процента',
    '5': 'процентов',
    '4': 'процента',
    '6': 'процентов',
    '7': 'процентов',
    '8': 'процентов',
    '9': 'процентов',
}

while number < 100:
    number += 1
    if 14 >= number >= 10:
        print(number, percent['0'])
    else:
        str_number = str(number)
        print(number, percent[str_number[-1]])