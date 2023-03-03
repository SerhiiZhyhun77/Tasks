# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Постройте столбчатую диаграмму, у которой центры столбцов находятся в точках
1, 2, 3, 4 и 5 по оси х с высотами 2, 4, 6, 8 и 10 соответственно.
"""

from matplotlib import pyplot as plt
import numpy as np

centers = np.arange(1, 6)
tops = np.arange(2, 12, 2)
plt.bar(centers, tops)
plt.show()