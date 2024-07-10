# flake8: noqa
import objectbase
import items
import time
from const import *

class BballShooter(objectbase.ObjectBase):
    '''Bballshooter inherits id (in object_dict map) and position from Object base.
        It summons bball.
    '''
    def __init__(self, pos):
        super().__init__(BBALLSHOOTER_ID, pos)
        self.hasbball = False
        self.readytoshoot = False
        self.summon_CD = 8 # summons bball every 8 seconds
        self.pre_summon_time = 0

    def update(self):
        if time.time() - self.pre_summon_time <= self.summon_CD:
            return super().update()
        # elif time_elapse is 8 seconds, summons and resets pre_summon_time to now
        self.pre_summon_time = time.time()
        self.hasbball = False
        self.readytoshoot = True
        self.pathIndex = 0
        return super().update()

    def hasSummon(self):
        return self.hasbball
    
    def checkImageIndex(self):
        '''Changes gesture by updating frame index.'''
        if time.time() - self.preIndexTime <= self.getImageIndexCD():
            # updates every 0.2 seconds
            return
        self.preIndexTime = time.time()

        idx = self.pathIndex + 1
        if idx == 2 and self.readytoshoot:
            # shoot at 2nd frame
            self.hasbball = True

        if idx >= self.pathIndexCount:
            idx = 0
        self.updateIndex(idx)

    def doSummon(self):
        if self.hasSummon():
            self.hasbball = False
            return items.Basketball((self.pos[0]+self.size[0], self.pos[1]))