# flake8: noqa
import pygame
import sys
from pygame.locals import *
from const import *
from game import *
import image
import items
import menubar
from menubar import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(20)

DS = pygame.display.set_mode( GAME_SIZE )
game = Game(DS)

### try add menu bar
menu_card_list = [menubar.Card("sunflower"), menubar.Card("peashooter"), menubar.Card("chickenflower")]
menu_bar = menubar.Menubar(DS, menu_card_list)
###

background = image.Image('pic/Background/Background_0.jpg', 0, (0, 0), (1280, 600), 0)
kun = items.KunKun((1280, 200))

mousedown = False
dragging_card = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if mousedown:
            x, y = game.mouseClickHandler(event.button)
            card_name = menu_bar.mouseClickHandler(event.button)
            if card_name:
                print(f"clicked on {card_name} card")
                # can drag the card to the game board
                C = Card(card_name, (x, y))
                C.draw(DS)
                dragging_card = True
                mousedown = False
        
        if dragging_card:
            # draw card where cursor is moving
            x, y = pygame.mouse.get_pos()
            image.Image(f"pic/Cards/card_{card_name}.png", 0, (x, y), C.size, 0).draw(DS)
  
            if event.type == pygame.MOUSEBUTTONUP:
                dragging_card = False
            pygame.display.update()


    
    game.update()
    DS.fill((255, 255, 255))
    game.draw()
    menu_bar.draw()
    kun.draw(DS)
    kun.update()

    pygame.display.update()

