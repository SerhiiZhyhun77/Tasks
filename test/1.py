import turtle
colors = ['red', 'yellow', 'blue', 'green']
turtle.bgcolor('black')
t = turtle.Pen()
t.speed(0)
for x in range(500):
    t.pencolor(colors[x % 4])
    t.circle(x)
    t.left(91)
