# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите программу создающую три фрейма с выравниванием по левому краю и
возможностью масштабирования при разворачивании окна. Параметры фреймов:
    1.Ширина - 200 текстовых единиц, высота - 100, цвет - красный.
    2.Ширина - 100, цвет - желтый.
    3.Ширина - 50, цвет - синий.
Используйте менеджер геометрии .pack()
"""

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=200, height=100, bg='red')
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg='yellow')
frame2.pack(fill=tk.BOTH, side=tk.LEFT,expand=True)

frame3 = tk.Frame(master=window, width=50, bg='blue')
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()
