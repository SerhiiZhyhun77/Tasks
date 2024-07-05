import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor('black')
sides = int(turtle.numinput('Количество сторон', 'Сколько сторон у вашей спирали спиралей? (2-6)', 4, 2, 6))
colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple','white',
          'brown', 'gray', 'pink']
for m in range(100):
    t.forward(m * 4)
    position = t.position()
    heading = t.heading()
    print(position, heading)

    for n in range(int(m / 2)):
        t.pendown()
        t.pencolor(colors[n % sides])
        t.forward(2 * n)
        t.right(360 / sides - 2)
        t.penup()
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360 / sides + 2)