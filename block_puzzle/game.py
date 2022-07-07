import sys
from typing_extensions import Self

import pygame

from .constants import SCREEN_HEIGTH, SCREEN_WIDTH
from .player import Player
from .ball import Ball
from .brick import Bricks

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
        self.nombre = pygame.display.set_caption("Block Puzzle")
        
        self.clock = pygame.time.Clock()
        
        self.bg_color = pygame.Color("black")
        self.bg_color1 = pygame.Color("white")

        self.font_game_over =  pygame.font.SysFont("Arial", 30, italic=True)
        self.font_lifes =  pygame.font.SysFont("Arial", 16, italic=True)

        self.player = Player()
        self.ball = Ball()

        self.all_sprite = pygame.sprite.Group()
        self.all_sprite.add(self.player, self.ball)

        self.brick = Bricks(self.all_sprite)

        self.game_over = False

    def rest(self):
        self.game_over = False
        self.player = Player()
        self.ball = Ball()

        self.all_sprite.empty()
        self.all_sprite.add(self.player, self.ball)
        self.brick = Bricks(self.all_sprite)
        

    def all_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.left_move()
        if keys[pygame.K_RIGHT]:
            self.player.right_move()
        
        if self.game_over and keys[pygame.K_SPACE]:
            self.rest()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        if self.ball.down_ball():
            self.player.lose_life()
            if self.player.life <= 0:
                self.game_over= True
            self.ball.reset()
        self.ball.check_collition(self.player)
        self.brick.check_collision(self.ball)
        self.all_sprite.update()
       
        pygame.display.update()
       
        self.clock.tick(60)

    def draw(self):
        self.screen.fill(self.bg_color)

        if self.game_over :
            text = self.font_game_over.render("Game Over!",1, pygame.Color("white"))
            self.screen.blit(text, (SCREEN_HEIGTH/2 + 32, SCREEN_WIDTH/2-100))

            text = self.font_lifes.render("Press Space to try again!",1, pygame.Color("white"))
            self.screen.blit(text, (SCREEN_HEIGTH/2 +32, SCREEN_WIDTH-2))
        else:
            self.all_sprite.draw(self.screen)
            text = self.font_lifes.render("Lifes {0}".format(self.player.life),1, pygame.Color("white"))
            self.screen.blit(text, (24,SCREEN_HEIGTH-32))
