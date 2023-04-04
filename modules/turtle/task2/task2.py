# -*- coding: utf-8 -*-

"""ЗАДАЧА: МОДУЛЬНЫЙ СНЕГОВИК
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу, которая использует черепашью графику для изображения
снеговика. Помимо главной функции программа также должна иметь перечисленные
ниже функции:
    - drawBase - функция должна нарисовать основу снеговика, т.е. большой
    снежный ком внизу;
    - drawMidSection - функция должна нарисовать средний снежный ком;
    - drawArms - функция должна нарисовать руки снеговика;
    - drawHead - функция должна нарисовать голову снеговика, глаза,
    рот и другие черты лица по вашему усмотрению;
    - drawHat - эта функция должна нарисовать шляпу снеговика.
"""

import turtle as t

def drawBase():
    t.penup()
    t.goto(0, -160)
    t.pendown()
    t.circle(55)

def drawMidSection():
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.circle(35)

def drawArms():
    # left arm
    t.penup()
    t.goto(-35, -10)
    t.pendown()
    t.left(165)
    t.forward(30)
    t.right(55)
    t.forward(30)
    t.right(20)
    t.forward(7)
    t.backward(7)
    t.left(80)
    t.forward(7)
    # right arm
    t.penup()
    t.goto(35, -10)
    t.right(140)
    t.pendown()
    t.forward(35)
    t.right(35)
    t.forward(8)
    t.backward(8)
    t.left(80)
    t.forward(8)
    t.right(t.heading())

def drawHead():
    # head
    t.penup()
    t.goto(0, 20)
    t.pendown()
    t.circle(23)
    # eyes
    t.penup()
    t.goto(-7, 45)
    t.pendown()
    t.circle(3)
    t.penup()
    t.goto(7, 45)
    t.pendown()
    t.circle(3)
    # mouth
    t.penup()
    t.goto(-12, 37)
    t.pendown()
    t.goto(12, 37)

def drawHat():
    t.penup()
    t.goto(-35, 54)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    t.forward(70)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(15)
    t.left(90)
    t.forward(10)
    t.end_fill()

def main():
    t.speed(10)
    t.width(2)
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()
    t.hideturtle()
    t.exitonclick()

if __name__ == '__main__':
    main()