import pygame


class Image(pygame.sprite.Sprite):
    def __init__(self, path, pathIndex, pos, size, pathIndexCount):
        self.path = path
        self.pathIndex = pathIndex
        self.pos = list(pos)  # position
        self.size = size  # set self.image to size
        self.pathIndexCount = pathIndexCount
        self.updateImage()

    # updateIndex and updateSize for 帧动画

    def updateIndex(self, pathIndex):
        self.pathIndex = pathIndex
        self.updateImage()

    def updateImage(self):
        path = self.path
        if self.pathIndexCount != 0:
            path = path % self.pathIndex  # path = "image_%(pathIndex).png", e.g.image_1.png
        self.image = pygame.image.load(path)
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)

    def updateSize(self, size):
        self.size = size
        self.updateImage()

    def getRect(self):
        rect = self.image.get_rect() # rectangle
        rect.x, rect.y = self.pos
        return rect
    
    def draw(self, ds): # draw on image (ds is pygame.display)
        ds.blit(self.image, self.getRect())