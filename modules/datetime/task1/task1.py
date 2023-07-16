# -*- coding: utf-8 -*-

'''
[Программирование на Python в примерахи задачах. Васильев А.Н. (2021)]
Напишите программу в которой иллюстрируются способы создания объекта time
'''

import datetime

# Объект для реализаци момента времени
mytime = datetime.time(13, 35, 20)
# Проверка результата
print('Время:', mytime)
# Использование полей объекта
print('Часы:', mytime.hour)
print('Минуты:', mytime.minute)
print('Секунды:', mytime.second)
# Создвние нового объекта на основе существующего
newtime = mytime.replace(15, second=45)
# Проверка результата
print('Время:', newtime)
# Создание нового объекта
mytime = datetime.time.fromisoformat('12:34:56')
# Проверка результата
print('Время:', mytime)
