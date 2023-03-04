# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Способствуют ли пираты глобальному потеплению? В текущей папке находится файл
CSV с данными о количестве пиратов и глобальной температуре. Напишите
программу для анализа связи между ними; программа должна читать файл pirates.csv
и строить график, на котором количество пиратов указано на оси х и
температура - на оси У. Добавьте заголовок и названия осей графиков,
затем сохраните полученный график в виде файла в формате PNG.
"""

import pathlib, csv
from matplotlib import pyplot as plt

# path to csv file
file_path = pathlib.Path('pirates.csv')
# read
with file_path.open(mode='r', encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    # get data
    temp_lst = []
    pirates_lst = []
    for i, row in enumerate(reader):
        if i == 0:
            _, y_lbl, x_lbl = row  # headers
        else:
            _, temp, pirates = row  # data
            temp_lst.append(temp)
            pirates_lst.append(pirates)

# build graph
plt.plot(pirates_lst, temp_lst)
plt.xlabel(x_lbl)
plt.xlabel(x_lbl)
plt.ylabel(y_lbl)
plt.title('Do pirates contribute to global warming?')
# save graph to file
plt.savefig('pirates_and_warming.png')