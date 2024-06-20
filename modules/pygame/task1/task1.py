import pygame as pg
from math import *
import random


class Player(pg.sprite.Sprite):
    def __init__(self, x_pos=0, y_pos=0):
        super().__init__()
        self.image = pg.image.load("insect1.png")
        self.x, self.y = x_pos, y_pos
        self.bild = self.image

    def rotate(self, degree):
        self.bild = pg.transform.rotate(self.image, degree)

    def move(self, distance, xx, yy):
        self.x += xx
        self.y += yy
        distance -= 1
        return distance

    def step(self, xx, yy):
        self.x += xx
        self.y += yy



# setting initial values
green = (0, 255, 0)
x_max, y_max = 600, 400
direction = 0
distance = 0
degree = 0

# launching Pygame, creating a game field and character
pg.init()
pg.key.set_repeat(20, 20)
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
            # x_dif = x_pos - figure.x - 50
            # y_dif = y_pos - figure.y - 50
            # distance = sqrt(x_dif * x_dif + y_dif * y_dif)
            # degree = atan2(-y_dif, x_dif)
            # degree = degrees(degree) - 90
            # x_dif /= distance
            # y_dif /= distance
            # figure.rotate(degree)

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
    figure.step(x_step, y_step)
    pg.time.delay(10)

        # setting the keys
        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_LEFT:
        #         direction = 1
        #         if figure.x > 0:
        #             figure.x -= 5
        #     if event.key == pg.K_RIGHT:
        #         direction = 3
        #         if figure.x < x_max - 100:
        #             figure.x += 5
        #     if event.key == pg.K_UP:
        #         direction = 0
        #         if figure.y > 0:
        #             figure.y -= 5
        #     if event.key == pg.K_DOWN:
        #         direction = 2
        #         if figure.y < y_max - 100:
        #             figure.y += 5
        #     figure.rotate(direction * 90)

    # motion delay
    # if distance > 5:
    #     distance = figure.move(distance, x_dif, y_dif)
    #     pg.time.delay(10)
    # update sprite position
    window.fill(green)
    window.blit(figure.bild, (figure.x, figure.y))
    pg.display.update()

pg.quit()
