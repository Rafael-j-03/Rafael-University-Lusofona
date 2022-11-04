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
    screen.fill(WHITE)
    
    speed=4
    v_normalized = v_direcao/np.linalg.norm(v_direcao)
    v_velocity = np.multiply(speed, v_normalized)
    v_pos=np.add(v_pos,v_velocity)

    pygame.draw.circle(screen,BLACK, v_pos, 4)

    pygame.display.update()
    fpsClock.tick(FPS)