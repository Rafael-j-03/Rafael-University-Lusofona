from curses import window
import pygame
import sys
from pygame.locals import *
pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500,400))
pygame.display.set_caption("Drawing")
WHITE = (255,255,255)
RED = (255,0,0)

# draw on the surface object
DISPLAYSURF.fill(WHITE)
pygame.draw.line(DISPLAYSURF,RED,(60,60),(120,60),4)
print("FFFF")
# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
         pygame.quit()
         sys.exit()
    pygame.display.update()
     

