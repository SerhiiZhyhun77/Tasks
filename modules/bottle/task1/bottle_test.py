# -*- coding: utf-8 -*-

"""
[Простой Python. Билл Любанович (2016)]

Напишите программу, которая с помощью модуля requests будет получать страницу
по адресу http://localhost:9999/echo/Mothra!
Если страница успешно получена и ее содержимое будет равно 'Say hello to my
little friend: Mothra!', вывести текст 'It worked! That almost never happens!'.
В противном случае вывести 'Angh, got this:' и текст полученой страницы.
"""

import requests

resp = requests.get('http://localhost:9999/echo/Mothra!')

if resp.status_code == 200 and \
    resp.text == 'Say hello to my little friend: Mothra!':
    print('It worked! That almost never happens!')
else:
    print('Angh, got this:', resp.text)