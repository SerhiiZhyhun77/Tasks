# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

1.Напишите программу, которая извлекает весь код HTML веб-страницы по адресу
http://olympus.realpython.org/profiles/dionysus.

2.Используйте строковый метод .find() для вывода текста, следующего за Name:
и Favorite Color: (не включая начальные пробелы или завершающие теги HTML,
которые могут присутствовать в той же строке).

3.Повторите упражнение с регулярными выражениями. В конце каждого шаблона
следует поставить знак <(начало тега HTML) или символ новой строки,
а из полученного текста надо убрать все лишние пробелы и символы новой строки
при помощи строкового метода .strip().
"""

import re
from urllib.request import urlopen

# 1
print('Task 1:')
print('Get html from url')
# url
url = 'http://olympus.realpython.org/profiles/dionysus'
# get page
page = urlopen(url)
# get html
html = page.read().decode('utf-8')
print('Result:')
print(html)
print()

# 2
print('Task 2:')
# get Name
print('Get Name')
start_index = html.find('Name:')
start_index += len('Name:')
end_index = html.find('</h2>')
name = html[start_index : end_index].strip()
print('\tResult:')
print('\t\t->', name)
# get Favorite Color
print('Get Favorite Color')
start_index = html.find('Favorite Color:')
start_index += len('Favorite Color:')
end_index = html.find('</center')
favorite_color = html[start_index : end_index].strip()
print('\tResult:')
print('\t\t->', favorite_color)
print()

# 3
print('Task 3:')
# get Name
print('Get Name:')
# re pattern
pattern = "Name:(.*?)</h2>"
result_matches = re.findall(pattern, html, re.IGNORECASE)
name = result_matches[0].strip()
print('\tResult:')
print('\t\t->', name)
# get Favorite Color
print('Get Favorite Color')
# re pattern
pattern = r'Favorite Color:(.*)'
result_matches = re.findall(pattern, html, re.IGNORECASE)
favorite_color = result_matches[0].strip()
print('\tResult:')
print('\t\t->', favorite_color)
