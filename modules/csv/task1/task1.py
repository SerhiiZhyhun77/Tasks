# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

В текущей папке находится файл CSV scores.csv с данными обигроках и их 
показателях. Первые несколько строк выглядят так:

name,score
LLCoolDave,23
LLCoolDave,27
red,12
LLCoolDave,26
tom123,26

Напишите программу,которая читает данные из файла CSV и создает новый файл 
high_scores.csv, в котором каждая строка содержит имя игрока и его наиболее 
высокий результат.

Выходной файл CSV должен выглядеть примерно так:

name,high_score
LLCoolDave,27
red,12
tom123,26
O_O,22
Misha46,25
Empiro,23
MaxxT,25
L33tH4x,42
johnsmith,30
"""

import pathlib, csv

# create file_path and read data
file_path = pathlib.Path.cwd() / 'scores.csv'
with file_path.open(mode = 'r', encoding = 'utf-8', newline = '') as file:
    reader = csv.DictReader(file)
    
    # get all scores and sort
    scores = {}
    for row in reader:
        name, score = row['name'], row['score']
        if name in scores:
            if scores[name] < score:
                scores[name] = score
        else:
            scores[name] = score

# create new dictionaries in list
high_scores = []
for name, score in scores.items():
   new_dict = {}
   new_dict['name'] = name
   new_dict['high_score'] = score
   high_scores.append(new_dict)

#create file_path and write data
file_path = pathlib.Path.cwd() / 'high_scores.csv'
with file_path.open(mode = 'w', encoding = 'utf-8', newline = '') as file:
    writer = csv.DictWriter(file, fieldnames = ['name', 'high_score'])
    
    # write headers
    writer.writeheader()
    # write data
    writer.writerows(high_scores)
