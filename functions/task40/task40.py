# -*- coding: utf-8 -*-

"""ЗАДАЧА: СЧЕТЧИК ЗНАЧЕНИЙ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Допустим, что файл с серией имен (в виде строковых значений) называется
names.txt и существует на диске компьютера. Напишите программу, которая
показывает количество хранящихся в файле имен. (Подсказка: откройте файл и
прочитайте каждую хранящуюся в нем строку. Используйте переменную для
подсчета количества прочитанных из файла значений.)
"""

def main():
    file_name = 'names.txt'
    try:
        f = open(file_name, 'r')
        n = 0
        for line in f:
            n += 1
        print(f'The file contains {n} names:')
        f.seek(0)
        for line in f:
            print('-',line, end='')
    except Exception as err:
        print(err)
    else:
        f.close()

if __name__ == '__main__':
    main()
