# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите программу создающую окно с фреймами в сетке 3х3, с выпуклой границей
шириной 1 пиксель. В каждый фрейм упакуйте виджеты Label c текстом
указывающим номер строки и номер столбца. Внешние отступы фреймов и Label
равны 5 пикселей. С помощью .columnconfigure() и .rowconfigure() настройте
пропорциональное изменение размеров сетки при изменении размеров окна.
"""

import tkinter as tk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f'Row {i}\nColumn {j}')
        label.pack(padx=5, pady=5)

window.mainloop()
