import pygame
from config import *

#Os cogumelos arrancaram a vida do player a cada vez que o player colidir com ele.
class Cogumelo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('graficos/boss.gif').convert_alpha()
        self.image = pygame.transform.scale(self.image, [80, 80])
        self.rect = pygame.Rect(100, 100, 100, 100)
        self.rect[0] = x
        self.mask = pygame.mask.from_surface(self.image)
        self.rect[1] = HEIGHT - y

    def update(self, *args):
        self.rect[0] -= desloca
        if self.rect[0] < - 30:
            self.kill()