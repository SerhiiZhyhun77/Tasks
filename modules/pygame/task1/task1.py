import pygame as pg
from math import *
import random
from bplayer import *

# setting initial values
green = (0, 255, 0)
x_max, y_max = 600, 400
direction = 0
distance = 0
degree = 0

# launching Pygame, creating a game field and character
pg.init()
pg.key.set_repeat(20, 20)
pg.display.set_caption("Bug Game")
window = pg.display.set_mode((x_max, y_max))
figure = Player(x_max / 2 - 50, y_max / 2 - 50)

# random direction
x_step, y_step = random.randint(0, 2), random.randint(0, 2)
if x_step == 0:
    x_step = -1
if y_step == 0:
    y_step = -1

# event loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # setting the mouse
        if event.type == pg.MOUSEBUTTONDOWN:
            (x_pos, y_pos) = pg.mouse.get_pos()
            if x_pos > figure.x and x_pos < figure.x + 100 \
                and y_pos > figure.y and y_pos < figure.y + 100:
                figure.destroy()

    # restriction of movement
    if figure.x < 0 or figure.x > x_max - 110:
        x_step = -x_step
    if figure.y < 0 or figure.y > y_max - 110:
        y_step = -y_step

    # determining the direction of movement
    degree = atan2(-y_step, x_step)
    degree = degrees(degree) - 90
    figure.rotate(degree)

    # motion delay
    if not figure.is_killed:
        figure.step(x_step, y_step)
        pg.time.delay(5)

    # sprite position in window (new)
    window.fill(green)
    window.blit(figure.bild, (figure.x, figure.y))
    pg.display.update()

pg.quit()
