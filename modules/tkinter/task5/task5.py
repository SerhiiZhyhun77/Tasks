# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Используя менеджер геометрии .grid() создайте сетку ячеек 1х2, размер
каждой ячейки 250х100. В первой ячейке сетки разместите в правом верхнем углу
Label с текстом "А". Во второй ячейке - разместите в нижнем левом углу Label
с текстом "В".
"""

import tkinter as tk

window = tk.Tk()

window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text='A')
label1.grid(row=0, column=0, sticky='ne')

label2 = tk.Label(text='B')
label2.grid(row=1, column=0, sticky='sw')

window.mainloop()
