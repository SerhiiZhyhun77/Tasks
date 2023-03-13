# -*- coding: utf-8 -*-

"""
[Простой Python. Билл Любанович (2016)]

Напишите программу, которая соберет все ссылки с веб-страниц, ссылки на
которые передаются в качестве входящих аргументов.
"""

import requests
from bs4 import BeautifulSoup as soup
import sys

def get_link(url):
    result = requests.get(url)
    page = result.text
    doc = soup(page, 'html.parser')
    links = [element.get('href') for element in doc.find_all('a')]
    return links

if __name__ == '__main__':
    for url in sys.argv[1 : ]:
        print('Links in', url)
        for num, link in enumerate(get_link(url), start=1):
            print(num, link)
        print()
