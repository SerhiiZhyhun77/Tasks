# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

1.Получите содержимое страницы http://olympus.realpython.org/profiles/aphrodite
2.С помощью .find() получите значение тега title.
"""

from urllib.request import urlopen

# 1
print('Task 1:')
url = 'http://olympus.realpython.org/profiles/aphrodite'
# get page
print('Get page')
page = urlopen(url)
# read page
print('Read page')
html_bytes = page.read()
# decode
print('Decode')
html = html_bytes.decode('utf-8')
# output
print('Result:')
print(html)
print()

# 2
print('Task 2:')
print('Get title with .find()')
title_index = html.find('<title>')
start_index = title_index + len('<title>')
print('Start index =', start_index)
end_index = html.find('</title>')
print('End index =', end_index)
title = html[start_index:end_index]
print('Result:')
print(title)
