# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Создайте базу данных test_database.db
1.Создайте в базе таблицу People с полями:
    FirstName,
    LastName,
    Age
Добавьте в эту таблицу значения
    'Ron',
    'Obvious',
    42
2.Прочитайте и выведите на экран значения из таблицы People.
3.Добавьте в таблицу People несколько значений
    people_values = (
            ('Den', 'Palmer', 33),
            ('Luigi', 'Vercotti', 43),
            ('Arthur', 'Belling', 28)
        )
одной командой .executemany() параметризированной командой.
4.Выведите все данные таблицы People.
"""

import sqlite3

with sqlite3.connect('test_database.db') as connection:
    cursor = connection.cursor()
    # 1
    print('Task 1:')
    # sql for create table
    create_table = """
    CREATE TABLE IF NOT EXISTS People(
        FirstName TEXT,
        LastName TEXT,
        Age INT
    );"""
    # sql for insert values
    insert_values = """
    INSERT INTO People VALUES(
        'Ron',
        'Obvious',
        42
    );"""
    # execute sql
    print('\tCreate table People')
    cursor.execute(create_table)
    print('\tInsert values')
    cursor.execute(insert_values)
    # commit changes
    connection.commit()  # not necessary
    print()

    # 2
    print('Task 2:')
    # sql for get data from table People
    query = "SELECT * FROM People;"
    #execute sql
    results = cursor.execute(query)
    print('\t Get row from table')
    row = results.fetchone()
    print('\t -> ', row)
    print()

    # 3
    print('Task 3:')
    # data for adding to db
    people_values = (
        ('Den', 'Palmer', 33),
        ('Luigi', 'Vercotti', 43),
        ('Arthur', 'Belling', 28)
    )
    # insert many data to table
    print('\tInsert many data to table')
    cursor.executemany('INSERT INTO People VALUES(?, ?, ?)', people_values)
    print()

    # 4
    print('Task 4:')
    # select all data from table People
    print('\tGet all data from table')
    cursor.execute('SELECT * FROM People')
    # output all data
    print('\tData from People:')
    for row in cursor.fetchall():
        print('\t -> ', row)
