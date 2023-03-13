# -*- coding: utf-8 -*-

"""
[Простой Python. Билл Любанович (2016)]

Используя фрейворк Flask создайте тестовый веб-сервер, который будет
возвращать 2 страницы:
    1.Главная страница по адресу localhost:9999 - возвращает отдельный
    HTML-файл, который называется index.html и содержит такую строку:
    My <b>new</b> and <i>improved</i> home page!!!

    2.Страница localhost:9999/echo/<thing> - возвращает текст:
    'Say hello to my little friend: <thing>', где <thing> означает, что все,
    что находится в URL после /echo/, присваивается строковому агрументу thing.
"""

from flask import Flask

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/echo/<thing>')
def echo(thing):
    return 'Say hello to my little friend: %s' % thing

app.run(port=9999, debug=True)