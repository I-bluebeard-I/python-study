"""
ЗАДАНИЕ 2

Сумма цифр числа
Спросить у пользователя число и вывести в ответ сумму цифр этого числа.
Программа должна спрашивать числа у пользователя до тех пор, пока он не введет "0".
"""

number = None

while number != '0':
    number = input('Введите число: ')

    result = 0
    for symbol in number:
        result += int(symbol)

    print(f'Сумма цифр числа {number} равна {result}')
