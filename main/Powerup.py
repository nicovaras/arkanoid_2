import pygame

class Powerup(pygame.sprite.Sprite):
    def __init__(self, powerupFileName, pos = (0,0)):
        pygame.sprite.Sprite.__init__( self )
        self.imageFile=powerupFileName
        self.pos = pos
        self.image = pygame.image.load(powerupFileName).convert_alpha()
        self.rect = self.image.get_rect().move(pos[0],pos[1])
    
    def update(self):
        self.rect = self.rect.move(0,3)
        self.pos = self.rect.topleft