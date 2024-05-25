# flake8: noqa
import objectbase
import items
import time
from const import *

class SunFlower(objectbase.ObjectBase):
    '''Sunflower inherits id (in object_dict map) and position from Object base.
        It summons sunlight.
    '''

    def __init__(self, pos):
        super().__init__(SUNFLOWER_ID, pos)
        self.hasSunlight = False
        self.summon_CD = 8 # summons sunlight every 8 seconds
        self.pre_summon_time = 0

    def update(self):
        if time.time() - self.pre_summon_time <= self.summon_CD:
            return super().update()
        # if time_elapse is 8 seconds, summons and resets pre_summon_time to now
        self.pre_summon_time = time.time()
        self.hasSunlight = True
        return super().update()

    def hasSummon(self):
        return self.hasSunlight

    def doSummon(self):
        if self.hasSummon():
            self.hasSunlight = False
            return items.SunLight(self.pos)
            # self.pos[0]+20, self.pos[1]-10) # up主逻辑不知道为啥
        

    
