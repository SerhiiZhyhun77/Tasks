# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите программу, которая записывает следующий список списков в файл 
numbers.csv в текущей директории

numbers = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]

"""

import pathlib, csv

# data for write
numbers = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]

# create file_path
file_path = pathlib.Path.cwd() / 'numbers.csv'
# open file
file = file_path.open(mode = 'w', encoding = 'utf-8', newline = '')
writer = csv.writer(file)
# write data
writer.writerows(numbers)
# close file
file.close()
# show message
print('All data has been written to a file numbers.csv')
print(f'Path to the file:\n{str(file_path)}')
