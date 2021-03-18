"""
Задание 3. Генератор объединения двух списков
Есть два списка:
```
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klass = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
```
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:

('Иван', '9А')
('Анастасия', '7В')
...

Количество генерируемых кортежей должно быть равно длине списка tutors. Если в списке klass меньше элементов,
чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
```('Станислав', None)```
Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях
генератор даст эффект.
"""


from pprint import pprint


def gen_cort(len_of_list):
    count = 1
    while count <= len_of_list:
        for pos, word in enumerate(tutors):
            try:
                new_cort = (tutors[pos], klass[pos])
            except IndexError:
                new_cort = (tutors[pos], None)
            yield new_cort
            count += 1


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klass = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

cort = gen_cort(len(tutors))

for i in cort:
    pprint(tuple(cort), width=30)
    print(type(cort))