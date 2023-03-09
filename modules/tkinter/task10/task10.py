# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите программу, моделирующую бросок игрального кубика. В программе должна
быть одна кнопка с текстом 'Roll'. Когда пользователь щелкает на кнопке,
должно выводиться случайное целое число от 1 до 6.
"""

import random
import tkinter as tk

# set random number from 1 to 6 to Label
def roll():
    new_number = random.randint(1, 6)
    lbl['text'] = f'{new_number}'

# create window
window = tk.Tk()
# configure window grid
window.rowconfigure([0, 1], weight=1, minsize=50)
window.columnconfigure(0, weight=1, minsize=100)
# create button
btn = tk.Button(text='Roll', command=roll)
btn.grid(row=0, column=0, sticky='nsew')
# create label
lbl = tk.Label(text='1')
lbl.grid(row=1, column=0)

window.mainloop()
