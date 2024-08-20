import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Smiley Explosion')
clock = pygame.time.Clock()
pic = pygame.image.load('CrazySmile.bmp')
colorkey = pic.get_at((0, 0))
pic.set_colorkey(colorkey)
sprite_list = pygame.sprite.Group()

BLACK = (0, 0, 0)
mousedown = False
keep_going = True

class Smiley(pygame.sprite.Sprite):
    pos = (0, 0)
    xvel = 1
    yvel = 1
    scale = 100

    def __init__(self, pos, xvel, yvel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pic
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = pos[0] - self.scale / 2
        self.rect.y = pos[1] - self.scale / 2
        self.xvel = xvel
        self.yvel = yvel




