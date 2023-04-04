# -*- coding: utf-8 -*-

"""ЗАДАЧА: ФУНКЦИЯ РИСОВАНИЯ ТРЕУГОЛЬНИКА
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите функцию triangle, которая использует библиотеку черепашьей графики
для рисования треугольника. Функция должна принимать в качестве аргументов
координаты X и Y, сторон треугольника и цвет, которым треугольник должен быть
заполнен. Продемонстрируйте эту функцию в программе.
"""

import turtle as t
from random import randint, choice

def triangle(x, y, width, color):
    t.penup()
    t.goto(x, y)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    for count in range(3):
        t.forward(width)
        t.left(120)
    t.end_fill()

def main():
    colors = ['red', 'green', 'yellow', 'blue', 'grey', 'black']
    t.speed(0)
    for i in range(100):
        triangle(randint(-350, 350), randint(-350, 350), randint(1, 150),
                 choice(colors))
    t.exitonclick()

if __name__ == '__main__':
    main()
