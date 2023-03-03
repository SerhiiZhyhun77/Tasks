# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Постройте столбчатую диаграмму, на которой выводятся данные из словаря:
    fruits = {
    'apples' : 10,
    'orange' : 16,
    'bananas' : 9,
    'pears' : 4,
}
"""

from matplotlib import pyplot as plt

fruits = {
    'apples' : 10,
    'orange' : 16,
    'bananas' : 9,
    'pears' : 4,
}

plt.bar(fruits.keys(), fruits.values())
plt.show()
