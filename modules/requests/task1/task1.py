# -*- coding: utf-8 -*-

"""
[Простой Python. Билл Любанович (2016)]
С помощью библиотеки requests обратитесь к какой-нибудь веб-странице,
выведите ответ сервера и содержимое страницы.
"""

import requests
# url
url = 'https://anekdotikov.net/anekdot/random/'
# get page
resp = requests.get(url)
# output server response
print(resp)
# output html
print(resp.text)
