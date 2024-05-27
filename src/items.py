# flake8: noqa
import objectbase
from const import *


class PeaBullet(objectbase.ObjectBase):
    def __init__(self, pos):
        super().__init__(BULLET_ID, pos)
    pass

class KunKun(objectbase.ObjectBase):
    def __init__(self, pos):
        super().__init__(KUN_ID, pos)
    pass

class SunLight(objectbase.ObjectBase):
    def __init__(self, pos):
        super().__init__(SUNLIGHT_ID, pos)
    pass

class Basketball(objectbase.ObjectBase):
    def __init__(self, pos):
        super().__init__(BBALL_ID, pos)
    pass

class Chicken(objectbase.ObjectBase):
    '''Summoned by ChickenFlower.'''
    def __init__(self, pos):
        super().__init__(CHICKEN_ID, pos)
    pass