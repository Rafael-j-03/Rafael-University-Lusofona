import pygame, sys
from pygame.locals import *
import math
import numpy

#Display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((600,500))
ang = 0

while True: #Main loop
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    ang = ang + numpy.pi/10
    valRed = (math.cos(ang)+1)/2*255

    DISPLAYSURF.fill((valRed,0,0))

    pygame.display.update()

