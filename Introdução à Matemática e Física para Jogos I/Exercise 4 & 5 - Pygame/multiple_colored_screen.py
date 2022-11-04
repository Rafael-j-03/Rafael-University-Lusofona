import pygame, sys
from pygame.locals import *
import math
import numpy

#Display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((600,500))
clock = pygame.time.Clock()

#Colors
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

colors = [RED, GREEN, BLUE]
current_index = 0

timer_interval = 1000 # 2.0 seconds
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, timer_interval)

#Display Color
DISPLAYSURF.fill(RED)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == timer_event:#
            current_index += 1
            if current_index >= len(colors):
                current_index = 0

    pygame.draw.line(DISPLAYSURF, colors[current_index], (0,500),(600,0),1000)
    pygame.display.flip()

while True: #Main loop
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()



    pygame.display.update()

