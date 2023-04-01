# -*- coding: utf-8 -*-

"""ЗАДАЧА: СЧЕТЧИК ЧЕТНЫХ / НЕЧЕТНЫХ ЧИСЕЛ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая генерирует 100 случайных чисел и подсчитывает
количество четных и нечетных случайных чисел.
"""

import random

def is_even(number):
    return True if number % 2 == 0 else False

def main():
    numbers_odd = []
    numbers_even = []
    for i in range(100):
        num = random.randint(1, 100)
        if is_even(num):
            numbers_even.append(num)
        else:
            numbers_odd.append(num)
    # output
    print('Even numbers:')
    print(numbers_even)
    print(f'Number of even numbers: {len(numbers_even)}')
    print()
    print('Odd numbers:')
    print(numbers_odd)
    print(f'Number of odd numbers: {len(numbers_odd)}')

if __name__ == '__main__':
    main()
