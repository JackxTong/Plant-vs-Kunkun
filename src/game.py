# flake8: noqa
import image
import sunflower
import chickenflower
import peashooter
import bballshooter
import zombiebase
import musicaudio
from const import *
import pygame
import time
import random
from object_dict import data

path_bg = 'pic/Background/Background_0.jpg'

class Game:
    def __init__(self, ds):
        self.ds = ds
        self.bg = image.Image(path_bg, 0, (0, 0), GAME_SIZE, 0) # background
        self.plants = []
        self.summons = [] # sunlight / chicken
        self.zombies = []
        self.zombie_generate_time = 0
        self.gold = 10000
        self.__hasPlant()
        musicaudio.bgm()

    def __hasPlant(self):
        # initialize hasPlant to m*n matrix, entry=0 means no plant (can plant)
        self.hasPlant = []
        for i in range(GRID_SIZE[0]):
            col = []
            for j in range(GRID_SIZE[1]):
                col.append(0)
            self.hasPlant.append(col)

    def print_gold(self):
        font = pygame.font.Font(None, 60)
        textImage = font.render("Gold: " + str(self.gold), True, (0, 0, 0))
        self.ds.blit(textImage, (603, 23)) # black shade

        textImage = font.render("Gold: " + str(self.gold), True, (255, 255, 255))
        self.ds.blit(textImage, (600, 20)) # white font

    def draw(self):
        self.bg.draw(self.ds)
        for plant in self.plants:
            plant.draw(self.ds)
        for summon in self.summons:
            summon.draw(self.ds)
        for zombie in self.zombies:
            zombie.draw(self.ds)
        self.print_gold()

    def update(self):
        self.bg.update()
        for plant in self.plants:
            plant.update()
            if plant.hasSummon(): # is sunflower / chickenflower
                photon_summon = plant.doSummon()
                self.summons.append(photon_summon)
        for photon in self.summons:
            photon.update()
        for zombie in self.zombies:
            zombie.update()
        if time.time() - self.zombie_generate_time > ZOMBIE_CD:
            self.zombie_generate_time = time.time()
            self.add_zombie()


    def clicksunlight(self, mousePos):
        for summon in self.summons:
            if summon.id == SUNLIGHT_ID or summon.id == CHICKEN_ID: # is sunlight or chick
                rect = summon.getRect() # location of sunlight
                if rect.collidepoint(mousePos): # mouse click sunlight
                    if summon.id == CHICKEN_ID:
                        musicaudio.ji()
                    else:
                        musicaudio.niganma()
                    self.summons.remove(summon)
                    self.gold += summon.getPrice()
                    return

    def add_sunflower(self, x, y):
        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        sf = sunflower.SunFlower(pos)
        self.plants.append(sf)

    def add_chickflower(self, x, y):
        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        cf = chickenflower.ChickenFlower(pos)
        self.plants.append(cf)

    def add_peashooter(self, x, y):
        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        ps = peashooter.PeaShooter(pos)
        self.plants.append(ps)

    def add_bballshooter(self, x, y):
        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        bs = bballshooter.BballShooter(pos)
        self.plants.append(bs)

    def add_zombie(self):
        '''Adds zombie at a random row at the screen right (x=14 grids).'''
        x = 14
        y = random.randint(0, GRID_COUNT[1])
        for y in range(GRID_COUNT[1]):
            # need to adjust y coord of zombie to fit
            pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + (y-0.5) * GRID_SIZE[1]
            zombie = zombiebase.ZombieBase(pos)
            self.zombies.append(zombie)
        

    def get_grid_by_mouse(self, pos):
        x = (pos[0] - LEFT_TOP[0]) // GRID_SIZE[0]
        y = (pos[1] - LEFT_TOP[1]) // GRID_SIZE[1]
        return x, y
    
    def checkAddPlant(self, mousePos, plant_id):
        x,y = self.get_grid_by_mouse(mousePos)
        if x < 0 or x >= GRID_COUNT[0]:
            return 
        if y < 0 or y >= GRID_COUNT[1]:
            return 
        if self.hasPlant[x][y] == 1:
            return
        if self.gold < data[plant_id]['PRICE']:
            return
        # conditions checked, can plant
        self.gold -= data[plant_id]['PRICE']
        self.hasPlant[x][y] = 1
        if plant_id == SUNFLOWER_ID:
            self.add_sunflower(x, y)
        elif plant_id == PEASHOOTER_ID:
            self.add_peashooter(x, y)
        elif plant_id == CHICKFLOWER_ID:
            self.add_chickflower(x, y)
        elif plant_id == BBALLSHOOTER_ID:
            self.add_bballshooter(x, y)

    def mouseClickHandler(self, btn):
        # handles mouse click
        mousePos = pygame.mouse.get_pos()
        self.clicksunlight(mousePos)
        if btn == 3: # mouse left-click, plant sunflower
            # self.checkAddPlant(mousePos, CHICKFLOWER_ID)
            # self.checkAddPlant(mousePos, PEASHOOTER_ID)
            self.checkAddPlant(mousePos, BBALLSHOOTER_ID)
        elif btn == 1: # mouse right-click
            # self.checkAddPlant(mousePos, SUNFLOWER_ID)
            self.checkAddPlant(mousePos, PEASHOOTER_ID)