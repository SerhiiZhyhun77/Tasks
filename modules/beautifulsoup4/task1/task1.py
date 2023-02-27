# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите программу, которая извлекает весь код HTML веб-страницы по адресу
http://olympus.realpython.org/profiles/dionysus. С помощью модуля
BeautifulSoup:
    1.Получите тег title и его значение.
    2.Получите все текстовые значения на странице.
    3.Получите все теги изображений и разложите их на имя тега и ссылку на
    изображение.
    4.Найдите в html коде тег изображения имеющий ссылку /static/dionysus.jpg
"""

import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

# url
url = 'http://olympus.realpython.org/profiles/dionysus'
# get html
page = urlopen(url)
html = page.read().decode('utf-8')
# create instance soup with html parser
soup = BeautifulSoup(html, 'html.parser')

# 1
print('Task 1:')
print('Get title tag:')
print('\t->', soup.title)
print('Get title string')
print('\t->', soup.title.string)
print()

# 2
print('Task 2:')
# get all text from page
print('Get all text from html:')
text = soup.get_text()
text = re.sub(r'\n{1,}', r'\n', text)
print(text)
print()

# 3
print('Task 3:')
print('Get img tags:')
for img_path in soup.find_all('img'):
    print(img_path)
    print('\tTag name ->', img_path.name)
    print('\tLink ->', img_path['src'])
print()

# 4
print('Task 4:')
print('Find neccessery tag:')
print('\tTag name: img')
print('\tLink: /static/dionysus.jpg')
result = soup.find_all('img', src='/static/dionysus.jpg')
print('Result:')
print('\t->', result)
