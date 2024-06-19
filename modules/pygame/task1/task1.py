import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("insect1.png")

green = (0, 255, 0)

pg.init()
window = pg.display.set_mode((600, 400))
window.fill(green)

figure = Player()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    window.blit(figure.image, (250, 250))
    pg.display.update()

pg.quit()