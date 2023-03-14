# -*- coding: utf-8 -*-

"""ЗАДАЧА: СПИСОК СПИСКОВ

Напишите программу, в которой создается следующий список списков:

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Vale', 11701, 40500]
]

Определите функцию enrollment_stats(), получающую один параметр. Этим 
параметром должен быть список списков, в котором каждый вложенный список 
содержит три элемента:
    1) название университета;
    2) общее количество зачисленных студентов;
    3) ежегодная плата за обучение.

Функция enrollment_stats() должна возвращать два списка. Первый содержит все 
данные о зачисленных зарегистрированных студентах, а второй - все данные о 
плате за обучение.

Затем определите две функции - mean() и median(), которые получают один 
списковый аргумент и возвращает среднее значение и медиану по каждому списку 
соответственно.

Используя universities, enrollment_stats(), mean() и median(), вычислите общее 
количество студентов, а также среднюю и медианную плату за обучение.

Наконец, выведите все значения и отформатируйте вывод, чтобы он выглядел так:
******************************
Total students: 77,285
Total tuition: $ 271,905

Student mean: 11,040.71
Student median: 10,566

Tuition mean: $ 38,848.57
Tuition median: $ 39,849
******************************
"""


import statistics


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Vale', 11701, 40500]
]


def enrollment_stats(universities):
    students = []
    tuitions = []
    for university in universities:
        students.append(university[1])
        tuitions.append(university[2])
    return students, tuitions


def mean(lst):
    return statistics.mean(lst)


def median(lst):
    return statistics.median(lst)


def main():
    print('*'*30)
    students, tuitions = enrollment_stats(universities)
    print(f'Total students: {sum(students):,}')
    print(f'Total tuition: $ {sum(tuitions):,}')
    print()
    print(f'Student mean: {mean(students):,.2f}')
    print(f'Student median: {median(students):,}')
    print()
    print(f'Tuition mean: $ {mean(tuitions):,.2f}')
    print(f'Tuition median: $ {median(tuitions):,}')
    print('*'*30)


if __name__ == '__main__':
    main()
