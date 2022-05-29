# 1 - Import library
import math
import pygame, math
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False, False, False]
playerpos=[100,100]

# 3 - Load images
player = pygame.image.load("resources/images/natchobacho.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
angle = 0

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    for x in range(round(width/grass.get_width())+1):
        for y in range(round(height/grass.get_height())+1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))

    # 6.1 - Set player position and rotation
    # position = pygame.mouse.get_pos()
    # angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    # playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerrot = pygame.transform.rotate(player, angle)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1) 

    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_LEFT:
                keys[1]=True
            elif event.key==K_DOWN:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True
            elif event.key==K_s:
                keys[4]=True
            elif event.key==K_x:
                keys[5]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False
            elif event.key==K_s:
                keys[4]=False
            elif event.key==K_x:
                keys[5]=False
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)
    # 9 - Move player
    if keys[0]:
        playerpos[1]-=1
    elif keys[2]:
        playerpos[1]+=1
    if keys[1]:
        playerpos[0]-=1
    elif keys[3]:
        playerpos[0]+=1
    elif keys[4]:
        angle += 0.5
    elif keys[5]:
        angle -= 0.5