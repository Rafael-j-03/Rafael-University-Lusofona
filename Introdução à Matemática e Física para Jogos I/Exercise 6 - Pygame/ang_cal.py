import pygame, sys
import numpy as np 
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((600, 500)) 

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)

#Posições Iniciais
#Azul pos
v_pos_blue = [60,50]
v_direcao_blue = [0.2,0]

#Vermelho pos
v_pos_red = [60,60]
v_direcao_red = [0,0.2]

while True:
    for event in pygame.event.get(): 

        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
    
    #Cor da tela
    DISPLAYSURF.fill(WHITE)
    
    #Movimento bola Azul
    speed=0.1
    v_normalized = v_direcao_blue/np.linalg.norm(v_direcao_blue)
    v_velocity= np.multiply(speed, v_normalized)
    v_pos_blue=np.add(v_pos_blue,v_velocity)     
    pygame.draw.circle( DISPLAYSURF, BLUE, v_pos_blue, 5)


    #Movimento bola Vermelha
    speed=0.1
    v_normalized2 = v_direcao_red/np.linalg.norm(v_direcao_red)
    v_velocity= np.multiply(speed, v_normalized2)
    v_pos_red=np.add(v_pos_red,v_velocity)     
    pygame.draw.circle( DISPLAYSURF, RED, v_pos_red, 5)


    #Soma dos ang
    produto_interno=np.dot(v_direcao_blue, v_direcao_red)
    magnitude_blue=np.linalg.norm(v_direcao_blue)
    magnitude_red=np.linalg.norm(v_direcao_red)
    produto_magnitudes=np.multiply(magnitude_blue,magnitude_red)
    angulo = np.arccos(np.divide(produto_interno,produto_magnitudes))
    #Soma imprimida dos angulos
    print(np.degrees(angulo))


    #Saber a relação entre duas direções

    #Se o produto interno for igual a 1 = Ambos têm a mesma direção
    if(np.dot(v_normalized2, v_normalized)==1):
        print("Same Direction")

    #Se o produto interno for igual a 0 = são perpendiculares
    elif(np.dot(v_normalized2, v_normalized)==0): 
        print("Perpendicular")

    #Se o produto interno for -1 = estão a ir em direções opostas
    elif(np.dot(v_normalized2, v_normalized)==-1): 
        print("Opposite directions")

    #Se não for nenhum dos casos então:
    else :
        print("Non orthogonal")



    #Update constante na tela
    pygame.display.update()