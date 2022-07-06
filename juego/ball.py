from math import radians
from turtle import speed
import pygame
from random import randint

from .constants import  SCREEN_HEIGTH, SCREEN_WIDTH, COLLISION_PELOTA, SPEED_BALL_MAX

class Ball (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/pelota.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.pos_x = SCREEN_WIDTH / 2
        self.pos_y = SCREEN_HEIGTH / 2
        self.rect.center = (self.pos_x, self.pos_y)
        self.velocity = [randint(2,4), randint(-4,4)]

    def update (self):
        if self.pos_x < 11 or self.pos_x > SCREEN_WIDTH - 11 :
            self.velocity [0] = -self.velocity[0]
        
        if self.pos_y < 11:
            self.velocity [1] = -self.velocity[1]
        
        if self.velocity[0] == 0:
            self.velocity[0] += 1

        if self.velocity[1] == 0:
            self.velocity[1] +=1 
        
        self.pos_x += self.velocity[0]
        self.pos_y += self.velocity[1]

        self.rect.center = (self.pos_x, self.pos_y)

    def reset (self):

        self.velocity = [randint(2,4), randint(-4,4)]
        self.pos_x = SCREEN_WIDTH / 2
        self.pos_y = SCREEN_HEIGTH / 2
        self.rect.center = (self.pos_x, self.pos_y)


    def check_collition (self,player):
        if self.rect.colliderect(player):
            if abs(self.rect.bottom - player.rect.top) < COLLISION_PELOTA and self.velocity[1] > 0 :
                self.velocity[1] = -self.velocity[1]
                self.velocity[0] = +self.velocity[0]

                if self.velocity[0] > SPEED_BALL_MAX:
                    self.velocity[0] = SPEED_BALL_MAX
                if self.velocity[0] < SPEED_BALL_MAX:
                    self.velocity[0] = SPEED_BALL_MAX
            else: 
                self.velocity[0] *= -1


    def down_ball(self):
        return self.pos_y > SCREEN_HEIGTH

    def bounce(self):
        self.velocity[0] = self.velocity[0]
        self.velocity[1] = -self.velocity[1]
         
        
