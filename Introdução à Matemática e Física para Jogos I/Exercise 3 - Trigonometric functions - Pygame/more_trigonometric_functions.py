import pygame, sys
from pygame.locals import *
import math
import numpy

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600,500)) #Display

#Cores
WHITE = (255,255,255)
RED = (255,0,0)
SALMON = (255,126,126)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
PURPLE = (126,126,255)

#Eixos
x1 = 0
y1 = 50
y2 = y1 + 50
y3 = y1 + 100
y4 = y1 + 150
y5 = y1 + 200
y6 = y1 + 250
y7 = y1 + 300

#Ângulos
a = 0
a2 = 0

#Amplitude
amplitude = 20
amplitude2 = 20

#Fase
fase = numpy.pi
fase2 = numpy.pi

#Frequencias
frequencia = 0.5
frequencia2 = 0.2
frequencia3 = 0.7


while True: #Main loop
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_ESCAPE:
             pygame.quit()
             sys.exit()
         if event.key == pygame.K_RIGHT:
             fase2 = fase2 + numpy.pi
         if event.key == pygame.K_LEFT:
             fase2 = fase2 - numpy.pi
    
    x1 = x1 + 1
    a = a + 1
    a2= a2 + 0.1

    pygame.draw.circle(DISPLAYSURF, WHITE, [x1,y1 + math.cos(a)],1) 
    
    #Amplitude
    pygame.draw.circle(DISPLAYSURF, RED, [x1, y2 + amplitude*math.cos(a2)],1)
    
    #Fase
    pygame.draw.circle(DISPLAYSURF, SALMON, [x1, y3 + amplitude*math.cos(a2 + fase)],1)
    pygame.draw.circle(DISPLAYSURF, PURPLE, [x1, y7 + amplitude*math.cos(a2 + fase2)],1)
    
    #Frequencia
    pygame.draw.circle(DISPLAYSURF, BLUE, [x1, y4 + amplitude*math.cos(a2*frequencia)],1)
    pygame.draw.circle(DISPLAYSURF, GREEN, [x1, y5 + amplitude*math.cos(a2*frequencia2)],1)
    pygame.draw.circle(DISPLAYSURF, YELLOW, [x1, y6 + amplitude*math.cos(a2*frequencia3)],1)

    pygame.display.update()