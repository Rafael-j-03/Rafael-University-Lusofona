import pygame, sys
from pygame.locals import *
import math
import numpy

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
ang = 0
WHITE = (255,255,255)

while True: #Main loop--
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    ang= ang + numpy.pi/10 
    raio = 100
    x = 200 + math.sin(ang)*raio
    y = 150 + math.cos(ang)*raio

    pygame.draw.circle( DISPLAYSURF, WHITE, [x,y], 2)
    
    pygame.display.update()
