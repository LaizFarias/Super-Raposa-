import random
from cogumelos import *
from cerebro import *

#sorteia os cogumelos que aparecem na tela
def sorteia_cogumelo(x):
    tamanho = random.randint(1, 1000)
    box = Cogumelo(x, tamanho)
    return box
#sorteia os cerebros que aparecem na tela
def sorteia_cerebro(x):
    tamanho = random.randint(60, 500)
    moeda = Cerebro(x, tamanho)
    return moeda

#verifica se o item está no fim da tela 
def fim_de_tela(sprite):
    return sprite.rect[0] < -(sprite.rect[2])