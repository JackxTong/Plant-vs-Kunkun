# flake8: noqa
import objectbase
import items
import time
from const import *

class ChickenFlower(objectbase.ObjectBase):
    '''Chickenflower inherits id (in object_dict map) and position from Object base.
        It summons Chicken.
    '''

    def __init__(self, pos):
        super().__init__(CHICKFLOWER_ID, pos)
        self.hasChicken = False
        self.summon_CD = 8 # summons chicken every 8 seconds
        self.pre_summon_time = 0

    def update(self):
        if time.time() - self.pre_summon_time <= self.summon_CD:
            return super().update()
        # if time_elapse is 8 seconds, summons and resets pre_summon_time to now
        self.pre_summon_time = time.time()
        self.hasChicken = True
        return super().update()

    def hasSummon(self):
        return self.hasChicken

    def doSummon(self):
        if self.hasSummon():
            self.hasChicken = False
            return items.Chicken(self.pos)