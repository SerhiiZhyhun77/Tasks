# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите программу, которая создаст простую столбчатую диаграмму с центрами
столбцов в точках [1, 2, 3, 4, 5, 6] и вершинами [2, 4, 6, 8, 10, 12]
соответственно. Сохраните диаграмму в файл bar.png текущего каталога.
"""

from matplotlib import pyplot as plt
import numpy as np

xs = np.arange(1, 6)
tops = np.arange(2, 12, 2)

plt.bar(xs, tops)
plt.savefig('bar.png')
