import image
import time
import object_dict

class ObjectBase(image.Image):
    def __init__(self, id, pos):
        self.id = id
        self.preIndexTime = 0
        self.prePositionTime = 0
        super().__init__(
            self.getData()["PATH"],
            0,
            pos,
            self.getData()["SIZE"],
            self.getData()['IMAGE_INDEX_MAX']
        )

    def getData(self):
        return object_dict.data[self.id]
    
    def getSpeed(self):
        return self.getData()["SPEED"]
    
    def getPositionCD(self):
        return self.getData()['POSITION_CD']
    
    def getImageIndexCD(self):
        return self.getData()['IMAGE_INDEX_CD']
    
    def getPrice(self):
        return self.getData()['PRICE']

    def update(self):
        self.checkImageIndex()
        self.checkPosition()

    def checkImageIndex(self):
        '''Changes gesture by updating frame index.'''
        if time.time() - self.preIndexTime <= self.getImageIndexCD():
            # updates every 0.2 seconds
            return
        self.preIndexTime = time.time()

        idx = self.pathIndex + 1
        if idx >= self.pathIndexCount:
            idx = 0
        self.updateIndex(idx)

    def checkPosition(self):
        if time.time() - self.prePositionTime <= self.getPositionCD():
            # updates position every 0.2s
            return False
        self.prePositionTime = time.time()
        speed = self.getSpeed()
        # self.pos = ( self.pos[0] + speed[0], self.pos[1] + speed[1])
        self.pos[0] += speed[0]
        self.pos[1] += speed[1]
        return True

