# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

1.Имеется веб-страница http://olympus.realpython.org/login с помощью класса
StatefulBrowser() модуля mechanicalsoup откройте данный url. Выведите на
экран текущий url и HTML полученной страницы.
2.Получите форму, подставьте следующие значения:
    логин: zeus
    пароль: ThunderDude
и програмно нажмите submit. Выведите текстовый ответ и новый url, который
вернет вам сервер после этого.
3.Проделайте все то же, но с помощью класса Browser.
"""

import mechanicalsoup

url = "http://olympus.realpython.org/login"

# 1
print('Task 1:')
# create instance browser
browser = mechanicalsoup.StatefulBrowser()
# open url
browser.open(url)
# output url and HTML
print('url: ', browser.url)
print('*' * 45)
print('HTML:')
print('-' * 45)
print(browser.page)
print('*' * 45)

# 2
print('Task 2:')
print('Get form')
print('-' * 45)
# select form with selector
browser.select_form('form[action="/login"]')
# show selected
print(browser.form.print_summary())
# set new values to input
print('-' * 45)
print('Set values')
browser['user'] = 'zeus'
browser['pwd'] = 'ThunderDude'
# submit form
print('-' * 45)
print('Submit')
response = browser.submit_selected()
# show response and new url
print('*' * 45)
print('Response:')
print('-' * 45)
print(response.text)
print('*' * 45)
print('Response url:', response.url)
print('Browser url:', browser.url)

# 3
print('-' * 45)
print('Task 3 (Perform the same task using the browser class):')
print('-' * 45)
# create instance Browser
browser = mechanicalsoup.Browser()
# get page
login_page = browser.get(url)
# get html
login_html = login_page.soup
# output html
print('HTML:\t')
print(login_html)
print('*' * 45)
# get form
print('Get form and set new values')
print('-' * 45)
form = login_html.select('form')[0]
print(form)
form.select('input')[0]['value'] = 'zeus'
form.select('input')[1]['value'] = 'ThunderDude'
# submit
print('-' * 45)
print('Submit')
profiles_page = browser.submit(form, login_page.url)
print('*'* 45)
# parameters of the received page
print('New url:', profiles_page.url)
print('*' * 45)
print('New HTML:')
print('-' * 45)
print(profiles_page.soup)
