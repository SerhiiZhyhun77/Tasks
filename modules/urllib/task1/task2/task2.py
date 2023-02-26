# -*- coding: utf-8 -*-

"""ИЗВЛЕЧЕНИЕ ТЕКСТА ИЗ HTML С ИСПОЛЬЗОВАНИЕМ РЕГУЛЯРНЫХ ВЫРАЖЕНИЙ
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Получите содержимое страницы http://olympus.realpython.org/profiles/dionysus
Получите содержимое тега title. Так как страница написана очень неаккуратно,
воспользуйтесь регулярными выражениями.
"""

import re
from urllib.request import urlopen

# url
url = 'http://olympus.realpython.org/profiles/dionysus'
# get html
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('utf-8')
# make a pattern
pattern = '<title.*?>.*?</title.*>'
# get matches
match_results = re.search(pattern, html, re.IGNORECASE)
# title with tags
title = match_results.group()
# del tags
title = re.sub('<.*?>', '', title)
# output
print('Result:')
print(title)
