import objectbase
from const import *


class ZombieBase(objectbase.ObjectBase):
    def __init__(self, pos):
        super().__init__(ZOMBIE_ID, pos)