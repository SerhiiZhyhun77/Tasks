# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

1.Напишите программу, которая извлекает весь HTML-код веб-страницы
http://olympus.realpython.org/profiles.

2.Используя Beautiful Soup, выделите список всех ссылок на странице -
проведите поиск тегов HTML с именем a и получите значение атрибута href для
каждого тега.

3.Извлеките HTML-код каждой страницы в списке - добавьте полный путь к файлу
и выведите текст (без тегов HTML) на каждой странице, используя метод
.get_text() из библиотеки Beautiful Soup.
"""

import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://olympus.realpython.org/profiles'
host = 'http://olympus.realpython.org'

def get_html(url):
    page = urlopen(url)
    return page.read().decode('utf-8')

def get_text_from_html(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    text = re.sub(r'\n{1,}', r'\n', text)
    return text

html = get_html(url)
soup = BeautifulSoup(html, 'html.parser')

# 1
print('Task 1:')
print('Get HTML from page:')
print('*' * 30)
print(html)
print('*' * 30)

# 2
print('Task 2:')
print('Get all links from HTML:')
links = soup.find_all('a')
url_lst = []
for link in links:
    print(link)
    href = link['href']
    url_lst.append(host+href)
    print('\tLink ->', href)
print('*' * 30)

# 3
print('Task 3:')
print('Get texts from all url')

for url in url_lst:
    print('URL: ', url)
    print(get_text_from_html(url))
    print('*' * 30)
