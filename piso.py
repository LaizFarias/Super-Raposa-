import pygame
from config import *

class Piso(pygame.sprite.Sprite):
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        #definir uma imagem pro meu chão. 
        self.image = pygame.image.load('graficos/piso.png')
#transforma a escala dele pra escala que voce quer
        self.image = pygame.transform.scale(self.image, [G_W,G_H])
        #pega o que o chão ja tem 
        self.rect = self.image.get_rect()
        self.rect[0] = x
        #primeiro parametro é y do chão 
        self.rect[1] = HEIGHT - G_H
    def update(self, *args):
        # o chão anda 
        self.rect[0] -= desloca
        if self.rect[0] <= - WIDTH:
            self.rect[0] = WIDTH

#cria o grupo do chão/piso
Group_piso = pygame.sprite.Group()
p = 0
while p < 2:
    chao = Piso(WIDTH * p)
    Group_piso.add(chao)
    p += 1