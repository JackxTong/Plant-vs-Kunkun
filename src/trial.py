import pygame
import sys
from pygame.locals import *
import peabullet
import basketball

pygame.init()
bball = basketball.Basketball("basketball", (40, 200))
bullet = peabullet.PeaBullet(0, (100, 200))
DS = pygame.display.set_mode( (1280, 600) )
image = pygame.image.load('pic/other/back.png')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DS.fill( (255, 255, 255 ) )
    DS.blit(image, image.get_rect() )
    bball.draw(DS)
    bullet.draw(DS)
    pygame.display.update()
