# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Постройте графики которые показывают сколько материала о языке Python было
изучено за первые 20 дней в результате чтения Real Python по сравнению с
другим веб-сайтом (условно Real Python = Other ** 2)
Чтобы на оси Х не отображались половины дней, задайте их принудительно
.xticks([0, 5, 10, 15, 20]). Задайте заголовок графика .title() и названия осей
.xlabel() и .ylabel(). Чтобы было понятно какой график к каким данным
относится, задайте .legend()
"""

from matplotlib import pyplot as plt
import numpy as np

days = np.arange(0, 21)
other_site, real_python = days, days ** 2
plt.plot(days, other_site)
plt.plot(days,real_python)
plt.xticks([0, 5, 10, 15, 20])
plt.xlabel('Days of Reading')
plt.ylabel('Amount of Python Learned')
plt.title('Python Learned Reading Real Python vs Other Site')
plt.legend(['Other Site', 'Real Python'])
plt.show()