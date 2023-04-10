# -*- coding: utf-8 -*-

"""ЗАДАЧА: ПРОГРАММА ЗАПИСИ И ЧТЕНИЯ ФАЙЛОВ СО СЛУЧАЙНЫМИ ЧИСЛАМИ
[Начинаем программировать на Python. Тони Гэддис (2022)]

1.Напишите программу, которая пишет в файл ряд случайных чисел. Каждое
случайное число должно быть в диапазоне от 1 до 500. Приложение должно
предоставлять пользователю возможность назначать количество случайных чисел,
которые будут содержаться в файле.

2.Напишите программу, которая читает случайные числа из файла, выводит их на
экран и затем показывает приведенные ниже данные:
    - сумму чисел;
    - количество случайных чисел, прочитанных из файла.
"""

import random

# 1
print('Task 1:')
# get number of numbers
while True:
    n = input('How many random numbers to write to the file? ')
    if n.isnumeric():
        break
    else:
        print('Please enter positive integer.')

n = int(n)
# generate a list of random numbers
print('Generate list of random numbers')
rnd_num_lst = [random.randint(1, 500) for i in range(n)]
print(rnd_num_lst)
# write numbers to file
print('Write numbers to file "numbers.txt"')
f = open('numbers.txt', 'w')
for n in rnd_num_lst:
    f.write(f'{n}\n')
f.close()
print()

# 2
print('Task 2:')
print('Read numbers from file "numbers.txt"')
try:
    f = open('numbers.txt', 'r')
    num_lst = [int(n.rstrip()) for n in f]
except Exception as err:
    print(err)
else:
    f.close()

if num_lst:
    print(num_lst)
    print(f'Sum of numbers: {sum(num_lst)}')
    print(f'Amount of numbers: {len(num_lst)}')
