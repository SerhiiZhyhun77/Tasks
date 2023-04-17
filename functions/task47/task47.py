# -*- coding: utf-8 -*-

'''ЗАДАЧА: ПРОГРАММА АНАЛИЗА ЧИСЕЛ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Разработайте программу, которая просит пользователя ввести ряд из 20 чисел.
Программа должна сохранить числа в списке и затем показать приведенные ниже
данные:
    - наименьшее число в списке;
    - наибольшее число в списке;
    - сумму чисел в списке;
    - среднее арифметическое значение чисел в списке.
'''

import statistics

def get_nums():
    while True:
        s = input('Enter a string of 20 numbers separated by spaces: ')
        num_lst = s.split()
        try:
            num_lst = [float(n.strip()) for n in num_lst]
            if len(num_lst) == 20:
                return num_lst
            else:
                print(f'You entered {len(num_lst)} numbers.')
        except Exception:
            print('You are mistaken!')


def main():
    num_lst = get_nums()
    print()
    print(f'Minimum number in the list: {min(num_lst)}')
    print(f'Maximum number in the list: {max(num_lst)}')
    print(f'Sum of numbers: {sum(num_lst)}')
    print(f'Average: {statistics.mean(num_lst)}')

if __name__ == '__main__':
    main()
