# -*- coding: utf-8 -*-

"""
[Простой Python. Билл Любанович (2016)]

Используя фреймворк Flask и систему шаблонов jinja2 напишите тестовый сервер,
которы будет получать параметры и подставлять их в шаблон веб-страницы.
Реализуйте это двумя способами:
    1.Передачей параметров в URL: /echo/<thing>/<place>
    2.Передачей в параметрах URL:/echo2/?thing=<thing>&place=<place>

HTML-шаблон имеет следующий код:
<html>
<head>
    <title>Flask2 Example</title>
</head>
<body>
Say hello to my little friend: {{ thing }}
Alas, it just destroyed {{ place }}
</body>
</html>
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/echo/<thing>/<place>')
def echo(thing, place):
    return render_template('flask2.html', thing=thing, place=place)

@app.route('/echo2/')
def echo2():
    thing = request.args.get('thing')
    place = request.args.get('place')
    return render_template('flask2.html', thing=thing, place=place)

app.run(port=9999, debug=True)