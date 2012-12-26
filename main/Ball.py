import pygame
from Resources import *

       
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__( self )
        self.imageFile = resources['ball']
        self.image = pygame.image.load(self.imageFile).convert_alpha()
        self.rect = self.image.get_rect().move(490,490)
        self.speed = (5,5)
        self.pos = self.rect.topleft
    
    def collidesIn(self,posX,posY):
        return not pygame.Rect(0,0,screen_size[0],screen_size[1]).collidepoint(posX,posY)
    
    def moveRelative(self,x,y):
        self.rect = self.rect.move(x,y)
        self.pos = self.rect.topleft

    def bounceX(self):
        self.speed = -1*self.speed[0],self.speed[1]

    def bounceY(self):
        self.speed = self.speed[0],-1*self.speed[1]
    

    def collides_from_left(self, block):
        return self.pos[0]+self.rect.width/2 <= block.pos[0]
    
    
    def collides_from_right(self, block):
        return self.pos[0]-self.rect.width/2 >= block.pos[0]
    
    
    def aligned_with(self, block):
        return -block.rect.height/2 < self.pos[1] -block.pos[1] <  block.rect.height/2 
    
    
    def collides_from_sides(self, block):
        return self.aligned_with(block) and (self.collides_from_left(block) or self.collides_from_right(block))
    
    
    def bounceAgainst(self,block):
        if self.collides_from_sides(block):
            self.bounceX()
        else:
            self.bounceY()