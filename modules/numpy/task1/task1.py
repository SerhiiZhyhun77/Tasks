# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]
1.Создайте матрицу A [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
2.Создайте матрицу B [[5, 4, 3], [7, 6, 5], [9, 8, 7]].
3.Умножте матрицу А на 2.
4.C = B - A
5.D = A * B
6.Получите кортеж длин осей А.
7.Получите массив диагональных элементов А.
8.Получите одномерный массив всех записей А.
9.Проведите транспонирование А.
10.Вычислите минимум А.
11.Вычислите максимум А.
12.Вычислите среднее значение всех элементов А.
13.Вычислите сумму всех элементов А.
"""

import numpy as np

# 1
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('A:')
print(A)
print()

# 2
B= np.array([[5, 4, 3], [7, 6, 5], [9, 8, 7]])
print('B:')
print(B)
print()

# 3
print('2 * A:')
print(2 * A)
print()

# 4
print('C = B - A:')
C = B - A
print(C)
print()

# 5
print('D = A * B:')
D = A * B
print(D)
print()

# 6
print('Matrix A shape:')
print(A.shape)
print()

# 7
print('Matrix A diagonal:')
print(A.diagonal())
print()

# 8
print('Matrix A flatten:')
print(A.flatten())
print()

# 9
print('Matrix A transpose:')
print(A.transpose())
print()

# 10
print('Matrix A min:')
print(A.min())
print()

# 11
print('Matrix A max:')
print(A.max())
print()

# 12
print('Matrix A mean (average):')
print(A.mean())
print()

# 13
print('Matrix A sum:')
print(A.sum())
print()
