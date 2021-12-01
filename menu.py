import pygame
from config import *
#menu e informativo inicial 

def menu_princial(janela,primeira,segunda): 
    primeira_imagem = True
    menu = True
    while menu != False:
        pygame.display.update()
        pygame.time.wait(600)
        #condição necessária para intercala duas imagens 
        if menu == True:
                
            if primeira_imagem == True:
                primeira_imagem = False
                janela.blit(segunda, (0,0))
            else:
                primeira_imagem = True
                janela.blit(primeira, (0,0))

        for event in pygame.event.get():
            #se o evento for igual a fechar 
            if event.type == pygame.QUIT:
                #fecha janela
                pygame.quit()
                break
        #Condição de Aperte qualquer tecla pra iniciar o game
            elif event.type == pygame.KEYDOWN:
                    menu = not menu