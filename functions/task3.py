# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите функцию doubles(), которая получает число и увеличивает его вдвое.
Используйте doubles() в цикле, чтобы трижды увеличить вдвое число 2, в выводом
каждого результата в отдельной строке. Пример вывода:

4
8
16
"""

def doubles(number):
    return number * 2


def main():
    number = 2
    counter = 3
    while counter > 0:
        number = doubles(number)
        print(number)
        counter -= 1

if __name__ == '__main__':
    main()