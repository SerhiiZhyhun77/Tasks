# -*- coding: utf-8 -*-

"""
[Знакомство с PYTHON. Дэн Бейдер, Дэвис Эймос (2023)]

1.Напишите программу, которая выводит виджет Button шириной 50 текстовых
единиц и высотой 25 текстовых единицю Виджет должен именть белый фон с синим
текстом "Click here".
2.Напишите программу для вывода виджета Entry шириной 40 текстовых единиц,
с белым фоном и черным текстом. Используйте метод .insert() для вставки
текста "What is your name?".
"""

import tkinter as tk

window = tk.Tk()

# 1
btn = tk.Button(master=window,
                text='Click here',
                width=50,
                height=15,
                bg='white',
                fg='blue')
btn.pack()

# 2
ent = tk.Entry(
    master=window,
    width=40,
    bg='white',
    fg='black'
)
ent.insert(0, 'What is your name?')
ent.pack()

window.mainloop()
