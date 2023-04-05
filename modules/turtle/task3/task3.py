# -*- coding: utf-8 -*-

"""ЗАДАЧА: ПРЯМОУГОЛЬНЫЙ УЗОР
[Начинаем программировать на Python. Тони Гэддис (2022)]

В программе напишите функцию drawPattern, которая использует библиотеку
черепашьей графики, чтобы нарисовать прямоугольный узор. Функция drawPattern
должна принимать два аргумента: один из них задает ширину узора, другой - его
высоту. Когда программа выполняется, она должна запросить у пользователя
ширину и высоту узора и затем передать эти значения в качестве аргументов в
функцию drawPattern.
"""

import turtle as t

def drawPattern(width, height):
    # func for draw rectangle
    def make_rect(side_x, side_y, fill=False):
        t.pendown()
        if fill:
            t.begin_fill()
        for i in range(2):
            t.forward(side_x)
            t.right(90)
            t.forward(side_y)
            t.right(90)
        if fill:
            t.end_fill()
        t.penup()

    # func for draw line
    def make_line(x1, y1, x2, y2):
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)
        t.penup()

    step_x = width / 2 / 4
    step_y = height / 2 / 4
    t.penup()
    t.width(2)
    # 1-st rect
    t.goto(-step_x * 4, step_y * 4)
    make_rect(step_x * 8, step_y * 8)
    # 2-nd rect
    t.goto(-step_x * 3, step_y * 3)
    make_rect(step_x * 6, step_y * 6)
    # 3-rd rect
    t.goto(-step_x * 2, step_y * 2)
    make_rect(step_x * 4, step_y * 4, True)
    # lines
    make_line(-step_x * 4, step_y * 4, step_x * 4, -step_y * 4)
    make_line(-step_x * 4, -step_y * 4, step_x * 4, step_y * 4)
    make_line(-step_x *4, 0, step_x * 4, 0)
    make_line(0, step_y * 4, 0 , -step_y * 4)
    
def inp(msg):
    while True:
        x = input(msg)
        if x.isnumeric():
            return int(x)
        print('Please enter positive integer.')

def main():
    # get size
    width = inp('Enter width: ')
    height = inp('Enter height: ')
    # draw
    drawPattern(width, height)
    t.hideturtle()
    t.exitonclick()

if __name__ == '__main__':
    main()
