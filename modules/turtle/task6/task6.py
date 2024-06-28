# SpiralMyName.py - печатает цветную спираль из имени
# пользователя

import turtle  # Установка графики Turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]

# Запрос имени пользователя с помощью всплывающего окна
# textinput
your_name = turtle.textinput("Введите свое имя", "Как тебя зовут?")

# Нарисовать на экране спираль из имени, повторенного 100 раз
for x in range(100):
    t.pencolor(colors[x % 4])  # По очереди выбрать все 4 цвета
    t.penup()  # Не рисовать обычные линии спирали
    t.forward(x * 4)  # Просто переместить черепашку по экрану
    t.pendown()  # Написать имя пользователя, увеличивая каждый раз шрифт
    t.write(your_name, font=("Arial", int((x + 4) / 4), "bold"))
    t.left(92)  # Повернуть налево, как в других спиралях

turtle.exitonclick()
