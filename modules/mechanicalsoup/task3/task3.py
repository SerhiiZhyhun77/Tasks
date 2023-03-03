# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Страница http://olympus.realpython.org/dice моделирует бросок шестигранного
кубика, результат обновляется при каждом обновлении браузера. Напишите
программу, которая получит 4 значения броска и текущее время его получения с
интервалом 10 секунд. Время можно получить из части строки внутри тега<p>,
следующего после результата броска в HTML-коде страницы.
"""

import mechanicalsoup
import time

# url
url = 'http://olympus.realpython.org/dice'
# create browser
browser = mechanicalsoup.Browser()
# repeat 4 times
for i in range(4):
    # get url
    page = browser.get(url)
    # get tags
    tag_number = page.soup.select('#result')[0]
    tag_time = page.soup.select('#time')[0]
    # get texts from tags
    number = tag_number.text
    time_ = tag_time.text
    # ouput
    print('-' * 50)
    print(i + 1, ':')
    print(f'The result of your dice roll is: {number}.')
    print(f'The value was received at {time_}')
    # wait 10 seconds, if this is not the last dice
    if i < 3:
        time.sleep(10)
