from dplayer import *
from dthing import *

# setting initial values
yellow = (255, 255, 0)
x_max, y_max = 800, 400
start = 0


def get_time(reset):
    global start
    if reset:
        start = pg.time.get_ticks()
    diff = pg.time.get_ticks() - start
    return diff


# running Pygame, creating the game board and character
pg.init()
pg.key.set_repeat(20, 20)
pg.display.set_caption('Dodger')
window = pg.display.set_mode((x_max, y_max))
figure = Player(20, 30)
ball = Thing('images/ball1.png')
ball.set_position(x_max - 50, y_max / 2, True)

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
                get_time(True)
            if event.key == pg.K_DOWN:
                figure.set_state(1)
                get_time(True)
            if event.key == pg.K_RETURN:
                figure.set_state(0)

    # testing
    time = get_time(False)
    if time > 200:
        figure.set_state(0)

    # move the ball, reset if necessary
    if not figure.is_hit:
        ball.move(-1, 0)
        ball.control_restart(x_max - 50, y_max / 2)
        # checking if the ball is in the playing area
        if ball.x < figure.x + 150:
            # if the player loses, the game ends
            if not figure.dodge(ball.y, y_max / 2):
                figure.is_hit = True

    # position the sprite in the window
    window.fill(yellow)
    window.blit(figure.bild, (figure.x, figure.y))
    window.blit(ball.bild, (ball.x, ball.y))
    pg.display.update()

pg.quit()
