# flake8: noqa
import objectbase
import items
import time
from const import *

class PeaShooter(objectbase.ObjectBase):
    '''Sunflower inherits id (in object_dict map) and position from Object base.
        It summons bullet.
    '''
    def __init__(self, id, pos):
        super().__init__(id, pos)
        self.hasBullet = False
        self.readytoshoot = False
        self.summon_CD = 1 # summons Bullet every 8 seconds
        self.pre_summon_time = 0

    def update(self):
        if time.time() - self.pre_summon_time <= self.summon_CD:
            return super().update()
        # elif time_elapse is 8 seconds, summons and resets pre_summon_time to now
        self.pre_summon_time = time.time()
        self.hasBullet = False
        self.readytoshoot = True
        self.pathIndex = 0
        return super().update()

    def hasSummon(self):
        return self.hasBullet
    
    def checkImageIndex(self):
        '''Changes gesture by updating frame index.'''
        if time.time() - self.preIndexTime <= self.getImageIndexCD():
            # updates every 0.2 seconds
            return
        self.preIndexTime = time.time()

        idx = self.pathIndex + 1
        if idx == 2 and self.readytoshoot:
            # shoot at 2nd frame
            self.hasBullet = True

        if idx >= self.pathIndexCount:
            idx = 0
        self.updateIndex(idx)

    def doSummon(self):
        if self.hasSummon():
            self.hasBullet = False
            return items.PeaBullet((self.pos[0]+self.size[0], self.pos[1]))