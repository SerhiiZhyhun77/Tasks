# -*- coding: utf-8 -*-

"""
[Простой Python. Билл Любанович (2016)]

Создайте скелет сайта с помощью веб-сервера Flask. Убедитесь, что сервер
начинает свою работу по адресу localhost на стандартном порте 5000.

Добавьте функцию home() для обработки запросов к домашней странице. Пусть она
возвращает строку It's alive!

Создайте шаблон для jinja2, который называется home.html и содержит следующий
контент:

<html>
<head>
<title>It's alive!</title>
<body>
I'm of course referring to {{thing}}, which is {{height}} feel tall and {{
color}}.
</body>
</html>

Модифицируйте функцию home() вашего сервера, чтобы она использовала шаблон
home.html. Передайте ей три параметра для команды GET: thing, height и color.
"""

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    thing = request.args.get('thing')
    height = request.args.get('height')
    color = request.args.get('color')
    return render_template('home.html', thing=thing, height=height, color=color)

app.run(port=5000)
