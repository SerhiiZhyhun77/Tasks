# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите программу, которая читает числа в файле numbers.csv из текущего 
каталога в список списков. Результат должен выглядеть так:

[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13,14, 15]]

"""

import pathlib, csv

# create file_path
file_path = pathlib.Path.cwd() / 'numbers.csv'

# open file
file = file_path.open(mode = 'r', encoding = 'utf-8', newline = '')
reader = csv.reader(file)

# read data to list
numbers = []
for row in reader:
    # string ->  integer
    int_row = [int(n) for n in row]
    # add to list
    numbers.append(int_row)

# close file
file.close()

# show result
print(numbers)
