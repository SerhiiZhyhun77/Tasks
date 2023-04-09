# -*- coding: utf-8 -*-

"""ЗАДАЧА: ВЫВОД НА ЭКРАН ВЕРХНЕЙ ЧАСТИ ФАЙЛА
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая запрашивает у пользователя имя файла. Программа
должна вывести на экран только первые пять строк содержимого файла. Если в
файле меньше пяти строк, то она должна вывести на экран все содержимое файла.
"""

def main():
    file_name = input('Enter file name: ')
    try:
        f = open(file_name, 'r')
        n = 1
        line = f.readline()
        while line and n <= 5:
            print(line, end='')
            line = f.readline()
            n += 1
    except IOError:
        print(f'An error occurred while trying to read the file {file_name}')
    else:
        f.close()

if __name__ == '__main__':
    main()
