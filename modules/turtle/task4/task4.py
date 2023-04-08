# -*- coding: utf-8 -*-

"""ЗАДАЧА: ШАХМАТНАЯ ДОСКА
[Начинаем программировать на Python. Тони Гэддис (2022)]

Напишите программу с использованием черепашьей графики, в которой применяется
функция square вместе с циклом (или циклами) для создания узора шахматной доски.
"""

import turtle as t

def square(x, y, width, fill=False):
    t.penup()
    t.goto(x, y)
    t.pendown()
    if fill:
        t.begin_fill()
    for i in range(4):
        t.forward(width)
        t.right(90)
    if fill:
        t.end_fill()
    t.penup

def is_odd(number):
    return False if number % 2 else True

def main():
    BOARD_WIDTH = 400
    NUMBER_OF_CELLS = 8
    CELL_WIDTH = int(BOARD_WIDTH / NUMBER_OF_CELLS)
    t.speed(10)

    for i in range(NUMBER_OF_CELLS):
        for j in range(NUMBER_OF_CELLS):
            x = -BOARD_WIDTH / 2 + i * CELL_WIDTH
            y = -(BOARD_WIDTH - 2 * CELL_WIDTH) / 2 + j * CELL_WIDTH
            # if both odd or both even - fill
            if (is_odd(i) and is_odd(j)) or \
                    (not is_odd(i) and not is_odd(j)):
                fill = True
            else:
                fill = False
            square(x, y, CELL_WIDTH, fill)

    t.hideturtle()
    t.exitonclick()

if __name__ == '__main__':
    main()