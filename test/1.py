import turtle
t = turtle.Pen()
t.speed(0)
sides = int(turtle.numinput("Количество сторон", "Сколько сторон будет у вашей спирали?", 4))
for m in range(5, 75):
    t.left(360 / sides + 5)
    t.width(m // 25 + 1)
    t.penup()
    t.forward(m * 4)
    t.pendown()

    if (m % 2 == 0):
        for m in range(sides):
            t.circle(m / 3 + 3)
            t.right(360 / sides)
    else:
        for m in range(sides):
            t.forward(m + 3)
            t.right(360 / sides)
turtle.exitonclick()