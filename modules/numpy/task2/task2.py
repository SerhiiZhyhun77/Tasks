# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

"""

import numpy as np

# 1
print('Create matrix A and B')
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])
print('A:')
print(A)
print('B:')
print(B)
print()

#2
print('Vertical stack A & B:')
print(np.vstack([A, B]))
print()

# 3
print('Horizontal stack A & B:')
print(np.hstack([A,B]))
print()

# 4
print('Reshape A (6, 1):')
print(A.reshape(6, 1))
print()

# 5
print('Get array with arange(1,10):')
nums = np.arange(1, 10)
print(nums)
print('Reshape(3, 3):')
matrix = nums.reshape(3, 3)
print(matrix)