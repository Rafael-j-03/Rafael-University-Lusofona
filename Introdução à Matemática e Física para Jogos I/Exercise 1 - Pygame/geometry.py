import pygame
import sys
from pygame.locals import *
pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Drawing")
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

# draw on the surface object
DISPLAYSURF.fill(WHITE)

# draw red line forming an rectangle
pygame.draw.line(DISPLAYSURF,RED,(10,10),(1014,10),4)
pygame.draw.line(DISPLAYSURF,RED,(10,10),(10,758),4)
pygame.draw.line(DISPLAYSURF,RED,(10,758),(1014,758),4)
pygame.draw.line(DISPLAYSURF,RED,(1014,758),(1014,10),4)

# draw a X inside the rectangle
pygame.draw.line(DISPLAYSURF,BLUE,(10,10),(1014,758),5)
pygame.draw.line(DISPLAYSURF,BLUE,(1014,10),(10,758),5)

# draw a circle inside the rectangle
pygame.draw.circle(DISPLAYSURF,YELLOW,(512,384),50,3)

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
         pygame.quit()
         sys.exit()
    pygame.display.update()