# -*- coding: utf-8 -*-

"""ЗАДАЧА: СРЕДНИЙ БАЛЛ И ЕГО УРОВЕНЬ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая просит пользователя ввести пять экзаменационных
оценок (баллов). Программа должна показать буквенный уровень для каждой
оценки и средний балл. Предусмотрите в программе функции:
    - calc_average - функция должна принимать в качестве аргументов пять
    балльных оценок и возвращать средний балл;
    - determine_grade - функция должна принимать в качестве аргумента
    балльную оценку и возвращать буквенный уровень оценки, опираясь на
    приведенную в табл.5.3 классификацию.

    Таблица 5.3
------------------------
    Баллы   |   Уровень |
________________________|
  90 и выше |    А      |
  80-89     |    В      |
  70-79     |    С      |
  60-69     |    D      |
  Ниже 60   |    F      |
------------------------
"""

from statistics import mean

def calc_average(grades):
    return mean(grades)

def determine_grade(grade):
    if grade >= 90:
        return 'A'
    elif 80 <= grade <= 89:
        return 'B'
    elif 70 <= grade <= 79:
        return 'C'
    elif 60 <= grade <= 69:
        return 'D'
    else:
        return 'F'

def get_grade(i):
    while True:
        inp = input(f'{i} grade: ')
        try:
            grade = int(inp)
            if 0 <= grade <= 100:
                return grade
        except:
            pass
        print('Please enter correct grade.')

def main():
    print('Enter 5 exam grades:')
    grades = []
    for i in range(5):
        grades.append(get_grade(i + 1))
    # output
    print('\nResult:')
    print('-' * 24)
    print('|    #    | grades | L |')
    for i, grade in enumerate(grades):
        print(f'| {i + 1} grade | {grade:6d} | {determine_grade(grade)} |')

    average = calc_average(grades)
    print('-' * 24)
    print(f'\tAverage: {average} = {determine_grade(average)}')

if __name__ == '__main__':
    main()
