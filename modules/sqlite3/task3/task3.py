# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

1.Создайте новую базу данных, содержащую таблицу Roster. Таблица состоит из
трех полей: Name, Species и Age. Столбцы Name и Species должны быть
текстовыми, а столбец Age должен быть целочисленным полем.

2.Заполните созданную таблицу следующими значениями:
NAME               SPECIES              AGE
Benjamin Sisko     Human                40
Jadzia Dax         Trill                300
Kira Nerys         Bajoran              29

3.Обновите поле Name записи Jadzia Dax, чтобы оно содержало значение Ezri Dax.

4.Выведите значения Name и Age для всех строк данных, у которых поле Species
содержит значение Bajoran.
"""

import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def get_data():
    cursor.execute('SELECT * FROM Roster')
    for row in cursor.fetchall():
        print(row)

# 1
print('Task 1:')
print('Create table')
sql = """CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INT
);"""
cursor.execute(sql)
print()


# 2
print('Task 2:')
print('Insert data into table')
data = (
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
)
cursor.executemany('INSERT INTO Roster VALUES (?, ?, ?);', data)
print('Result:')
get_data()
print()

# 3
print('Task 3:')
print('Update table. Jadzia Dax is replaced by Ezri Dax.')
sql = "UPDATE Roster SET Name=? WHERE Name=?;"
cursor.execute(sql, ('Ezri Dax', 'Jadzia Dax'))
print('Result:')
get_data()
print()

# 4
print('Task 4:')
print('Select name and age where Species = Bajoran')
sql = "SELECT Name, Age FROM Roster WHERE Species='Bajoran'"
cursor.execute(sql)
print('Result:')
for row in cursor.fetchall():
    print(row)
