import pygame
from Resources import *

class Paddle(pygame.sprite.Sprite):
    def __init__(self, startPosition=(500,500)):
        pygame.sprite.Sprite.__init__(self)
        self.imageFile= resources['paddle']
        self.image = pygame.image.load(self.imageFile).convert_alpha()
        self.rect = self.image.get_rect().move(startPosition[0],startPosition[1])
        self.startPosition = startPosition
        self.pos = startPosition
    
    def update(self):
        if self.pos[1] > self.startPosition[1]:
            self.pos = (self.pos[0],self.pos[1]-1)
        if self.pos[1] < self.startPosition[1]:
            self.pos = (self.pos[0],self.pos[1]+1)
        self.rect.center = self.pos
        
    def moveLeft(self):
        if (self.pos[0] >= self.rect.width/2 ):
            self.pos = (self.pos[0]-5,self.pos[1])
        self.rect.center = self.pos
        
    def moveRight(self):
        if self.pos[0] <= screen_size[0]-self.rect.width/2 : 
            self.pos = (self.pos[0]+5,self.pos[1])
        self.rect.center = self.pos

    def recoil(self,offset):
        minOffset = self.startPosition[1]-40
        maxOffset = self.startPosition[1]+40
        newPosY = min(max(self.pos[1]+offset,minOffset),maxOffset)
        self.pos = (self.pos[0],newPosY)
