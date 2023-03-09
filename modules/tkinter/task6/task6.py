# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите программу, которая используя менеджер геометрии .grid() создает
сетку 1х4 минимальной шириной 50. В каждую ячейку добавьте Label с текстом -
номер ячейки. Воспользуйтесь атрибутом позиционирования sticky, чтобы задать:
    label1 - не позиционировать;
    label2 - заполнение по горизонтали;
    label3 - заполнение по вертикали;
    label4 - заполнение всей ячейки.
"""

import tkinter as tk

window = tk.Tk()

window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)

label1 = tk.Label(text='1', bg='black', fg='white')
label2 = tk.Label(text='2', bg='black', fg='white')
label3 = tk.Label(text='3', bg='black', fg='white')
label4 = tk.Label(text='4', bg='black', fg='white')

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky='ew')
label3.grid(row=0, column=2, sticky='ns')
label4.grid(row=0, column=3, sticky='nsew')

window.mainloop()
