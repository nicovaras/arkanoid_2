import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, colorFileName, pos = (0,0)):
        pygame.sprite.Sprite.__init__( self )
        self.imageFile=colorFileName
        self.pos = pos
        self.image = pygame.image.load(colorFileName).convert_alpha()
        self.rect = self.image.get_rect().move(pos[0],pos[1])
