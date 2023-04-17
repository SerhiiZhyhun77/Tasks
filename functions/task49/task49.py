# -*- coding: utf-8 -*-

'''ЗАДАЧА: БОЛЬШЕ ЧИСЛА n
[Начинаем программировать на Python. Тони Гэддис (2022)]

В программе напишите функцию, которая принимает два аргумента: список и число n.
Допустим, что список содержит числа. Функция должна показать все числа в
списке, которые больше n.
'''

import random

def more_n(num_lst, n):
    print(f'Numbers more than {n}:')
    for num in num_lst:
        if num > n:
            print(num, end=' ')
    print()

def main():
    # set initial data
    n = random.randint(1, 100)
    num_lst = random.sample(range(100), random.randint(1, 100))
    # output
    print(f'Selected number: {n}')
    print('List of numbers:')
    print(num_lst)
    more_n(num_lst, n)

if __name__ == '__main__':
    main()
