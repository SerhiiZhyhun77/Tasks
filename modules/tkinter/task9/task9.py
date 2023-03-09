# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите программу, которая выводит одну кнопку с цветом фона по умолчанию и
черным текстом "Click me". Когда пользователь щелкнет на кнопке, ее фон
должен окрашиваться в цвет, случайным образом выбранный из следующего списка:
    ['red', 'orange', 'yellow', 'blue', 'indigo', 'violet']
"""

import tkinter as tk
import random

# set of colors
colors = ['red', 'orange', 'yellow', 'blue', 'indigo', 'violet']

# changer background color
def chng_bg():
    color = random.choice(colors)
    btn['bg'] = color

# create window
window = tk.Tk()
# create button
btn = tk.Button(
    text='Click me',
    fg='black',
    command=chng_bg
)
btn.pack()

window.mainloop()