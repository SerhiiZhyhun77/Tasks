# Намалюйте 100 кіл випадкових кольорів випадкових розмірів у випадкових місцях і примусьте їх рухатись згори до низу
# зліва направо. Коли коло досягатиме краю екрану, нехай воно з'явиться вгорі і продовжить падіння.

import random
import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

colors = list([0] * 100)
locations = list([0] * 100)
sizes = list([0] * 100)
keep_going = True
BLACK = (0, 0, 0)
timer = pygame.time.Clock()

for n in range(100):
    colors[n] = (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255))
    locations[n] = (random.randint(0, 800),
                    random.randint(0, 600))
    sizes[n] = random.randint(10, 40)

while keep_going:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    for n in range(100):
        pygame.draw.circle(screen, colors[n], locations[n], sizes[n])
        new_x = locations[n][0] + 1
        new_y = locations[n][1] + 1
        if new_x > 850:
            new_x -= 900
        if new_y > 650:
            new_y -= 700
        locations[n] = (new_x, new_y)

    pygame.display.update()
    timer.tick(60)

pygame.quit()
