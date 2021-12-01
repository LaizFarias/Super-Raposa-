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


#inicialização dos itens do game
def inicializacao():
    # cria o grupo de cerebros 
    Group_cerebro = pygame.sprite.Group()
    c = 0
    while c < 2:
        moeda = sorteia_cerebro(WIDTH * c + 1000)
        Group_cerebro.add(moeda)
        c+= 1

    #cria o grupo de cogumelos 
    Group_cogumelo = pygame.sprite.Group()
    k = 0
    while k < 2:
        obstaculo = sorteia_cogumelo(WIDTH * k + 1000)
        Group_cogumelo.add(obstaculo)
        k += 1

    # cria o grupo das vidas
    Group_vida = pygame.sprite.Group()
    v = 0
    while v < 2:
        lifes = sorteia_vida(WIDTH * v + 1000)
        Group_vida.add(lifes)
        v += 1
    return Group_cerebro, Group_cogumelo, Group_vida

Group_cerebro, Group_cogumelo, Group_vida = inicializacao()

# condição para fazer o loop do game
estado = True 

# condição inicial para pausar o jogo 
pausa = False 

###vamo criar uma função para que a gente consiga desenhar na tela

def fim_de_tela(sprite):
    return sprite.rect[0] < -(sprite.rect[2])
def desenha():
    #preencher a tela de uma cor especifica
    raposa.Group_char.draw(janela)
    piso.Group_piso.draw(janela)
    Group_cogumelo.draw(janela)
    Group_cerebro.draw(janela)
    Group_vida.draw(janela)

#essa função vai atualizar a todo momento os freimer da tela com as nossas classes
def atualiza():
    piso.Group_piso.update()
    Group_cogumelo.update()
    Group_cerebro.update()
    Group_vida.update()
#arrumar a velocidade com que a raposa corre 
intercala = pygame.time.Clock()

#Estabelecendo as quantidades iniciais de vida
vida = 3
# Estabelecendo a variavel para contabilizar os pontos 
pontos = 0
# comparativo para aumentar a valocidade de deslocamento dos itens do game 
desloca0 = desloca

#Inicialização do Menu 
#=============================================================================
pygame.mixer.music.set_volume(0)
ativa_menu.play()
menu_princial(janela,menu_img1,menu_img2)
#=============================================================================

#Inicialização da partida utilizando a variavel estado 
while estado:

#================================================================================
# Escrevendo a contagem de pontos feitos pelo jogador no canto superior direito 
# a cada vez que ele colide com um cérebro 
    janela.blit(plano_de_fundo, (0,0))
    font = pygame.font.SysFont('Arial',30)
    text = font.render('Pontos', True, [255,255,255])
    janela.blit(text, [1100, 20])
    conta_ponto = font.render(f'{pontos}', True, [255,255,255])
    janela.blit(conta_ponto, [1125, 50])
       
# Escrevendo a contagem de vidas conquistadas pelo jogador no canto superior direito 
# a cada vez que ele colide com um coração
    font = pygame.font.SysFont('Arial',30)
    text = font.render('Vidas', True, [255,255,255])
    janela.blit(text, [1000, 20])
    desconto_ponto = font.render(f'{vida}', True, [255,255,255])
    janela.blit(desconto_ponto, [1025 , 50])

    janela.blit(text, [1000, 20])
    intercala.tick(10)
#=================================================================================

    for event in pygame.event.get():
        #se o evento for igual a fechar 
        if event.type == pygame.QUIT:
            #fecha janela
            pygame.quit()
            break
    #comando para pausar o jogo, aperte P para pausar e aperte P novamente para sair do modo pausa. 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pausa = not pausa


    if pausa == True: 
        #desliga a música principal enquanto o jogo estiver pausado
        pygame.mixer.music.set_volume(0)
        continue
    else:
        # Liga o som principal novamente quando o jogo sai da condição de pausa
        pygame.mixer.music.set_volume(1)

    #se tiver fora da tela esse objeto, posso tirar ele do meu grupo e remover esse objeto. 
    if fim_de_tela(piso.Group_piso.sprites()[0]):
        piso.Group_piso.remove(piso.Group_piso.sprites()[0])
        #cria um novo piso
        novo_piso = piso.Piso(WIDTH-40)
        piso.Group_piso.add(novo_piso)

    #sorteia o itens do jogo
    if len(Group_cerebro) <= 5:
        novo_cerebro = sorteia_cerebro(WIDTH * (1+random.random()))
        Group_cerebro.add(novo_cerebro)

    if len(Group_cogumelo) <= 5:
        novo_cogumelo = sorteia_cogumelo(WIDTH * (1+random.random()))
        Group_cogumelo.add(novo_cogumelo)

    if len(Group_vida) <= 5:
        novo_vida = sorteia_vida(WIDTH * (1+random.random()))
        Group_vida.add(novo_vida)
#=======================================================================================================
    #adiciona uma colisão do grupo player com o grupo do chão
    if pygame.sprite.groupcollide(raposa.Group_char, piso.Group_piso, False, False):
        velocidade_de_caida = 0
    else:
        velocidade_de_caida = 10 
    #adiciona uma colisão do grupo player com o grupo do cerebro
    if pygame.sprite.groupcollide(raposa.Group_char, Group_cerebro, False, True):
        #Colidiu com o cérebro e ganhou pontos 
        pontos += 1
        barulho_cerebro.play()
    # Se a divisão por 4 for igural a zera , aumenta a velocidade de deslocamento 
    # de todos os itens 
    if pontos % 4 == 0 and pontos != 0 and desloca < desloca0+(10*pontos/4):
        desloca += 0.2               
        piso.desloca = desloca
        cerebro.desloca = desloca
        cogumelos.desloca = desloca
        raposa.desloca = desloca
    #adiciona uma colisão do grupo player com o grupo de vida
    if pygame.sprite.groupcollide(raposa.Group_char, Group_vida, False, True):
        #colidiu com o coração e ganhou mais uma vida
        vida += 1      
        barulho_vida.play()   

    #adiciona uma colisão do grupo player com o grupo do cogumelo
    if pygame.sprite.groupcollide(raposa.Group_char, Group_cogumelo, False, True):
        #colidiu com o cogumelo e perdeu vida 
        vida -= 1
        barulho_cogumelo.play()

    #condição para entrar na tela de game over
    if vida == 0:
        pygame.mixer.music.set_volume(0)
        game_over.play()
        tela_game_over(janela, over1,over2)
        Group_cerebro, Group_cogumelo, Group_vida = inicializacao()
        vida = 3
        # break #return estado depois
    raposa.Group_char.update()
    atualiza()
    # chamar a minha função toda vez que eu for executar ela na minha janela.
    desenha()
    pygame.display.update()