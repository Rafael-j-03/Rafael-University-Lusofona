import pygame, sys
from pygame.locals import *

#Display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((600,500))

#Colors
BLUE = (0,0,255)

#Display Color
DISPLAYSURF.fill(BLUE)

while True: #Main loop
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()



    pygame.display.update()

