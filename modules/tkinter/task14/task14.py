# -*- coding: utf-8 -*-

"""
[Python для детей. Джейсон Бриггс (2017)]

Используя модуль tkinter нарисуйте на холсте треугольник и реализуйте его
управление с помощью клавиш со стрелками.
"""

from tkinter import *

window = Tk()

canvas = Canvas(window, width=400, height=400)
canvas.pack()

canvas.create_polygon(10, 10, 10, 60, 50, 35)

def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)

canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)

window.mainloop()