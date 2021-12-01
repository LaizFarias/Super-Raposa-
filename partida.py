import pygame 
import raposa
from sorteia_itens import *  
import piso 
import cerebro
import cogumelos
from vida import *
from pygame import image
from pygame import key
from pygame.constants import K_LEFT, K_RIGHT 
from config import *
from tela_game_over import *
from menu import *

pygame.init()

#adicionando as musicas ao jogo
#===================================================================
musica_de_fundo = pygame.mixer.music.load('musica/musica_2.ogg')
#condição para o som tocar mais de uma vez 
pygame.mixer.music.play(-1)
barulho_cerebro = pygame.mixer.Sound('musica/pegou_cerebro.wav')
barulho_cogumelo = pygame.mixer.Sound('musica/pegou_cogumelo.wav')
barulho_vida = pygame.mixer.Sound('musica/pegou_vida.wav')
game_over = pygame.mixer.Sound('musica/game_over.ogg')
ativa_menu = pygame.mixer.Sound('musica/menu.wav')
#===================================================================

#criando a janela
janela = pygame.display.set_mode([1200, 600])


#dando nome a janela. 
pygame.display.set_caption('Super Raposa')

# Adicionando os gráficos ao jogo 
#========================================================================
plano_de_fundo = pygame.image.load('graficos/fundo.png').convert_alpha()
plano_de_fundo = pygame.transform.scale(plano_de_fundo, [1200,600])
over1 = pygame.image.load('graficos/over_1.png').convert_alpha()
over1 = pygame.transform.scale(over1, [1200,600])
over2 = pygame.image.load('graficos/over_2.png').convert_alpha()
over2 = pygame.transform.scale(over2, [1200,600])
menu_img1 = pygame.image.load('graficos/menu_tela1.png').convert_alpha()
menu_img1 = pygame.transform.scale(menu_img1, [1200,600])
menu_img2 = pygame.image.load('graficos/menu_tela2.png').convert_alpha()
menu_img2 = pygame.transform.scale(menu_img2, [1200,600])

#========================================================================