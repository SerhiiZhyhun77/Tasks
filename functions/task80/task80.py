# -*- coding: utf-8 -*-

'''ЗАДАЧА: РЕКУРСИВНЫЕ СТРОКИ
[Начинаем программировать на Python. Тони Гэддис (2022)]
Напишите рекурсивную функцию, которая принимает целочисленный аргумент n.
Данная функция должна вывести на экран n строк, состоящих из звездочек; при
этом первая строка должна показать 1 звездочку, вторая строка - 2 звездочки и
так до n-й строки, которая должна показать n звездочек.
'''


def stars_in_line(n):
    if n < 2:
        print('*')
        return
    stars_in_line(n - 1)
    print('*' * n)
    return


def main():
    n = 20
    stars_in_line(n)


if __name__ == '__main__':
    main()
