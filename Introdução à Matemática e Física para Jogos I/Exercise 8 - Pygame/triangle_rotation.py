import pygame, sys
import numpy as np 
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1000,700)) #Colocar o tamanho da tela

pygame.display.set_caption("Aula 8") #Colocar titulo na janela

#Cores
WHITE = (255,255,255)
BLACK = (0,0,0)

#Posição das rots
p0 = [400, 350]
p1 = [350, 400]
p2 = [450, 400]

#Angulo
angulo = 10
theta = np.radians(angulo)

#Matriz de rotação
R = np.matrix([[np.cos(theta), np.sin(theta)], [-1*np.sin(theta), np.cos(theta)]])

while True:
    for event in pygame.event.get(): 

        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
            
    DISPLAYSURF.fill(BLACK)

    #Desenhar as rots
    pygame.draw.line(DISPLAYSURF, WHITE, p0, p1, 1)
    pygame.draw.line(DISPLAYSURF, WHITE, p1, p2, 1)
    pygame.draw.line(DISPLAYSURF, WHITE, p2, p0, 1)
    
    #Rotação
    p0_rot=np.matmul(R,p0)
    p0=[p0_rot[0,0], p0_rot[0,1]]

    p1_rot=np.matmul(R,p1)
    p1=[p1_rot[0,0], p1_rot[0,1]]

    p2_rot=np.matmul(R,p2) 
    p2=[p2_rot[0,0], p2_rot[0,1]]

    pygame.display.update()
    pygame.time.wait(50)