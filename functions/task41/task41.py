# -*- coding: utf-8 -*-

"""ЗАДАЧА: СУММА ЧИСЕЛ И СРЕДНЕЕ АРИФМЕТИЧЕСКОЕ ЧИСЕЛ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Допустим, что файл с рядом целых чисел называется numbers.txt и существует на
диске компьютера. Напишите программу, которая читает все хранящиеся в файле
числа, вычисляет их сумму и среднее арифметическое.
"""
from statistics import mean

def main():
    file_name = 'numbers.txt'
    try:
        f = open(file_name, 'r')
        num_lst = [int(n) for n in f]
        print(f'Numbers read: \n{num_lst}')
        print(f'Sum of numbers: {sum(num_lst)}')
        print(f'Average of numbers: {mean(num_lst)}')
    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()
