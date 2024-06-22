import pygame as pg
import random
from dplayer import *

# setting initial values
yellow = (255, 255, 0)
x_max, y_max = 800, 400

# running Pygame, creating the game board and character
pg.init()
pg.key.set_repeat(20, 20)
pg.display.set_caption('Dodger')
window = pg.display.set_mode((x_max, y_max))
figure = Player(20, 30)

# event loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # setting the keys
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                figure.set_state(2)
            elif event.key == pg.K_DOWN:
                figure.set_state(1)
            elif event.key == pg.K_RETURN:
                figure.set_state(0)
    # position the sprite in the window
    window.fill(yellow)
    window.blit(figure.bild, (figure.x, figure.y))
    pg.display.update()


pg.quit()
