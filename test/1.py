from turtle import *
import random

width, height = 600, 400
window = Screen()
window.title("Черепашка")
window.setup(width=width, height=height)

shape("turtle")
for step in range(20):
    forward(random.randint(5, 30))
    left(random.randint(-90, 90))

print("OK")
