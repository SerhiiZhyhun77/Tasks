import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
t.pencolor('white')
t.turtlesize(2, 2, 20)

def up():
    t.forward(50)

def left():
    t.left(90)

def right():
    t.right(90)


turtle.onkeypress(up, 'Up')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.onscreenclick(t.setpos)
turtle.listen()

turtle.mainloop()