# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

1.Используйте MechanicalSoup для предоставления правильного имени
пользователя ('zeus') и пароля ('ThunderDude') форме авторизации, находящейся
по адресу http://olympus.realpython.org/login.

2.Выведите заголовок текущей страницы, чтобы убедиться, что вы были
перенаправлены на страницу /profiles.

3.Используйте MechanicalSoup для возвращения к странице входа (вернитесь к
предыдущей странице).

4.Введите в форме авторизации неправильное имя пользователя и пароль, а затем
найдите в HTML-коде возвращенной веб-страницы текст "Wrong username or
password!", чтобы убедиться в том, что попытка входа завершилась неудачей.
"""

import mechanicalsoup

url = 'http://olympus.realpython.org/login'

# 1
print('Task 1:')
# create instance browser
browser = mechanicalsoup.StatefulBrowser()
# open
print('Open')
browser.open(url)
print('url:', browser.url)
# select form
print('Select form')
browser.select_form('form')
# set login and pass
print('Set login and pass')
browser['user'] = 'zeus'
browser['pwd'] = 'ThunderDude'
# submit form
print('Submit')
browser.submit_selected()
# new url
print('New url:', browser.url)

# 2
print('-' * 50)
print('Task 2:')
title = browser.page.title.get_text()
print('Title:', title)

# 3
print('-' * 50)
print('Task 3:')
browser.open(url)
title = browser.page.title.get_text()
print('New title:', title)
print('url:', browser.url)

# 4
print('-' * 50)
print('Task 4:')
# select form
print('Select form')
browser.select_form('form')
# set wrong login and pass
print('Set wrong login and pass')
browser['user'] = 'zzz'
browser['pwd'] = 'tunderdude'
# print(browser.form.print_summary())  # shows all fields of form
# submit
print('Submit')
browser.submit_selected()
print('*' * 50)
# show current url
print('Current url:', browser.url)
# find text
text = 'Wrong username or password'
html_str = str(browser.page)
if html_str.find(text):
    print('"Wrong username or password!" was founded!')
