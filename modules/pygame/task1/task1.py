import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pg.image.load("insect1.png")
        self.x, self.y = x_pos, y_pos


# setting initial values
green = (0, 255, 0)

# launching Pygame, creating a game field and character
pg.init()
pg.key.set_repeat(20, 20)
window = pg.display.set_mode((600, 400))
figure = Player(250, 150)

# event loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # setting the keys
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                figure.x -= 5
            if event.key == pg.K_RIGHT:
                figure.x += 5
            if event.key == pg.K_UP:
                figure.y -= 5
            if event.key == pg.K_DOWN:
                figure.y += 5
    # update sprite position
    window.fill(green)
    window.blit(figure.image, (figure.x, figure.y))
    pg.display.update()

pg.quit()
