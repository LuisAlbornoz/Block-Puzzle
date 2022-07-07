from tkinter import CENTER
import pygame

from .constants import SCREEN_HEIGTH, SCREEN_WIDTH, SPEED_BARRA, START_LIFE


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/barra.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.pos_x = SCREEN_WIDTH / 2
        self.pos_y = SCREEN_HEIGTH - 50
        self.rect.center = (self.pos_x, self.pos_y)
        self.direction = 8
        self.life = START_LIFE

    def update(self):
        if self.pos_x < 52:
            self.pos_x = 52
        if self.pos_x > SCREEN_WIDTH - 52:
            self.pos_x = SCREEN_WIDTH - 52

        self.rect.center = (self.pos_x, self.pos_y)

    def lose_life(self):
        self.life -= 1

    def reset(self):
        self.life = START_LIFE

    def left_move(self):
        self.pos_x -= SPEED_BARRA
        self.direction -= 1

    def right_move(self):
        self.pos_x += SPEED_BARRA
        self.direction += 1
