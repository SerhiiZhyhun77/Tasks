# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

Напишите программу для создания фрейма шириной 200 текстовых единиц и
высотой - 100 с зеленым фоном. Расположите в этом фрейме две метки:
    1.Текст - "I'm at (0, 0)", фон - красный. Координаты: х=0, у=0.
    2.Текст - "I'm at (75, 75)", фон - желтый. Координаты: х=75, у=75.
Для позиционирования виджетов используйте менеджер геометрии .place()
"""

import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window, width=200, height=100, bg='green')
frame.place(x=0, y=0)

label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg='red')
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg='yellow')
label2.place(x=75, y=75)

window.mainloop()
