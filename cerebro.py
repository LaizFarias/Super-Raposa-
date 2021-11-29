import pygame
from config import *

# O cerebro dará pontos para o player, permitindo que o jogo acelere
# quando o resto da divisão por 4 dos pontos for igual a zero.
class Cerebro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('graficos/cerebro.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [40, 40])
        self.rect = pygame.Rect(100, 100, 20, 20)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect[0] = x
        self.rect[1] = HEIGHT - y

    def update(self, *args):
        self.rect[0] -= desloca
        if self.rect[0] < - 50:
            self.kill()