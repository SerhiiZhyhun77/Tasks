# -*- coding: utf-8 -*-

"""
[Простой Python. Билл Любанович (2016)]

Используя фрейворк Bottle создайте тестовый веб-сервер, который будет
возвращать 3 страницы:
    1.Главная страница по адресу localhost:9999 - возвращает отдельный
    HTML-файл, который называется index.html и содержит такую строку:
    My <b>new</b> and <i>improved</i> home page!!!

    2.Страница localhost:9999/about - возвращает простой текст:
    'This is about page.'

    3.Страница localhost:9999/echo/<thing> - возвращает текст:
    'Say hello to my little friend: <thing>', где <thing> означает, что все,
    что находится в URL после /echo/, присваивается строковому агрументу thing.
"""

from bottle import route, run, static_file

@route('/')
def home():
    return static_file('index.html', root='.')

@route('/about')
def about():
    return 'This is about page.'

@route('/echo/<thing>')
def echo(thing):
    return 'Say hello to my little friend: %s' % thing

run(host='localhost', port=9999)