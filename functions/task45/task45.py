# -*- coding: utf-8 -*-

'''ЗАДАЧА: ГЕНЕРАТОР ЛОТЕРЕЙНЫХ ЧИСЕЛ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Разработаейте программу, которая генерирует семизначную комбинацию лотерейных
чисел. Программа должна сгенерировать семь случайных чисел, каждое в
диапазоне от 0 до 9, и присвоить каждое число элементу списка. Затем напишите
еще один цикл, который показывает содержимое списка.
'''

import random

def main():
    # 1
    num_lst = [random.randint(0, 9) for i in range(7)]
    # 2
    print('Random numbers:')
    for num in num_lst:
        print(num)

if __name__ == '__main__':
    main()