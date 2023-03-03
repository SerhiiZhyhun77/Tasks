# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

С помощью numpy сгенерируйте массив data (1, 21). Функцией .reshape()
перестройте его в матрицу 5х4. Массив data должен содержать следующие значения:
array([[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16],
       [17, 18, 19, 20]])
Постройте графики по этим данным.
"""

from matplotlib import pyplot as plt
import numpy as np

data = np.arange(1, 21).reshape(5, 4)
plt.plot(data)
plt.show()
