import pygame, sys
import numpy as np
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400,300))

fpsClock = pygame.time.Clock()
FPS = 15 #num de segundos
WHITE = (255,255,255)
BLACK = (0,0,0)

v_pos=[0,100]
v_direcao=[1,0]


# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
         pygame.quit()
         sys.exit()
        if event.type == pygame.KEYDOWN:
         print(event.key)
         #print(chr(event.key))
         if event.key == pygame.K_ESCAPE:
             pygame.quit()
             sys.exit()
         if event.key == pygame.K_RIGHT:
             v_direcao=[1,0]
         if event.key == pygame.K_LEFT:
             v_direcao=[-1,0]
         if event.key == pygame.K_UP:
             v_direcao=[0,-1]
         if event.key == pygame.K_DOWN:
             v_direcao=[0,1]
    screen.fill(WHITE)
    v_pos=np.add(v_pos,v_direcao)
    pygame.draw.circle(screen,BLACK, v_pos, 4)

    pygame.display.update()
    fpsClock.tick(FPS)