import pygame 
from pygame import image
from pygame import key
from pygame.constants import K_LEFT, K_RIGHT 
from piso import *
from config import *

# Criando a classe da raposa 
class Char(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #definir uma imagem pro meu player. 
        lista_raposa = [pygame.image.load('graficos/andar1.png'),pygame.image.load('graficos/andar2.png')]
        self.image_corre = lista_raposa
        self.image_cair = pygame.image.load('graficos/cair.png')
        self.image = pygame.image.load('graficos/andar1.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(100,100,100,100)

#na classe sempre vai ter o metodo update que serve para atualizar o nosso player 
#pra poder chamar la na janela e ele entender 
        self.atual_imagem = 0
    def update(self, *args):
        ### cria uma função pra mover o player 
        def movimento(self):
            #vamo fazer o player se  movimentar na tela 
            key = pygame.key.get_pressed()
            #pra frente
            if key[pygame.K_RIGHT]:
                self.rect[0] += desloca
                if self.rect.right > WIDTH:
                    self.rect.right  = WIDTH
            #pra trás
            if key[pygame.K_LEFT]:
                self.rect[0] -= desloca
                if self.rect[0] < 0:
                    self.rect[0] = 0

            #imagem atual por que ele vai ter que percorrer a lista inteira 
            self.atual_imagem = (self.atual_imagem + 1) % 2 #resto da divisão pelo numero de imagens 
            self.image = self.image_corre[self.atual_imagem]
            self.image = pygame.transform.scale(self.image,[100, 100])
        movimento(self)
         #adicionar uma gravidade pro player 
        if pygame.sprite.groupcollide(Group_char, Group_piso, False, False):
            velocidade_de_caida = 0
        else:
            velocidade_de_caida = 10  
        self.rect[1] += velocidade_de_caida
        def voar(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.rect[1] -= 30 
                self.image = pygame.image.load('graficos/voar1.png').convert_alpha()
                self.image = pygame.transform.scale(self.image, [100,100])

        voar(self)
        #fazer a função pra cair
        def cair(self):
            key = pygame.key.get_pressed()
            if not pygame.sprite.groupcollide(Group_char,Group_piso, False, False) and not key[pygame.K_SPACE]:
                self.image = self.image_cair
                self.image = pygame.transform.scale(self.image, [120,120])
        cair(self)
##### toda vez que eu crio uma classe, eu tenho que criar um grupo pra essa classe
Group_char = pygame.sprite.Group()
#vou pegar o player, que vai receber a classe Char
player = Char()
Group_char.add(player)