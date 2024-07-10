# flake8: noqa
import pygame
import sys
from pygame.locals import *
from const import *
from game import *
import image
import items

class Menubar():
    def __init__(self, ds, card_list):
        '''Card_list is list of card names in string.'''
        self.ds = ds
        self.pos = (0, 0)
        self.size = (522, 87)
        self.image = self.load_menubar()
        self.rect = self.image.getRect()
        self.first_card_x_coord = 70 # first card x coordinate
        self.card_y_coord = 4
        self.setup_cards(card_list)
        
    def load_menubar(self):
        return image.Image('pic/menu_bar.png', 0, self.pos, self.size, 0)
    
    def update(self):
        pass

    def check_menubar_click(self):
        pass

    def draw(self):
        self.image.draw(self.ds)
        for card in self.card_list:
            card.draw(self.ds)

    def setup_cards(self, card_list):
        self.card_list = []
        x = self.first_card_x_coord
        y = self.card_y_coord
        for c in card_list:
            pos = (x, y)
            x += 60
            self.card_list.append(Card(c.name, pos))

    # make menubar clickable
    def mouseClickHandler(self, button):
        if button == 1:
            x, y = pygame.mouse.get_pos()
            if self.rect.collidepoint(x, y):
                for card in self.card_list:
                    if card.image.getRect().collidepoint(x, y):
                        print(f"clicked on {card.name} card")
                        # can drag the card to the game board
                        card.image.move(x, y)
                        card.image.draw(self.ds)
                        if card.name == "sunflower":
                            print("sunflower")



class Card():
    def __init__(self, name, pos=(0,0)):
        '''Name is the plant name in string.'''
        self.name = name 
        self.x = pos[0]
        self.y = pos[1]
        self.size = (55, 76.4) # orignal size: (64, 89)
        self.image = image.Image(f"pic/Cards/card_{self.name}.png", 0, (self.x, self.y), self.size, 0)
    
    def draw(self, ds):
        self.image.draw(ds)
