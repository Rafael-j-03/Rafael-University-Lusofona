import pygame, sys
from pygame.locals import *
import math
import numpy as np

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))

#Color
WHITE=(255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)

#Variables
ang=np.pi
posicao=0
inicio_linha=(200,150)
raio=100


while True: #Main loop--
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
               
    DISPLAYSURF.fill(BLACK)

    ang = ang - np.pi / 500

    #Coordenadas fim linha
    x = math.sin(ang)*raio
    y = math.cos(ang)*raio
    fim_linha=np.add(inicio_linha, [x,y])

    pygame.draw.circle( DISPLAYSURF, WHITE, [200,150], 100,3)
    pygame.draw.line(DISPLAYSURF, RED, inicio_linha, fim_linha, 2)

    pygame.display.update()


