# -*- coding: utf-8 -*-

'''
[Программирование на Python в примерахи задачах. Васильев А.Н. (2021)]
Напишите программу в которой иллюстрируются способы создания объекта date
'''

import datetime

# Способ 1
# Объект для реализации даты
myday = datetime.date(2019, 10, 22)
# Проверка результата
print('Первая дата:', myday)
# Использование полей объекта
print('Год:', myday.year)
print('Месяц:', myday.month)
print('Число:', myday.day)
print()
# Определение дня недели
print('Определяем день недели:')
print('День недели (weekday 0 - 6):', myday.weekday())
print('День недели (isoweekday 1 - 7):', myday.isoweekday())
print()

# Способ 2
# Создание нового объекта на основе существующего
newday = myday.replace(1985, day=15)
# Проверка результата
print('Вторая дата:', newday)
print()

# Способ 3
# Создание нового объекта
newday = datetime.date.fromisoformat('1988-08-12')
# Проверка результата
print('Новая дата:', newday)
print()

# Объект для текущей даты
thisday = datetime.date.today()
print('Сегодня:', thisday)

# Разность дат
delta = myday - thisday
# Проверка результата
print('До первой даты:', delta)
