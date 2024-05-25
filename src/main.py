# flake8: noqa
import pygame
import sys
from pygame.locals import *
from const import *
from game import *
import image
import zombiebase
import peabullet
import kunkun

pygame.init()

DS = pygame.display.set_mode( GAME_SIZE )
game = Game(DS)

background = image.Image('pic/Background/Background_0.jpg', 0, (0, 0), (1280, 600), 0)
bullet = peabullet.PeaBullet(0, (0, 200))
kun = kunkun.KunKun("kun", (1280, 200))
pbb = image.Image('pic/pbb.png', 0, (220, 60), (120, 120), 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.mouseClickHandler(event.button)

    game.update()
    DS.fill((255, 255, 255))
    game.draw()
    # bullet.draw(DS)
    # bullet.update()
    kun.draw(DS)
    kun.update()
    # pbb.draw(DS)

    pygame.display.update()

