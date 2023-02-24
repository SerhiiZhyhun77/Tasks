# -*- coding: UTF-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Подключитесь к базе даных в памяти. Создайте и выполните запрос к базе даных,
который вернет текущую дату и время.
"""

import sqlite3
# create connection with db in memory
connection = sqlite3.connect(':memory:')
# create cursor
cursor = connection.cursor()
# create sql request
query = "SELECT datetime('now', 'localtime');"
# execute request
results = cursor.execute(query)
# ger result row
row = results.fetchone()
# extract time
time = row[0]
# print
print(time)
# close connection
connection.close()
