import pygame
import random

from Ball import Ball
from Paddle import Paddle
from Block import Block
from Resources import *
from Powerup import Powerup

        
pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Arkanoid')
background = pygame.Surface(screen_size)
background = background.convert()
background.fill((250, 250, 250))
score_font = pygame.font.Font(None, 36)
        
score = 0
done = False

ball1 = Ball()
paddle = Paddle()
blocks = []
powerups = []
for i in range(10):
    for j in range(10):
        blocks.append(Block(resources['verde'],(i*48 +100 , j*24 +100)))


clock = pygame.time.Clock()
last_key = None
while not done:
    
    pressed = pygame.key.get_pressed()
        
    if pressed[pygame.K_LEFT]:
        paddle.moveLeft()
    if pressed[pygame.K_RIGHT]:
        paddle.moveRight()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    x,y = ball1.pos
    if ball1.collidesIn(x+ball1.speed[0], y):
        ball1.bounceX()

        
    if ball1.collidesIn(x, y+ball1.speed[1]):
        ball1.bounceY()
    
    ball1.moveRelative(ball1.speed[0],ball1.speed[1])
    
    paddle.update()
    
    if pygame.sprite.collide_rect(paddle, ball1):
        ball1.bounceY()
        ball1.speed = (5*(paddle.pos[0]/ball1.pos[0]), ball1.speed[1])
        if ball1.pos[1] > paddle.pos[1] : 
            offset = -20
        else:
            offset = 20
        paddle.recoil(offset)
    
    block_to_remove = None
    for block in blocks:    
        if pygame.sprite.collide_rect(ball1,block):
            ball1.bounceAgainst(block)
            block_to_remove = block
            score += 10
            if random.random() < 0.1:
                powerups.append(Powerup(resources['rojo'], block.pos))
            
    powerup_to_remove = None
    for powerup in powerups:
        powerup.update()
        if pygame.sprite.collide_rect(paddle,powerup) or powerup.pos[1]>screen_size[1]:
            powerup_to_remove = powerup
    if powerup_to_remove:
        powerups.remove(powerup_to_remove)
    if block_to_remove:
        blocks.remove(block_to_remove)
            
    for block in blocks:
        background.blit(block.image,block.rect)
    for powerup in powerups:
        background.blit(powerup.image,powerup.rect)
    
    background.blit(score_font.render(str(score), 1, (10, 10, 10)),pygame.Rect(0,0,20,20))
    background.blit(ball1.image,ball1.rect)
    background.blit(paddle.image,paddle.rect)
    
    screen.blit(background, (0, 0))
    pygame.display.flip()
    background.fill((250, 250, 250))
    clock.tick(60)
    
