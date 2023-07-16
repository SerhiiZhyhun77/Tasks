# -*- coding: utf-8 -*-

'''
[Программирование на Python в примерахи задачах. Васильев А.Н. (2021)]
Напишите программу в которой иллюстрируются способы создания объекта datetime
'''

import datetime

# Объект для реализации даты и времени
md = datetime.datetime(2019, 10, 22, 13, 27, 45)
# Проверка результата
print('Дата и время:', md)
# Использование полей объекта
print('Год:', md.year)
print('Месяц:', md.month)
print('Чило:', md.day)
print('Часы:', md.hour)
print('Минуты:', md.minute)
print('Секунды:', md.second)
print()
# Определение дня недели
print('День недели (weekday 0 - 6):', md.weekday())
print('День недели (isoweekday 1 - 7):', md.isoweekday())
# Дата
d = md.date()
# Проверка результата
print('Дата:', d)
# Время
t = md.time()
# Проверка результата
print('Время:', t)
print()
# Создание нового объекта на основе существующего
print('Создание нового объекта на основе существующего')
nd = md.replace(1985, day=3, second=15)
# Проверка результата
print('Дата и время:', nd)
print()
# Создание нового объекта
print('Создание нового объекта на основе ISO формата')
nd = datetime.datetime.fromisoformat('1998-08-12 11:25:36')
# Проверка результата
print('Новая дата и время:', nd)
print()
# Объект для текущей даты и времени
td = datetime.datetime.today()
# Проверка результата
print('Сегодня и сейчас:', td)
print()
# Разность дат
print('Разность дат')
delta = md - td
# Проверка результата
print('Интервал времени:', delta)
print('Дни:', delta.days)
print('Секунды:', delta.seconds)
print('Интервал в секундах:', delta.total_seconds())
