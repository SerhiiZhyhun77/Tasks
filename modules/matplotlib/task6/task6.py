# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Постройте гистограмму десяти тысяч случайных чисел с нормальным
распределением, сгруппированных по 20 категориям. Для генерирования случайных
чисел используйте функцию randn() из модуля NumPy random. Она возвращает
массив случайных чисел с плавающей точкой, многие из которых близки к нулю.
"""

from matplotlib import pyplot as plt
from numpy import random

plt.hist(random.randn(10000), 20)
plt.show()