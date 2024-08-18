# Намалюйте 100 кіл випадкових кольорів випадкових розмірів у випадкових місцях

import random
import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

colors = list([0] * 100)
locations = list([0] * 100)
sizes = list([0] * 100)
keep_going = True

for n in range(100):
    colors[n] = (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255))
    locations[n] = (random.randint(0, 800),
                    random.randint(0, 600))
    sizes[n] = random.randint(10, 100)

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    for n in range(100):
        pygame.draw.circle(screen, colors[n], locations[n], sizes[n])

    pygame.display.update()

pygame.quit()
