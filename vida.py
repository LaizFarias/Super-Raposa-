import pygame 
import random 
from config import *


def sorteia_vida(x):
    tamanho = random.randint(1, 3000)
    life = Vida(x, tamanho)
    return life

class Vida(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('graficos/vida.png')
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(100, 100, 50, 50)
        self.rect[0] = x
        self.mask = pygame.mask.from_surface(self.image)
        self.rect[1] = HEIGHT - y

    def update(self, *args):
        self.rect[0] -= desloca
        if self.rect[0] < - 20:
            self.kill()

vidaGroup = pygame.sprite.Group()
for i in range(2):
    lifes = sorteia_vida(WIDTH * i + 1000)
    vidaGroup.add(lifes)