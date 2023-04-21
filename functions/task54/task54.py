# -*- coding: utf-8 -*-

'''ЗАДАЧА: МАГИЧЕСКИЙ КВАДРАТ ЛО ШУ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Магический квадрат Ло Шу представляет собой таблицу с 3 строками и 3
столбцами. Он имеет свойства:
    - таблица содержит числа строго от 1 до 9;
    - сумма каждой строки, каждого столбца и каждой диагонали в итоге
    составляет одно и то же число.

Магический квадрат можно сымитировать в программе при помощи двумерного
списка. Напишите функцию, которая принимает двумерный список в качестве
аргумента и определяет, является ли список магическим квадратом Ло Шу.
Протестируйте функцию в программе.
'''

def is_magic_square(square):
    # add rows to list
    lines = [row for row in square]
    # add columns to list
    for i in range(3):
        line = [square[j][i] for j in range(3)]
        lines.append(line)
    # add diag to list
    line = [square[j][i] for i in range(3) for j in range(3) if i == j]
    lines.append(line)
    line = [square[j][i] for i in range(3) for j in range(3) if i + j == 2]
    lines.append(line)

    # check for magic
    summ = None
    for line in lines:
        if summ is None:
            summ = sum(line)
        else:
            if summ != sum(line):
                return False
    return True

def output(square, status):
    print('The list:')
    for line in square:
        print(*line)
    if status:
        print('is magic square Luoshu.')
    else:
        print('is not magic square Luoshu.')
    print()

def main():
    square = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ]
    output(square, is_magic_square(square))

if __name__ == '__main__':
    main()
