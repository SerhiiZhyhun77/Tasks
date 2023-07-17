# -*- coding: utf-8 -*-

'''ЗАДАЧА: РЕКУРСИВНАЯ ПЕЧАТЬ
[Начинаем программировать на Python. Тони Гэддис (2022)]
Разработайте рекурсивную функцию, которая принимает целочисленный аргумент n
и распечатывает числа от 1 до n.
'''


def print_numbers(n):
    if n < 1:
        return
    print_numbers(n - 1)
    print(n)


def main():
    n = 10
    print_numbers(n)
    print('-' * 30)
    n = 8
    print_numbers(n)


if __name__ == '__main__':
    main()
