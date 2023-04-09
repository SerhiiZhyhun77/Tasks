# -*- coding: utf-8 -*-

"""ЗАДАЧА: ГОРОДСКОЙ СИЛУЭТ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу с черепашьей графикой, которая рисует городской силуэт.
Конечная задача программы состоит в том, чтобы нарисовать контуры нескольких
городских зданий на фоне ночного неба. Подразделите программу на модули,
написав функции, которые выполняют приведенные ниже задачи:
    - рисование контуров зданий;
    - рисование нескольких окон в зданиях;
    - использование случайно разбросанных звезд в виде точек (убедитесь,
    что звезды появляются на небе, а не на зданиях).
"""

import turtle as t
import random

def get_pixel_color(x, y):
    # canvas use different coordinates than turtle
    y = -y
    # get access to tkinter.Canvas
    canvas = t.getcanvas()
    # find IDs of all objects in rectangle (x, y, x, y)
    ids = canvas.find_overlapping(x, y, x, y)
    # if found objects
    if ids:
        # get ID of last object (top most)
        index = ids[-1]
        # get its color
        color = canvas.itemcget(index, "fill")
        # if it has color then return it
        if color:
            return color
    # if there was no object then return "white" - background color in turtle
    return "white"  # default color

def draw_buildings(width, height):
    # draw one building
    def draw_building(width_b, height_b):
        t.pendown()
        t.fillcolor('grey')
        t.color('grey')
        t.begin_fill()
        for i in range(2):
            t.forward(width_b)
            t.left(90)
            t.forward(height_b)
            t.left(90)
        t.end_fill()
        t.penup()

    # start coordinates
    x_s = -width / 2 - 10
    y_s = -height / 2 - 6
    t.penup()
    t.goto(x_s, y_s)
    t.pendown()
    # draw buildings of different widths and heights
    while x_s < width / 2:
        width_b = random.randint(20, 50)
        height_b = random.randint(10, height)
        draw_building(width_b, height_b)
        x_s += width_b
        t.goto(x_s, y_s)

def draw_windows(width, height):
    # draw one window
    def draw_window(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor('white')
        t.color('white')
        t.begin_fill()
        for i in range(4):
            t.forward(5)
            t.right(90)
        t.end_fill()
        t.penup()

    # checking the color to make sure the window is on the building
    def fit_window(x, y):
        if get_pixel_color(x_s - 4, y_s + 4) == 'grey' and \
                get_pixel_color(x_s + 9, y_s - 9) == 'grey' and \
                get_pixel_color(x_s + 9, y_s + 4) == 'grey' and \
                get_pixel_color(x_s - 4, y_s - 9) == 'grey':
            return True
        else:
            return False

    x_s = -width / 2
    while x_s < width / 2:
        # drawing several windows at different heights
        y_lst = random.sample(
            range(int(-height / 2) + 10, int(height / 2), 15), 3)
        for y_s in y_lst:
            if fit_window(x_s, y_s):
                draw_window(x_s, y_s)
        x_s += random.randint(10, 30)

def draw_stars(width, height):
    # draw one star
    def draw_star(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(2, 'yellow')
        t.penup()

    # checking that the star does not hit the building
    def fit_star(x, y):
        if get_pixel_color(x - 2, y - 2) != 'grey' and \
                get_pixel_color(x + 2, y + 2) != 'grey':
            return True
        else:
            return False

    # list of stars at random coordinates
    star_lst = [
        (random.randint(-width / 2, width / 2),
         random.randint(-height / 2, height / 2))
        for i in range(random.randint(10, 30))
    ]
    # draw a star if it doesn't hit the building
    for x, y in star_lst:
        if fit_star(x, y):
            draw_star(x, y)

def main():
    WIDTH = 200
    HEIGHT = 200
    t.speed(0)
    t.setup(WIDTH + 20, HEIGHT + 20)
    t.screensize(WIDTH, HEIGHT, 'black')
    draw_buildings(WIDTH, HEIGHT)
    draw_windows(WIDTH, HEIGHT)
    draw_stars(WIDTH, HEIGHT)
    t.hideturtle()
    t.exitonclick()

if __name__ == '__main__':
    main()
