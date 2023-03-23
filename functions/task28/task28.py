# -*- coding: utf-8 -*-

"""ЗАДАЧА: МАКСИМАЛЬНОЕ ИЗ ДВУХ ЗНАЧЕНИЙ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите функцию max, которая в качестве аргументов принимает два
целочисленных значения и возвращает значение, которое является большим из
двух. Например, если в качестве аргументов переданы 7 и 12, то функция должна
вернуть 12. Примените функцию в программе, которая предлагает пользователю
ввести два целочисленных значения. Программа должна показать большее значении
из двух.
"""

def max(x, y):
    return x if x > y else y

def get_number(msg):
    while True:
        inp = input(msg)
        try:
            return int(inp)
        except:
            print('Please enter integer.')

def main():
    x = get_number('Input the first number: ')
    y = get_number('Input the second number: ')
    print('\nResult:')
    print(f'The number {max(x, y)} is greater.')

if __name__ == '__main__':
    main()
