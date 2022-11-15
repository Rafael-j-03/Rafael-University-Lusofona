import pygame, sys
import numpy as np 
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,500)) #Colocar o tamanho da tela

font = pygame.font.SysFont('Arial', 15) #Selecionar a fonte

cnt_x = screen.get_width()/2 #Centro do X
cnt_y = screen.get_height()/2 #Centro do Y
max_x = screen.get_width() #X máximo
max_y = screen.get_height() #Y máximo

pos_circle =[cnt_x, cnt_y] #Regular a posição do circulo

#Colors
BLUE = (0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

while True:
    for event in pygame.event.get(): 

        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
    
    #Cor da tela
    screen.fill(WHITE)
    
    #Linhas centradas horizontalmente e verticalmente
    pygame.draw.line(screen, RED,(0,cnt_y), (max_x,cnt_y),1)
    pygame.draw.line(screen, RED,(cnt_x,0), (cnt_x,max_y),1)

    #Desenhar o circulo e a sua posição
    pygame.draw.circle(screen, BLUE, pos_circle, 10)
    pos_circle = np.round(pos_circle,2) #Arredondar às casas decimais
    screen.blit(font.render(str(pos_circle), True, BLACK), pos_circle) 
    
    #Calcular o ângulo
    angulo = np.arctan2(cnt_y - pos_circle[1], cnt_x - pos_circle[0])
    angulo_graus = np.degrees(angulo) #Colocar o angulo em graus
    angulo_graus = np.round(angulo_graus) #Arrendondar o resultado às unidades
    screen.blit(font.render( str(angulo_graus)+ " graus ", True, BLACK), (pos_circle[0],pos_circle[1]+20)) #Colocar a font do número de graus
    
    #Linha a apontar para o circulo
    pygame.draw.line(screen, GREEN,(cnt_x,cnt_y), pos_circle,1)
    
    #Keys de movimento
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pos_circle[0]-=0.1
    if keys[pygame.K_RIGHT]:
        pos_circle[0]+=0.1
    if keys[pygame.K_UP]:
        pos_circle[1]-=0.1
    if keys[pygame.K_DOWN]:
        pos_circle[1]+=0.1
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    #Update constante na tela
    pygame.display.flip()