# -*- coding: utf-8 -*-

"""ЗАДАЧА: НОМЕРА СТРОК
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая запрашивает у пользователя имя файла. Программа
должна вывести на экран содержимое файла, при этом каждая строка должна
предваряться ее номером и двоеточием. Нумерация строк должна начинаться с 1.
"""

def main():
    file_name = input('Enter file name: ')
    try:
        with open(file_name, 'r') as f:
            for n, line in enumerate(f):
                print(f'{n + 1}:', line, end='')
    except FileNotFoundError:
        print(f'An error occurred while trying to read the file {file_name}')

if __name__ == '__main__':
    main()
