import pygame
pygame.init()
screen = pygame.display.set_mode([800, 600])
keep_going = True
pic = pygame.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0, 0)) # Ця і...
pic.set_colorkey(colorkey) # ця команди необов'язкові. Якщо зображення виглядає так, наче у нього  є чорні кути, то вони виправлять це і кути будуть прозорими
picx = 0
picy = 0
BLACK = (0, 0, 0)
timer = pygame.time.Clock() # Таймер для анімації
speedx = 5
speedy = 5

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    picx += speedx
    picy += speedy

    if picx <= 0 or picx + pic.get_width() >= 800:
        speedx = -speedx
    if picy <= 0 or picy + pic.get_height() >= 600:
        speedy = -speedy

    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))
    pygame.display.update()
    timer.tick(60) # Обмежити до 60 кадрів в секунду

pygame.quit()
